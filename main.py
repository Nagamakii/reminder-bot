from discord.ext import commands
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

bot = commands.Bot(command_prefix='!', description="This is a bot to remind me of things")
token = os.getenv("TOKEN")
db_token = os.getenv("DB_PASS")

conn = None
# read connection parameters
print('Connecting to the PostgreSQL database...')
conn = psycopg2.connect(user="db_user",
                          password=db_token,
                          host="192.168.4.59",
                          port="5433",
                          database="postgres")
cur = conn.cursor()
        
@bot.event
async def on_ready():
    print("Bot is online!")

@bot.command()
async def remindme(ctx, arg):
    await ctx.send(f"I will remind you to {arg} when you get home!")
    insert = (cur.execute(f""" INSERT INTO COMMANDS (ID, CONTENT) VALUES (1, '{arg}') """))
    conn.commit()

@bot.command()
async def home(ctx):
    try:
        select = (cur.execute(""" SELECT content FROM commands"""))
        await ctx.send(f"Welcome home {ctx.author.mention}! Don't forget to {select}")
        conn.commit()
    finally:
        rm = (cur.execute(""" TRUNCATE commands """))
        (rm)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    bot.run(token)