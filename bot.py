from genericpath import exists
import random
import subprocess
import json
import discord
from discord.ext import commands


with open('config.json', 'r') as f:
    data = json.load(f)

if exists('config.local.json'):
    with open('config.local.json') as f:
        data = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

description = '''Bot to end all bots'''

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def sub(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def times(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def say(ctx, message):
    await ctx.send(message)

@bot.command()
async def cool(ctx):
    cool_factor = random.uniform(0, 100)
    await ctx.send(f'{ctx.author} is {cool_factor} cool!')

@bot.command()
async def update(ctx):
    subprocess.Popen('./update.sh')
    print(f'Updating, see you on the other side')

bot.run(data['token'])