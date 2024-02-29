from discord import Intents,Interaction, ButtonStyle, ui
from discord.ext import commands
intents = Intents.all()
from secret import TOKEN
bot = commands.Bot(command_prefix=".", intents=intents)


@bot.command()
async def button(ctx:commands.Context):

    async def button_response(interact:Interaction):
        await interact.response.send_message('Button Pressed')


    view = ui.View()
    button = ui.Button(label='Button', style=ButtonStyle.success)
    button.callback = button_response

    view.add_item(button)
    await ctx.reply(view=view)

@bot.event
async def on_ready():
    print("Bot Online")

bot.run(TOKEN)