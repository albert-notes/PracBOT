from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['kevin', 'black', 'Black', 'BlackKevin', 'KevinBlack']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('You are Right!')


def setup(bot):
    bot.add_cog(Event(bot))
