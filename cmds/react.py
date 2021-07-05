from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands
import random
import json

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class React(Cog_Extension):
    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(self.bot.user.avatar_url)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(data['pics'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)


def setup(bot):
    bot.add_cog(React(bot))
