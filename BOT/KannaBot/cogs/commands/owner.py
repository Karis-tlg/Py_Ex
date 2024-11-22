import discord
from discord import Embed
from discord import app_commands
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    def owner_only(interaction: discord.Interaction) -> bool:
        return interaction.user.id in (807947010861826058,)

    @app_commands.command(name="say", description="The bot will say anything you want.")
    @app_commands.check(owner_only)
    async def say(self, interaction: discord.Interaction, *, message: str) -> None:
        embed = Embed(description=message)
        await interaction.response.send_message(embed=embed)
