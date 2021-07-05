from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands
import datetime


class Main(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(title="Test Embed Messages",
                              description="I'm watching you~~~", color=0x00e1ff, timestamp=datetime.datetime.now())
        embed.set_author(name="Albert Huang", url="https://albert-notes.github.io/",
                         icon_url="https://i.imgur.com/NDHNTFs.png")
        embed.set_thumbnail(url="https://i.imgur.com/NDHNTFs.png")
        embed.add_field(name="Kevin", value="Black", inline=True)
        embed.add_field(name="Vic", value="Hello", inline=True)
        embed.add_field(name="Mochi", value="Friend", inline=True)
        embed.set_footer(text="This is a test message.")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(Main(bot))
