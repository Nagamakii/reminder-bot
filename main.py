# TODO: Figure out how to send reminders from the same bot and deploy all of this in a docker container

from discord import Webhook, RequestsWebhookAdapter
from flask import Flask, request, abort
from discord.ext import commands
from dotenv import load_dotenv
import threading
import os

load_dotenv()
app = Flask(__name__)

# Start bot and get env variables, command prefix is the char before the message
bot = commands.Bot(command_prefix='!', description="This is a bot to remind me of things when I get home")
wh = os.getenv('WEBHOOK')
token = os.getenv("TOKEN")

# msg for bot online
@bot.event
async def on_ready():
    print("Bot is online!")

# When command "!remindme *" is run it will send me a confirmation in the server and add it to the list
reminders = []
@bot.command()
async def remindme(ctx, arg):
    await ctx.send(f"I will remind you to {arg} when you get home!")
    print(f"New reminder!: {arg}")
    reminders.append(arg)

# Start the flask webhook, when the POST request comes in it formats the list, then sends it in a webhook, prob need to figure out how to send it from the same bot lol
@app.route('/', methods=['POST'])
def webhook():
    print(request.method)
    if request.method == 'POST':
        try:
            print(request.json)
            formatted_list = (', '.join(reminders))
            Webhook.from_url(wh, adapter=RequestsWebhookAdapter()).send(f"Remember to {formatted_list} <@383762688355991554>!", username='Reminder-bot')
            return 'Home!', 200
        # Clear the list after the message is sent
        finally:
            reminders.clear()
    # Abort the request if it's not POST
    else:
        abort(400)


# Run the webhook server in a seperate thread so not to conflict with the discord bot
if __name__ == '__main__':
    threading.Thread(target=lambda: app.run("0.0.0.0")).start()
    bot.run(token)