import os
from dotenv import load_dotenv
import discord
from discord.ext import commands



load_dotenv()
intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """A response"""
        await ctx.send("no bruv, don't even try.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('?hello'):
            await message.channel.send('Hello!')


client.add_cog(MyCog(client))

		

client.run(os.environ['TOKEN'])