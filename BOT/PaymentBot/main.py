import discord
import requests
import random
import psutil
import time
import asyncio
import uvicorn
import logging
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from payos import PayOS, PaymentData

TOKEN = "YOUR_BOT_TOKEN"
AUTHORIZED_ROLE = [1195351303182889031, 1204404049210769418, 1280481283713273969, 894579088843485244]  
BANK_ID = "970418"
ACCOUNT_NO = "8893816596"
TEMPLATE = "qr_only"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
start_time = time.time()

def VndFormat(amount: int) -> str:
    return f"{amount:,}vnđ".replace(",", ".")

def Vnd2Text(amount: int) -> str:
    response = requests.get(f"http://forum.vdevs.net/nossl/mtw.php?number={amount}")
    if response.status_code == 200:
        return response.json().get("result", "Không thể chuyển đổi")
    return "Không thể kết nối"

async def IsGuild(interaction: discord.Interaction) -> bool:
    if interaction.guild is None or interaction.guild.id != bot.guild_id:
        await interaction.response.send_message("❌ Lệnh này chỉ có thể sử dụng trong server đúng!", ephemeral=True)
        return False
    return True

class DataBase:
    def __init__(self, bot):
        uri = "mongodb+srv://khad24124zvcl:khaawduiahwdkhadzhaha@stel24124la.kpwmr.mongodb.net/?retryWrites=true&w=majority&appName=Stella"
        self.client = AsyncMongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["coal"]
        self.users = self.db["users"]
        self.giftcodes = self.db["giftcodes"]
        self.bot = bot
        self.bot.logger.info("Database connected")
    
    async def has_user(self, user_id: int):
        user = await self.users.find_one({"_id": user_id})
        return user is not None
    
    async def add_user(self, user_id: int):
        await self.users.insert_one({"_id": user_id, "coin": 0})
        await self.giftcodes.insert_one({"_id": user_id, "codes": []})
    
    async def get_value(self, user_id: int, key: str, table = "users"):
        table = self.users if table == "users" else self.giftcodes
        user = await table.find_one({"_id": user_id})
        return user[key]
    
    async def set_value(self, user_id: int, key: str, value: int, table = "users"):
        table = self.users if table == "users" else self.giftcodes
        await table.update_one({"_id": user_id}, {"$set": {key: value}})

class PaymentBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", help_command=None, intents=discord.Intents.all())
        self.start_time = datetime.now()
        self.logger = logging.getLogger("discord.client")
        self.guild_id = 894469438009651230
        self.log_channel_id = 1214596264617050173
        self.payos = PayOS(
            client_id="fdfa1a7f-23d6e264750",
            api_key="f180600b-f321-45a-ecb2ea5dfbeb",
            checksum_key="c8bc91d4e817cd6c652f014a67100b"
        )

class PaymentView(View):
    def __init__(self, price: int, amount: int, target_user: discord.User):
        super().__init__()
        self.price = price
        self.amount = amount
        self.target_user = target_user
        self.timeout = 3600  

    async def create_payment(self, bot: commands.Bot, interaction: discord.Interaction):
        expired_at = (datetime.now() + timedelta(hours=3)).strftime("%H:%M:%S")
        text_amount = Vnd2Text(self.price)
        payment_data = PaymentData(
            orderCode=random.randint(1000, 999999),
            amount=self.price,
            expiredAt=int((datetime.now() + timedelta(hours=3)).timestamp()),
            description=f"{self.target_user.id} {self.amount}",
            returnUrl="https://stellamc.net/",
            cancelUrl="https://stellamc.net/"
        )
        payment = bot.payos.createPaymentLink(payment_data)
        embed = discord.Embed(
            title="🔮 Yêu cầu thanh toán",
            description=(
                f"**Người thanh toán:** {self.target_user.mention}\n"
                f"**Thành tiền:** {Vnd2Text(self.amount)} VND\n"
                f"**Thành chữ:** {text_amount}\n\n"
                f"#Vui lòng thanh toán trước {expired_at}"
            ),
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow()
        )
        qr_url = QrGen(self.amount, f"Thanh toán {self.target_user.id} {self.amount}", self.accountname)
        embed.set_image(url=qr_url)
        self.add_item(Button(label="Click to Pay", url=payment.checkoutUrl, style=discord.ButtonStyle.link))
        await interaction.followup.send(embed=embed, view=self)
        await bot.log(
            "Payment Request Created",
            f"Requester: {interaction.user.name}\nRecipient: {self.target_user.name}\nAmount: {self.amount:,} credits",
            interaction.user
        )

class BotCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="payment")
    @app_commands.describe(amount="Amount in VND", user="User to receive the credits")
    async def payment(self, interaction: discord.Interaction, amount: int, user: discord.User):
        if not await IsGuild(interaction):
            return
        if AUTHORIZED_ROLE not in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message("❌ Bạn không có quyền sử dụng lệnh này!", ephemeral=True)
            return
        if amount < 2000:
            await interaction.response.send_message("Minimum amount is 2,000 VND", ephemeral=True)
            return
        
        view = PaymentView(amount, amount, user)
        await view.create_payment(self.bot, interaction)

    @app_commands.command(name="status")
    async def status(self, interaction: discord.Interaction):
        if not await IsGuild(interaction):
            return
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        uptime = datetime.now() - self.bot.start_time
        embed = discord.Embed(
            title="📊 Bot Status",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow()
        )
        embed.add_field(
            name="System",
            value=(
                f"📡 **Ping:** `{round(self.bot.latency * 1000, 1)}ms`\n"
                f"⚡ **CPU:** `{cpu_usage}%`\n"
                f"💾 **RAM:** `{ram.used // (1024 * 1024):,} MB / {ram.total // (1024 * 1024):,} MB ({ram.percent}%)`"
            ),
            inline=False
        )
        embed.add_field(name="Runtime", value=f"🕒 **Uptime:** `{str(uptime).split('.')[0]}`", inline=False)
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_payos(self, data: dict):
        if data["success"] and data["desc"] == "success":
            payment_data = data["data"]["description"].split()
            user_id = int(payment_data[0])
            user = await self.bot.fetch_user(user_id)
            embed = discord.Embed(
                title="✅ Payment Successful",
                description=(
                    f"**Người thụ hưởng:** {user.mention}\n"
                    f"**Số tiền đã thanh toán:** {data['data']['amount']:,} VND\n"
                ),
                color=discord.Color.green(),
                timestamp=discord.utils.utcnow()
            )
            await user.send(embed=embed)
            await self.bot.get_channel(123456789012345678).send(embed=embed)  

@asynccontextmanager
async def lifespan(app: FastAPI):
    bot.logger.info("Starting application...")
    asyncio.create_task(bot.start(TOKEN))
    yield
    bot.logger.info("Shutting down...")
    await bot.close()

app = FastAPI(title="Stella | Callback", lifespan=lifespan)
bot = PaymentBot()

@app.post("/api/payos")
async def payos_callback(request: Request):
    data = await request.json()
    bot.dispatch("payos", data)
    return {"success": True}

if __name__ == "__main__":
    async def setup():
        await bot.add_cog(BotCommands(bot))
    
    asyncio.run(setup())
    uvicorn.run(app, host="0.0.0.0", port=8000)
