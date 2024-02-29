import discord
from discord.ext import commands
intents = discord.Intents.all()
from secret import TOKEN
bot = commands.Bot(command_prefix=".", intents=intents)

fun_stuff = False

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
    await ctx.reply(text)

@bot.command()
async def activateFunstuff(ctx:commands.Context):
    global fun_stuff
    fun_stuff = True
    embed = discord.Embed(
        description="✅ Funstuff Activated"
    )
    await ctx.reply(embed=embed)

@bot.event
async def on_guild_channel_create(channel:discord.abc.GuildChannel):
    print(fun_stuff)
    if fun_stuff:
        await channel.send("First!")
    else:
        return

@bot.event
async def on_member_join(member:discord.Member):
    welcome_channel = bot.get_channel(1212568753146171422) # ID do canal de boas vindas
    await welcome_channel.send(f'{member.display_name} Entrou no servidor, seja bem-vindo!')

@bot.event
async def on_member_remove(member:discord.Member):
    bye_channel = bot.get_channel(1212568753146171422) # ID do canal de saídas
    await bye_channel.send(f'{member.display_name} Saiu do servidor, iremos sentir a tua falta')

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(TOKEN)