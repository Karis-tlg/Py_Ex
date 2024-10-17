import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@tree.command(
    name="hello",
    description="Hello, world!",
    guild=discord.Object(id=1275475899818442866)  
)
async def first_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1275475899818442866)) 
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run('MTI3NTQ2NjY5NTE4MzU2NDkyMQ.GiuIzf.WRqjk1IiOGCQqA5ZEe9AJ5GGV2esHe-80efwvE')
