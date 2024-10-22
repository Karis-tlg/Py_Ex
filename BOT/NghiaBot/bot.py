import discord
import os
import re
import json
import asyncio
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from difflib import SequenceMatcher
from colored import fg, attr

#
# NghiaBot code by karis (discord: _karisan_)
#

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

PLUGIN_FOLDER = 'plugins'
SNACK_FILE = 'snack.json'
WHITELISTED_PREFIX = ['[Colorful]']  
WHITELISTED_USERS = {'807941826058'}
EXCEPTION_CHANNELS = {"1275476968334430339"}

def load_snack_config():
    try:
        with open(SNACK_FILE, 'r') as file:
            config = json.load(file)
            for entry in config.get('blacklist', []):
                if 'channel-id' in entry and 'name' not in entry:
                    EXCEPTION_CHANNELS.update(entry['channel-id'])
            return config
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"{fg('red')}Lỗi đọc file {SNACK_FILE}: {e}{attr('reset')}")
        return {"blacklist": [], "whitelist": []}

def normalize_plugin_name(plugin_name):
    plugin_name = plugin_name.lower()
    plugin_name = re.sub(r'[\s_\[\]]', '-', plugin_name)
    plugin_name = re.sub(r'-v?\d+[\._\d]*(-snapshot)?', '', plugin_name)
    plugin_name = re.sub(r'-b\d+', '', plugin_name)
    plugin_name = re.sub(r'-jar$', '', plugin_name)
    plugin_name = re.sub(r'[^a-z0-9-]', '', plugin_name)
    plugin_name = plugin_name.strip('-')
    return plugin_name

def is_plugin_allowed(plugin_filename, channel_id, config):
    if str(channel_id) in EXCEPTION_CHANNELS:
        return False

    plugin_name = plugin_filename
    whitelist = config.get('whitelist', [])
    blacklist = config.get('blacklist', [])

    for entry in whitelist:
        if plugin_name in entry.get('name', []):
            allowed_channels = entry.get('channel-id', [])
            block_global = entry.get('block-global', 'false').lower() == 'true'
            if block_global and str(channel_id) not in allowed_channels:
                return False
            return True

    for entry in blacklist:
        if plugin_name in entry.get('name', []):
            if 'channel-id' not in entry or str(channel_id) in entry['channel-id']:
                return False

    return True

def find_best_channel(plugin_name, channels):
    normalized_plugin_name = normalize_plugin_name(plugin_name)
    parts = normalized_plugin_name.split('-')

    best_match = None
    highest_similarity = 0.0

    for i in range(1, len(parts) + 1):
        partial_name = '-'.join(parts[:i])
        for channel_name, channel_id in channels.items():
            similarity = SequenceMatcher(None, partial_name, channel_name).ratio()
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = (channel_name, channel_id)

            similarity_no_hyphen = SequenceMatcher(None, partial_name, channel_name.replace('-', '')).ratio()
            if similarity_no_hyphen > highest_similarity:
                highest_similarity = similarity_no_hyphen
                best_match = (channel_name, channel_id)

    if best_match and highest_similarity >= 0.8:
        return best_match[0], best_match[1], highest_similarity
    return None, None, None

def should_skip_plugin(plugin_filename):
    for prefix in WHITELISTED_PREFIX:
        if plugin_filename.startswith(prefix):
            return True
    return False

async def check_permissions_and_execute(ctx, command_func):
    if str(ctx.author.id) not in WHITELISTED_USERS:
        print(f"{fg('yellow')}Người dùng {ctx.author} ({ctx.author.id}) không có quyền sử dụng lệnh: {ctx.command}{attr('reset')}")
        await ctx.send("Bạn không có quyền sử dụng lệnh này.", hidden=True)
        return
    try:
        await command_func(ctx)
    except Exception as error:
        print(f"{fg('red')}Lỗi: {error}{attr('reset')}")
        await ctx.send("Đã xảy ra lỗi khi thực thi lệnh này.", hidden=True)
        raise error

@bot.event
async def on_ready():
    print(f"{fg('green')}Đăng nhập thành công: {bot.user}{attr('reset')}")

@slash.slash(name="channel", description="Quản lý kênh")
async def channel(ctx: SlashContext):
    await check_permissions_and_execute(ctx, lambda ctx: ctx.send("Sử dụng lệnh: `/channel upload` hoặc `/channel sort`.", hidden=True))

@slash.subcommand(base="channel", name="upload", description="Upload các plugin từ thư mục được chỉ định lên các kênh phù hợp")
async def upload_plugins(ctx: SlashContext):
    async def upload_command(ctx):
        print(f"{fg('yellow')}Upload Plugins{attr('reset')}")
        config = load_snack_config()
        channels = {ch.name.lower(): ch.id for ch in ctx.guild.channels if isinstance(ch, discord.TextChannel)}

        results = [0, 0, 0]  # pl done, false, sx done

        for filename in os.listdir(PLUGIN_FOLDER):
            if filename.endswith('.jar'):
                if should_skip_plugin(filename):
                    print(f"{fg('blue')}Skipped: {filename} (Prefix is whitelisted){attr('reset')}")
                    continue

                plugin_name = os.path.splitext(filename)[0]
                channel_name, channel_id, similarity = find_best_channel(plugin_name, channels)
                normalized_plugin_name = normalize_plugin_name(plugin_name)

                if channel_name and channel_id:
                    if is_plugin_allowed(filename, channel_id, config):
                        try:
                            await bot.get_channel(channel_id).send(file=discord.File(os.path.join(PLUGIN_FOLDER, filename)))
                            print(f"{fg('green')}Done: {filename} -> {normalized_plugin_name} -> {channel_name} | Tỷ lệ: {similarity:.2f}{attr('reset')}")
                            results[0] += 1
                        except Exception as e:
                            print(f"{fg('red')}Lỗi khi upload: {filename} lên {channel_name}: {e}{attr('reset')}")
                            results[1] += 1
                    else:
                        print(f"{fg('red')}Error: {filename} -> {normalized_plugin_name} (Không được phép upload){attr('reset')}")
                        results[1] += 1
                else:
                    print(f"{fg('red')}Error: {filename} -> {normalized_plugin_name} (Không tìm thấy kênh phù hợp){attr('reset')}")
                    results[1] += 1

        print(f"{fg('green')}Upload thành công {results[0]} plugin, thất bại {results[1]}/{results[0] + results[1]} plugin.{attr('reset')}")

    await check_permissions_and_execute(ctx, upload_command)

@slash.subcommand(base="channel", name="sort", description="Sắp xếp các kênh trong server theo thứ tự A-Z")
async def sort_channels(ctx: SlashContext):
    async def sort_command(ctx):
        print(f"{fg('yellow')}Sort Channel{attr('reset')}")
        initial_sleep_time = 2

        results = [0, 0, 0]  # pl done, false, sx done

        for category in ctx.guild.categories:
            sorted_channels = sorted(category.channels, key=lambda c: c.name.lower())
            for i, channel in enumerate(sorted_channels):
                if channel.position != i:
                    try:
                        await channel.edit(position=i)
                        print(f"{fg('cyan')}Sắp xếp: {channel.name} -> Vị trí: {i} -> #{category.name}{attr('reset')}")
                        await asyncio.sleep(initial_sleep_time)
                        results[2] += 1
                    except discord.errors.HTTPException as e:
                        print(f"{fg('red')}Lỗi khi sắp xếp kênh {channel.name}: {e}{attr('reset')}")

        total_channels = sum(len(category.channels) for category in ctx.guild.categories)
        print(f"{fg('green')}Sắp xếp thành công {results[2]}/{total_channels} kênh.{attr('reset')}")

    await check_permissions_and_execute(ctx, sort_command)

bot.run('', root_logger=True)
