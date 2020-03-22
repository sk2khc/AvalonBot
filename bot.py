import discord
from discord.ext import commands
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(">>Avalon is Online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(691389870974697522)
    await channel.send(f'{member} Hello!')

@bot.event
async def on_member_remove(member):
    print(f'{member} has been removed!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('NjkxMzgxNjcxNDI1MjEyNDU2.XnfJdw.uWkIFr4rxwWFfFQOjIXkfZpONnw')