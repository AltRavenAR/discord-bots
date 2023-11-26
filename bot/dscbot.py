from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord.ext import commands



intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command
async def ping(self, ctx):
    """A response"""
    await ctx.send("no bruv, don't even try.")
	

@client.command
async def on_message(self, message):
    if message.author == self.bot.user:
        return
    if message.content.startswith('?hello'):
       await message.channel.send('Hello!')
	   

client.run(os.environ['TOKEN'])