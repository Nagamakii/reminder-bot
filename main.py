from discord import Webhook, RequestsWebhookAdapter
from flask import Flask, request, abort
from discord.ext import commands
from dotenv import load_dotenv
import os
import threading

load_dotenv()
app = Flask(__name__)

bot = commands.Bot(command_prefix='!', description="This is a bot to remind me of things")
wh = os.getenv('WEBHOOK')
token = os.getenv("TOKEN")
db_token = os.getenv("DB_PASS")

@bot.event
async def on_ready():
    print("Bot is online!")

reminders = []
@bot.command()
async def remindme(ctx, arg):
    await ctx.send(f"I will remind you to {arg} when you get home!")
    reminders.append(arg)

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.method)
    if request.method == 'POST':
        print(request.json)
        formatted_list = (', '.join(reminders))
        Webhook.from_url(wh, adapter=RequestsWebhookAdapter()).send(f"Remember to {formatted_list} <@383762688355991554>!", username='Reminder-bot')
        return 'Home!', 200
    else:
        abort(400)    

threading.Thread(target=lambda: app.run(host="0.0.0.0")).start()

if __name__ == '__main__':
    bot.run(token)