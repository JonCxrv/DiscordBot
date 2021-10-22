import discord
from discord.ext import commands, tasks
import os
import datetime

intents = discord.Intents.default()
intents.members = True

testing = False

bot = commands.Bot('>',  intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} ta pronto!')
    current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user :
        return
    if 'palavrao' in message.content:
        await message.channel.send(
            f"{message.author.name}, meu fiiii não fale coisa feia fiDumaÉgua!"
            )
        await message.delete()
        
    if 'herbert' in message.content:
        await message.channel.send(
            f"{message.author.name}, meu fiiii o nome dele é uéebit, Quando estiver com raiva dele apenas fale 'daqui a 5 anos da bom pro Jon em rs'"
            )

    await bot.process_commands(message)    


@bot.command(name='oi' or 'Oi')
async def send_hello(ctx):
    name = ctx.author.name

    response = 'Qual a boa ' + name + ' ?'

    await ctx.send(response) 


@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime('%d/%m/%Y ás %H:%M:%S')

    channel = bot.get_channel(804762511521742859)

    await channel.send ('Data Atual: ' + now )


bot.run('ODk5Mjg4MDg2ODk3MzgxNDA2.YWwlSw.fOk1hJyzxWbszK41nTJbbu_cktA')