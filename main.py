import disnake
from disnake.ext import commands
from model import get_class
import os, random
import requests

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=disnake.Intents.default(), help_command=None, test_guilds=[1161681641870213295])

token = "YOUR TOKEN HERE"

@bot.event
async def on_ready():
    print(f"You have just entered as {bot.user}")
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Streaming(name=f'twitch', url='https://www.twitch.tv/unknowpage')) # Статус бота (Для примера выбрал стриминг)

@bot.command()
async def ping(ctx):
    await ctx.send("ping")

@bot.slash_command(description="Простой калькулятор!")
async def calc(inter, a: float, oper: str, b: float):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    else:
        result = "Неверный оператор"

    await inter.send(str(result))
    

    
@bot.command(description="check")
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./photos/{attachment.filename}")
            #ttt = 'More info on: [norgbot.io](<https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley>)'
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path='labels.txt', image_path=f"./photos/{attachment.filename}"))
            #await ctx.send(ttt)
            
    else:
        await ctx.send('Вы забыли загрузить картинку!')
            
bot.run(token)
