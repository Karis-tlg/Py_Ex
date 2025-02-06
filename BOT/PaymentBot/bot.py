import discord
import requests
import random
import psutil
import pytz
import asyncio
import uvicorn
import logging
import subprocess
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from payos import PayOS, PaymentData

VipRole = [1195351303182889031, 1204404049210769418, 1280481283713273969, 894579088843485244]
start_time = datetime.now()

def vndformat(amount: int) -> str:
    return f"{amount:,}vnđ".replace(",", ".")

def vnd2text(amount: int) -> str:
    response = requests.get(f"http://forum.vdevs.net/nossl/mtw.php?number={amount}")
    return response.json().get("result", "Không thể chuyển đổi") if response.status_code == 200 else "Không thể kết nối"

async def hasperm(interaction: discord.Interaction) -> bool:
    if not interaction.guild or interaction.guild.id != bot.guild_id:
        await interaction.response.send_message(embed = discord.Embed(title="❌ Lệnh này chỉ có thể sử dụng trong server Stella Studio", color=discord.Color.red(), timestamp=discord.utils.utcnow()), ephemeral=True)
        return False
    if not any(role.id in VipRole for role in interaction.user.roles):
        await interaction.response.send_message(embed = discord.Embed(title="❌ Bạn không có quyền sử dụng lệnh này!", color=discord.Color.red(), timestamp=discord.utils.utcnow()), ephemeral=True)
        return False
    return True

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.on_start_time = datetime.now()
        self.logger = logging.getLogger("discord.client")
        self.guild_id = 894469438009651230
        self.log_channel = 1214596264617050173
        self.db = DataBase(self)
        self.payos = PayOS(client_id="CLIENT_ID", api_key="YOUR_KEY", checksum_key="MAIN_KEY")

    async def setup_hook(self):
        await self.add_cog(BotCommands(self))
        await self.tree.sync()
    
    async def on_ready(self):
        self.logger.info(f"Bot logged in as {self.user}")
        self.guild = self.get_guild(self.guild_id)

    async def log(self, title: str, message: str, user: discord.User = None) -> None:
        channel = self.get_channel(self.log_channel)
        embed = discord.Embed(title=title, description=message, color=discord.Color.dark_gray())
        embed.timestamp = discord.utils.utcnow()
        if user is not None:
            embed.set_author(name=user.name, icon_url=user.display_avatar.url)
        await channel.send(embed=embed)

class DataBase:
    def __init__(self, bot):
        self.client = AsyncMongoClient("YOUR_LINK_MONGO", server_api=ServerApi('1'))
        self.db = self.client["stella"]
        self.payments = self.db["payments"]
        self.bot = bot
        self.bot.logger.info("Database connected")

    async def save(self, user_id: int, amount: int):
        await self.payments.insert_one({"user_id": user_id, "amount": amount, "timestamp": datetime.now()})
    
    async def gettop(self, limit: int = 10):
        pipeline = [
            {"$group": {"_id": "$user_id", "total_amount": {"$sum": "$amount"}}},
            {"$sort": {"total_amount": -1}},
            {"$limit": limit}]
        cursor = await self.payments.aggregate(pipeline) 
        return [entry async for entry in cursor] 

class PayOSCallback(View):
    def __init__(self, inuser, user: discord.User, amount: int, bot: commands.Bot, channel: discord.TextChannel):
        super().__init__()
        self.amount = amount
        self.inuser = inuser
        self.user = user
        self.bot = bot
        self.channel = channel.id

    async def send_payment(self, interaction: discord.Interaction) -> str:
        await interaction.response.defer()
        pay = self.bot.payos.createPaymentLink(PaymentData(
            orderCode=random.randint(1000, 999999),
            amount=self.amount,
            expiredAt=int((datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + timedelta(hours=3)).timestamp()),
            description=requests.post("https://api.pastes.dev/post", data=f"{self.inuser} {self.user.id} {self.channel}".encode("utf-8"), headers={"Content-Type": f"text/plain", "User-Agent": "MyPythonClient/1.0"}).json().get("key"),
            returnUrl="https://stellamc.net/",
            cancelUrl="https://stellamc.net/"))
        embed = discord.Embed(
            title="🔮 Yêu cầu thanh toán",
            description=(
                f"**Người thanh toán:** {self.user.mention}\n"
                f"**Thành tiền:** {vndformat(self.amount)}\n"
                f"**Thành chữ:** {vnd2text(self.amount)}\n\n"
                f"**Vui lòng thanh toán trước {(datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')) + timedelta(hours=3)).strftime('%H:%M:%S')}**"),
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow())
        embed.set_image(url=f"https://quickchart.io/qr?text={pay.qrCode}&margin=1&size=450")
        self.add_item(Button(label="Click to Pay", url=pay.checkoutUrl, style=discord.ButtonStyle.link))
        await interaction.followup.send(embed=embed, view=self)

class BotCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="payment", description="Định dạng <user> <số tiền>")
    @app_commands.describe(user="Vui lòng chọn khách hàng", amount="Định dạng tiền VNĐ")
    async def payment(self, interaction: discord.Interaction, user: discord.User, amount: int):
        if not await hasperm(interaction):
            return
        if amount < 2000:
            await interaction.response.send_message(embed = discord.Embed(title="❌ Số tiền tối thiểu là 2,000 VND"), color=discord.Color.red(), timestamp=discord.utils.utcnow())
            return False
        payment = PayOSCallback(interaction.user.id, user, amount, self.bot, interaction.channel)
        await payment.send_payment(interaction)

    @app_commands.command(name="status", description="Show status of the bot")
    async def status(self, interaction: discord.Interaction):
        if not await hasperm(interaction):
            return
        ram = psutil.virtual_memory()
        embed = discord.Embed(
            title="📊 Bot Status",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow())
        embed.add_field(
            name="System",
            value=(
                f"📡 **Ping:** `{round(self.bot.latency * 1000, 1)}ms`\n"
                f"⚡ **CPU:** `{psutil.cpu_percent(interval=1)}%`\n"
                f"💾 **RAM:** `{ram.used // (1024 * 1024):,} MB / {ram.total // (1024 * 1024):,} MB ({ram.percent}%)`"),
            inline=False)
        embed.add_field(name="Runtime", value=f"🕒 **Uptime:** `{str(datetime.now() - self.bot.on_start_time).split('.')[0]}`", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="leaderboard", description="Hiện thị top Customer")
    async def leaderboard(self, interaction: discord.Interaction):
        if not await hasperm(interaction):
            return
        await interaction.response.defer()
        top_users = await self.bot.db.gettop(limit=10)
        if not top_users:
            await interaction.response.send_message(embed=discord.Embed(title="❌ Không có người dùng nào có giao dịch thanh toán.", color=discord.Color.red(), timestamp=discord.utils.utcnow()))
            return
        ranks = ""
        for rank, entry in enumerate(top_users, start=1):
            user = await self.bot.fetch_user(entry["_id"])
            ranks += f"**#{rank} {user.name} - 💰 {vndformat(entry['total_amount'])}**\n"
        embed = discord.Embed(
            title="🏆 Leaderboard - Top Người Dùng Thanh Toán",
            description=ranks,
            color=discord.Color.gold(),
            timestamp=discord.utils.utcnow())
        await interaction.followup.send(embed=embed)

    @commands.Cog.listener()
    async def on_payos(self, data: dict) -> None:
        try:
            if data["success"] and data["desc"] == "success":
                payment_data = requests.get(f"https://api.pastes.dev/{data['data']['description']}", headers={"User-Agent": "MyPythonClient/1.0"}).text.split()
                inuser = await self.bot.fetch_user(int(payment_data[0]))
                user = await self.bot.fetch_user(int(payment_data[1]))
                guild = self.bot.get_guild(self.bot.guild_id)
                member = guild.get_member(user.id) if guild else None
                role = guild.get_role(894580615146508289) if guild else None
                await self.bot.db.save(int(payment_data[1]), data['data']['amount'])
                embed = discord.Embed(
                title="✅ Payment Successful",
                description=(
                    f"**Người thụ hưởng:** {inuser.mention}\n"
                    f"**Số tiền đã thanh toán:** {data['data']['amount']:,} VND\n"
                    f"**Thời gian thanh toán:** {datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime('%Y-%m-%d %H:%M')}\n"
                    f"**Thanh toán bởi:** {user.mention}"),
                color=discord.Color.green(),
                timestamp=discord.utils.utcnow())
                if member and role and role not in member.roles: 
                    await member.add_roles(role)
                    embed.description += f"\n\n✅ **Đã thêm role Customer cho {user.name}!**"
                await self.bot.get_channel(int(payment_data[2])).send(embed=embed)
                await self.bot.log(embed.title, embed.description)
            else: 
                await self.bot.log(embed=discord.Embed(title="❌ Có lỗi xảy ra", description=f"Mã lỗi {data}", color=discord.Color.red(), timestamp=discord.utils.utcnow()))
        except Exception as e:
            self.bot.logger.error(f"❌ Lỗi xử lý webhook: {e}")

async def start_ngrok():
    print("Đang khởi động Ngrok...")
    process = await asyncio.create_subprocess_exec(
        r"J:\Data\Tin\Py_Ex\BOT\PaymentBot\ngrok.exe", "http", "6216", "--log", "stdout",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    async for line in process.stdout:
        decoded_line = line.decode().strip()
        print(decoded_line)
        if "https://" in decoded_line and ".ngrok-free.app" in decoded_line:
            break

@asynccontextmanager
async def lifespan(app: FastAPI):
    bot.logger.info("Starting application...")
    await start_ngrok() 
    bot.logger.info("Ngrok ready. Starting bot...")
    asyncio.create_task(bot.start("BOT_TOKEN"))
    yield
    bot.logger.info("Shutting down...")
    await bot.close()
    
discord.utils.setup_logging(root=False)    
app = FastAPI(title="Stella | Callback", lifespan=lifespan)
bot = Bot("!", help_command=None, intents=discord.Intents.all())

@app.post("/api/payos")
async def payos_callback(request: Request):
    data = await request.json()
    bot.dispatch("payos", data)
    return {"success": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6216, loop="asyncio")
