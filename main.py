import discord
from discord.ext import commands
intents = discord.Intents.all()
from secret import TOKEN
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command()
async def button(ctx:commands.Context):

    async def button_response(interact:discord.Interaction):
        await interact.response.send_message('Button Pressed')

    view = discord.ui.View()
    button = discord.ui.Button(label='Button', style=discord.ButtonStyle.success)
    button.callback = button_response

    buttonURL = discord.ui.Button(label='Click me please', url="https://www.youtube.com/watch?v=dQw4w9WgXcQ1")

    view.add_item(button)
    view.add_item(buttonURL)
    await ctx.reply(view=view)

@bot.command()
async def favoriteGame(ctx:commands.Context):

    async def select_response(interaction:discord.Interaction):
        choosed = interaction.data['values'][0]
        games = {
            '1':'Minecraft',
            '2':'GTA V',
            '3':'League of Legends'
        }
        game_choosed = games[choosed]
        await interaction.response.send_message(f'O teu jogo favorito é {game_choosed}')
    
    selectMenu = discord.ui.Select(placeholder="Choose a option")
    options = [
        discord.SelectOption(label='Minecraft', value='1'),
        discord.SelectOption(label='GTA V', value='2'),
        discord.SelectOption(label='League of Legends', value='3') 
    ]
    selectMenu.options = options
    selectMenu.callback = select_response
    view = discord.ui.View()
    view.add_item(selectMenu)
    await ctx.reply(view=view)

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(TOKEN)