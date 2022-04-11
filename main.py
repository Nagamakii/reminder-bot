import asyncio
from urllib import response
from urllib.request import urlopen
from aiohttp import request
from discord.ext import commands
from dotenv import load_dotenv
import os
import psycopg2
import websockets

load_dotenv()


bot = commands.Bot(command_prefix='!', description="This is a test bot")
token = os.getenv("TOKEN")



# Command that parses the reminders
@bot.command()
async def remindme(ctx, arg):
    await ctx.send(f"I will remind you to {arg} when you get home!")
    global x
    x = arg

print('running websockets ws://192.168.4.21:8000')
server = websockets.serve(response, '192.168.4.21', '8000')
asyncio.get_event_loop().run_until_complete(server)

if __name__ == '__main__':
    bot.run(token)