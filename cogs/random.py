from discord.ext import commands
import asyncio
import random

class Random(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(brief='Sends happy matt or unhappy matt, randomly chosen')
    async def emoji(self, ctx):
        options = ["downmatt", "happymatt"]
        emote = random.choice(options)
        async with ctx.channel.typing():
            await asyncio.sleep(1)
        emoji = [x for x in ctx.guild.emojis if x.name == emote]
        await ctx.channel.send(f"<:{emoji[0].name}:{emoji[0].id}>")
    
    @commands.command(brief='Roll some die, eg 2d12')
    async def roll(self, ctx, roll: str):
        num = int(roll.split('d')[0])
        dice = int(roll.split('d')[-1])
        results = [random.randint(1,dice) for i in range(num)]
        total = sum(results)
        async with ctx.channel.typing():
            await asyncio.sleep(1)
        await ctx.channel.send(f"You rolled: {results} for a total of **{total}**")

    @commands.command(brief='choose random item from a space separated list')
    async def random(self, ctx, *, input: str):
        options = input.split(" ")
        async with ctx.channel.typing():
            await asyncio.sleep(1)
        await ctx.channel.send(f"{random.choice(options)}")

def setup(client):
    client.add_cog(Random(client))