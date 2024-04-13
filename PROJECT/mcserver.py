import discord
import requests
from utils.bot import Bot, ClassicEmbed
from discord.ext import commands
from discord import app_commands

class MCStatus(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.checks.cooldown(1,5)
    @app_commands.command(name="mcstatus", description="View minecraft server status")
    @app_commands.describe(address="Minecraft server address",bedrock="Bedrock server?")
    async def mcserver(self, interaction: discord.Interaction, address:str, bedrock:bool = False):
        await interaction.response.defer()
        embed = ClassicEmbed()
        if address is None:
            embed.title="Please enter address."
        else:
            if not bedrock: url=f"https://api.mcsrvstat.us/3/{address}"
            else: url=f"https://api.mcsrvstat.us/bedrock/3/{address}"
            status = requests.get(url, timeout=300).json()
            ipi = requests.get(f"http://ip-api.com/json/{status['ip']}?fields=17667",timeout=300).json()
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")            
            if not bedrock:
                embed.set_image(url=f"http://status.mclive.eu/Server/{status['ip']}/{status['port']}/banner.png")
            desc = f"Online: {str(status['online']).capitalize()}"
            desc += f"\nIP: {status['ip']}"
            if "hostname" in status: desc += f"\nHost: {status["hostname"]}"
            desc += f"\nPort: {status['port']}"
            if ipi['status'] == "success":
                desc += f"\nCountry: {ipi['country']}"
                desc += f"\nOrganization: {ipi['org']}"
            if status["online"]:
                embed.set_author(name=address, icon_url="https://cdn3.emoji.gg/emojis/6292-goodconnection.png")
                if "protocol" in status:
                    if "name" in status["protocol"]:
                        desc += f"\nVersion: {status['protocol']['name']}({status['protocol']['version']})"
                    else:
                        desc += f"\nVersion: {status['protocol']['version']}"
                else: desc += f"\nVersion: {status['version']}"
                if "software" in status: desc += f"\nSoftware: {status['software']}"
                desc += f"\nPlayers: {status['players']['online']}/{status['players']['max']}"
                desc += f"\nMotd:\n" + '`' + "\n".join(status["motd"]["clean"]) + "`"
            else: embed.set_author(name=address, icon_url="https://cdn3.emoji.gg/emojis/8031-lowconnection.png")
            embed.description = desc
        await interaction.followup.send(embed=embed)
async def setup(bot: Bot):
    await bot.add_cog(MCStatus(bot))