import discord
from discord.ext import commands
from datetime import datetime  
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

@bot.command(name="say", help="Tạo embed thông báo Payment Success và hiển thị user ID")
async def say(ctx: commands.Context, user: discord.Member):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    embed = discord.Embed(
        title="Payment Success",
        description=f"Type: Payment Success <@{user.id}>",
        color=discord.Color.green()
    )
    embed.add_field(name="User ID", value=f"{user.id}", inline=False)
    embed.add_field(name="Time", value=current_time, inline=False)
    embed.set_footer(text="Transaction Log")
    
    await ctx.send(embed=embed)

bot.add_cog(Owner(bot))
bot.run('MTI3NTQ2NjY5NTE4MzU2NDkyMQ.GLEbVq.Jfv_B-VX5c1s0gHV5KG6eFf_A69NCr8DFZgBlQ')
