import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def load_cogs():
    await bot.load_extension('cogs.mtg')

@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))

async def main():
    async with bot:
        await load_cogs()
        await bot.start(token)

asyncio.run(main())