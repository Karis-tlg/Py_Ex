import discord
import asyncio
import threading

EXCEPTION_CHANNELS = {"1276210386584080425"}

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

async def save_channels():
    guild = client.get_guild(1276210386584080424)
    
    if guild is None:
        print('Không tìm thấy server với ID đó.')
        return
    
    with open('channels.txt', 'w', encoding='utf-8') as file:
        for category in sorted(guild.categories, key=lambda c: c.position):
            if str(category.id) in EXCEPTION_CHANNELS:
                continue
            file.write(f'- {category.name}:\n')
            for channel in sorted((channel for channel in category.channels if str(channel.id) not in EXCEPTION_CHANNELS), key=lambda c: c.name):
                file.write(f'  #{channel.name}\n')
    
    print('Đã ghi tất cả tên kênh vào file channels.txt')

def console_input():
    while True:
        command = input()  
        if command.strip().lower() == 'save':
            asyncio.run_coroutine_threadsafe(save_channels(), client.loop)

@client.event
async def on_ready():
    print(f'Đã đăng nhập với tài khoản: {client.user.name}')

    threading.Thread(target=console_input, daemon=True).start()

client.run("MTIxNDEyMTkzMjAxOTA3MzA1NQ.GrUMQB.xesQ8IDFClX5nyO8ldOe3no855NAyzaIlsghoQ")
