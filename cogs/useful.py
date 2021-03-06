import discord
from discord.ext import commands, tasks
import random
import requests
import json
from Crypto.Util.number import long_to_bytes

class useful(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command(brief='Decode a number to bytes')
    async def lb(self, ctx, arg):
        try:
            await ctx.send(long_to_bytes(int(arg)).decode().replace("@",""))
        except:
            await ctx.send("Failed <:sex:736200562890113055>")
            
    
    @commands.command(brief='Gives a bot discord invite.')
    async def invite(self, ctx):
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=742802810843693089&permissions=8&scope=bot')

def setup(client):
    client.add_cog(useful(client))
