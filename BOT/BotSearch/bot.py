import discord
from discord import app_commands
import asyncio
from datetime import datetime, timedelta, timezone
from rapidfuzz import fuzz
from colorama import Fore, Style, init

intents = discord.Intents.default()
intents.message_content = True

init(autoreset=True)

class Bot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.cached_results = {}
        self.cache_duration = timedelta(minutes=10)

    async def setup_hook(self):
        await self.tree.sync()

    def clear_old_cache(self):
        now = datetime.now(timezone.utc)
        self.cached_results = {
            key: value for key, value in self.cached_results.items()
            if now - value[0] <= self.cache_duration
        }

    def log_and_format_response(self, interaction, text, results, page, total_pages):
        start_index = page * 30
        end_index = min(start_index + 30, len(results))
        paginated_results = results[start_index:end_index]

        log_message = (
            f"{Fore.GREEN}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"{Fore.YELLOW}{interaction.user.name}{Fore.RESET} tìm kiếm: \"{text}\" - "
            f"{len(paginated_results)} kết quả trang {page + 1}/{total_pages}: "
            f"{', '.join(Fore.BLUE + result[0] + Fore.RESET for result in paginated_results)}"
        ) if results else (
            f"{Fore.GREEN}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"{Fore.YELLOW}{interaction.user.name}{Fore.RESET} tìm kiếm: \"{text}\" - "
            f"Không tìm thấy kênh nào phù hợp."
        )
        
        print(log_message)

        formatted_results = "\n".join(result[1] for result in paginated_results)
        return (
            f"**🔍 Người dùng:** {interaction.user.name}\n"
            f"**📝 Tìm kiếm:** \"{text}\"\n"
            f"**📊 Số kết quả:** {end_index}/{len(results)}\n"
            f"**Trang {page + 1} trên {total_pages}**\n"
            f"**--------------------**\n"
            f"{formatted_results}\n"
            f"**--------------------**"
        )

    async def send_paginated_message(self, interaction, message, text, results, page):
        total_pages = (len(results) + 29) // 30
        embed = discord.Embed(description=message, color=discord.Color.purple())
        view = discord.ui.View(timeout=180.0)

        if (page + 1) * 30 < len(results):
            next_button = discord.ui.Button(
                label=f"Tiếp tục (Trang {page + 1}/{total_pages})",
                emoji="➡️",
                style=discord.ButtonStyle.primary,
                custom_id=f"next_{text}_{page}"
            )
            next_button.callback = self.get_next_page_callback(interaction, text, page + 1, total_pages)
            view.add_item(next_button)

        if interaction.response.is_done():
            await interaction.followup.send(embed=embed, view=view)
        else:
            await interaction.response.send_message(embed=embed, view=view)

    def get_next_page_callback(self, interaction, text, page, total_pages):
        async def callback(interaction):
            self.clear_old_cache()
            cached_data = self.cached_results.get(text)
            
            if cached_data:
                _, results = cached_data
            else:
                results = await asyncio.gather(*[search_in_channel(channel, text) for channel in interaction.guild.text_channels])
                results = sorted((result for result in results if result), key=lambda x: x[2], reverse=True)
                self.cached_results[text] = (datetime.now(timezone.utc), results)

            response = self.log_and_format_response(interaction, text, results, page, total_pages)
            await interaction.response.edit_message(embed=discord.Embed(description=response, color=discord.Color.purple()), view=None)
            
            if (page + 1) * 30 < len(results):
                await self.send_paginated_message(interaction, response, text, results, page)
        
        return callback

bot = Bot()

EXCEPTION_CHANNELS = {"1275454710706470943", "1275452856102817833", "1273140752687435840", "1274553646490583062", "1275453489077555211"}

@bot.event
async def on_ready():
    print(f"{Fore.CYAN}Bot {bot.user} đã khởi động!{Style.RESET_ALL}")

async def search_in_channel(channel, text, threshold=83):
    if str(channel.id) in EXCEPTION_CHANNELS:
        return None
    similarity = fuzz.partial_ratio(text.lower(), channel.name.lower())
    return (channel.name, f"<#{channel.id}>", similarity) if similarity >= threshold else None

@bot.tree.command(name="search", description="Tìm kiếm kênh plugins.")
async def search(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    bot.clear_old_cache()

    cached_data = bot.cached_results.get(text)
    if cached_data:
        _, cached_response = cached_data
        await interaction.followup.send(cached_response)
        return

    results = await asyncio.gather(*[search_in_channel(channel, text) for channel in interaction.guild.text_channels])
    results = sorted((result for result in results if result), key=lambda x: x[2], reverse=True)
    total_pages = (len(results) + 29) // 30
    response = bot.log_and_format_response(interaction, text, results, page=0, total_pages=total_pages)
    await bot.send_paginated_message(interaction, response, text, results, page=0)

@bot.tree.command(name="info", description="Hiển thị thông tin của bot.")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="BotSearch v1.0.0",
        description="Overview",
        color=discord.Color.purple()
    )
    embed.add_field(name="Author", value="@karisan", inline=True)
    embed.add_field(name="Client", value="@nghialonton", inline=True)
    embed.add_field(name="Language", value="Python", inline=True)
    embed.add_field(name="Library", value="discord.py", inline=True)
    embed.add_field(name="Version", value="1.0.0", inline=True)
    embed.set_footer(text="For any inquiries, contact @nghialonton")

    await interaction.response.send_message(embed=embed)

bot.run('MTIxNDEyMTkzMjAxOTA3MzA1NQ.GrUMQB.xesQ8IDFClX5nyO8ldOe3no855NAyzaIlsghoQ')
