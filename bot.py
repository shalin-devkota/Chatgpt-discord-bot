import discord 
from discord.ext import commands
import os
from gpthandler import get_response
intents = discord.Intents.default()
intents.message_content= True
client = commands.Bot(command_prefix="/",case_insensitive=True,intents=intents)
client.remove_command("help")

@client.command()
async def gpt(ctx,*, message):
        print(message)
        try:
            reply =  get_response(message)
            embed=discord.Embed(colour=discord.Colour.green(),description=reply)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Some error occured")



client.run('TOKEN HERE')

