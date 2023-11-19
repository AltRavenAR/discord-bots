import discord

from discord.ext import commands
client = commands.Bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
	print('we have logged in as {0.user}'.format(client))


@commands.command()
async def ping(ctx):
    """A response"""
    await ctx.send("no bruv, don't even try.")

@commands.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@client.event
async def on_message(message):
	if message.author==client.user:
		return
	if message.content.startswith('?hello'):
		await message.channel.send('Hello!')
		

client.run(TOKEN)