import subprocess
from discord.ext import commands
from dotenv import load_dotenv
import os
from threading import Timer

load_dotenv()

bot = commands.Bot(command_prefix='!', description="This is a test bot")
token = os.getenv("TOKEN") 

def check_mac():
    cmd = subprocess.run('nmap -sn 192.168.4.0/24 | findstr "64:A2:F9:EB:FA:49"', shell=True)
    return cmd.returncode

@bot.command(name="remindme")
async def test(ctx, arg):
    await ctx.send(f"Gotcha!, I will send you a reminder to {arg} when you get home.")
   

if __name__ == '__main__':
    bot.run(token)