import discord
from discord.ext import commands
intents = discord.Intents.all()
from secret import TOKEN
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command()
async def hello(ctx:commands.Context):
    user = ctx.author
    await ctx.send(f'Olá {user.display_name}')

@bot.command()
async def sum(ctx:commands.Context, num1:int, num2:int):
    res = num1 + num2
    await ctx.reply(f'A soma de {num1} + {num2} = {res}')

@bot.command()
async def speak(ctx:commands.Context, *,text): # *, para ser um texto inteiro
    await ctx.send(text)

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(TOKEN)