import discord
from discord.ext import commands
from secret import TOKEN

bot = commands.Bot(command_prefix="!")

bot.run(TOKEN)