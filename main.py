import discord
from discord.ext import commands
intents = discord.Intents.all()
from secret import TOKEN
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(TOKEN)