import discord
from discord.ext import commands 
from rich import * 

console = Console()

intents = discord.Intents.default()
intents.message_content = True
bot = command.Bot(command_prefix='>', intents=intents)

@bot.command(CreationCall)
async def cCall_publica(guild):
    