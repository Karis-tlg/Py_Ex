import discord
from discord.ext import commands
from discord import app_commands
from cogs.commands.owner import Owner

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

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
    await tree.sync()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.add_cog(Owner(bot))
bot.run('MTI3NTQ2NjY5NTE4MzU2NDkyMQ.GU6joP.YyB8vLM75_bjlRroSXf6HpWb7cE1SCjqSqDnVM')
