import requests
import asyncio
from discord.ext import commands
from discord.ext.commands.core import command

class Stuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(brief="Insults the specified person")
    async def insult(self, ctx, *, person):
        insult = requests.get("https://insult.mattbas.org/api/insult")
        insult = insult.text.replace("Y", "y")
        async with ctx.channel.typing():
            await asyncio.sleep(3)
        await ctx.channel.send(f"{person}, {insult}")

    @commands.command(brief="Get a random dad joke")
    async def joke(self, ctx):
        joke = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()['joke']
        async with ctx.channel.typing():
            await asyncio.sleep(2)
        await ctx.channel.send(f"{joke}")

    @commands.command(brief="Give a word to get the definition")
    async def define(self, ctx, word):
        reply = ""
        definition = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en_GB/{word}").json()
        try:
            for i in definition[0]["meanings"]:
                reply += f"\r\n**{i['partOfSpeech']}**: "
                for j in i['definitions']:
                    reply += f"\r\n{j['definition']}\r\n"  
                    try:
                        reply += f"> {j['example']}\r\n"
                    except:
                        pass
        except:
            reply = f'{definition["message"]}'
        
        async with ctx.channel.typing():
            asyncio.sleep(2)
        await ctx.channel.send(reply)

def setup(client):
    client.add_cog(Stuff(client))
