from discord.ext import commands
from dotenv import load_dotenv
import os
from threading import Timer

load_dotenv()

bot = commands.Bot(command_prefix='!', description="This is a test bot")
token = os.getenv("TOKEN") 

@bot.command(name="remindme")
async def reminder(ctx, arg):
    await ctx.send(f"Gotcha! I will send you a reminder to {arg} when you get home.")
    global x
    x = arg

@bot.command(name="home")
async def user_home(ctx):
    await ctx.send(f"Remember to {x}!")


if __name__ == '__main__':
    bot.run(token)