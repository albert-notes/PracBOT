from core.classes import Cog_Extension
import discord
from discord import channel
from discord.ext import commands, tasks
import datetime
import json
import asyncio

with open('settings.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class Task(Cog_Extension):
    # Official API
    """
    def __init__(self, bot):
        self.index = 0
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        self.channel = self.bot.get_channel(int(data['channel']))
        await self.channel.send(f'I\'ve been online for {self.index*5} seconds!')
        self.index += 1

    @printer.before_loop
    async def before_printer(self):
        print('waiting...')
        await self.bot.wait_until_ready()
    """
    # Proladon

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0
        """
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(data['channel']))
            while not self.bot.is_closed():
                await self.channel.send('Hi, I\'m running!')
                await asyncio.sleep(5)

        self.bg_task = self.bot.loop.create_task(interval())
        """

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(data['channel']))
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M')
                if data['time'] == now_time and self.counter == 0:
                    await self.channel.send(f'Current Time : {int(now_time)//100}:{int(now_time)%100}')
                    self.counter += 1
                    await asyncio.sleep(1)
                else:
                    pass
                    await asyncio.sleep(1)

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_ch(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel {self.channel.mention} successfully!')

    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        data['time'] = time
        with open('settings.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


def setup(bot):
    bot.add_cog(Task(bot))
