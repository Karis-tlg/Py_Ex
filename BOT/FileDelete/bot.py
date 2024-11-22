import discord
import asyncio
from discord.ext import commands

SERVER_ID = 1276088606909403136

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)
webhook_cache = {}  # Bộ nhớ cache cho webhook của mỗi kênh

@bot.event
async def on_ready():
    print(f'{bot.user} đã kết nối tới Discord!')
    await delete_all_files()

async def delete_all_files():
    guild = bot.get_guild(SERVER_ID)
    if not guild:
        print("Không tìm thấy server.")
        return

    for channel in guild.text_channels:
        async for msg in channel.history(limit=None):
            if msg.attachments:
                await handle_message(msg)
                await asyncio.sleep(0.5)  # Tăng thời gian đợi giữa các tin nhắn
        await asyncio.sleep(1)  # Thời gian đợi giữa các kênh

async def handle_message(msg):
    attachment_names = ', '.join([att.filename for att in msg.attachments])

    try:
        if msg.webhook_id:
            await msg.delete()
            await send_message(msg)
            print(f"Đã xoá tin nhắn từ Webhook trong kênh: {msg.channel.name}")
        elif not msg.content.strip():
            await msg.delete()
            print(f"Đã xoá file: {attachment_names} trong kênh: {msg.channel.name}")
        else:
            await msg.delete()
            await send_message(msg)
            print(f"Đã xoá file: {attachment_names} và gửi lại tin nhắn trong kênh: {msg.channel.name}")

    except discord.HTTPException as e:
        if e.status == 429:
            retry_after = int(e.headers.get('Retry-After', 1))
            print(f"Bị giới hạn tốc độ. Đợi {retry_after + 0.5} giây.")
            await asyncio.sleep(retry_after + 0.5)

async def send_message(msg):
    webhook = await get_or_create_webhook(msg.channel)
    username = msg.author.display_name if not msg.webhook_id else "NexusUtils"
    avatar_url = str(msg.author.avatar) if msg.author.avatar else "https://i.imgur.com/tHfRXIO.jpeg"
    await webhook.send(content=msg.content, username=username, avatar_url=avatar_url)

async def get_or_create_webhook(channel):
    # Kiểm tra bộ nhớ cache để lấy webhook cho kênh
    if channel.id in webhook_cache:
        return webhook_cache[channel.id]

    webhooks = await channel.webhooks()
    for webhook in webhooks:
        if webhook.token:
            webhook_cache[channel.id] = webhook
            return webhook

    webhook = await channel.create_webhook(name="NexusUtils")
    webhook_cache[channel.id] = webhook
    return webhook

bot.run("")  # Thay thế bằng token của bạn
