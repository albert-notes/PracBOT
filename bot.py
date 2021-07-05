import discord
from discord import channel
from discord.ext import commands
import json
import random
import os

bot = commands.Bot(command_prefix='=')

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


@bot.event
async def on_ready():
    print("{0} is online now!".format(bot.user))
    channel = bot.get_channel(int(data['channel']))
    await channel.send('Thank you for adding me! I\'m {0}! :heart:\n`-`I\'m online now! ✅\n`-`**My prefix is `=`**\n`-`**Please use `=h` to see my options.** :arrow_forward:\nAuthor : <@679666429041442836>\nAuthor\'s website : **<https://albert-notes.github.io>**'.format(bot.user.mention))


@bot.command()
async def h(ctx):
    await ctx.send('Help!')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} loaded!')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} unloaded!')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} reloaded!')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(data['token'])
