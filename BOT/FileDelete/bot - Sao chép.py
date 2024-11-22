import discord
import asyncio
from discord.ext import commands

SERVER_ID = 1276088606909403136

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

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
                await asyncio.sleep(0.3)
        await asyncio.sleep(0.6)  

async def handle_message(msg):
    attachment_names = [att.filename for att in msg.attachments]
    try: 
        if msg.webhook_id:
            await msg.delete() 
            await send_webhook_message(msg)
            print(f"Đã xoá tin nhắn từ Webhook trong kênh: {msg.channel.name}")
        elif not msg.content.strip():
            await msg.delete()   
            print(f"Đã xoá file: {', '.join(attachment_names)} trong kênh: {msg.channel.name}")
        else:  
            await msg.delete()
            await send_user_message(msg)
            print(f"Đã xoá file: {', '.join(attachment_names)} và gửi lại tin nhắn trong kênh: {msg.channel.name}")
    except discord.HTTPException as e:
        if e.status == 429:
            await asyncio.sleep(int(e.headers.get('Retry-After', 1)) + 0.2)

async def send_webhook_message(msg):
    webhook = await msg.channel.create_webhook(name="NexusUtils")
    await webhook.send(msg.content, username="NexusUtils", avatar_url="https://i.imgur.com/tHfRXIO.jpeg")
    await webhook.delete()

async def send_user_message(msg):
    webhook = await msg.channel.create_webhook(name=f"{msg.author.display_name}'s Webhook")
    await webhook.send(msg.content, username=msg.author.display_name, avatar_url=str(msg.author.avatar))
    await webhook.delete()

bot.run("")  
