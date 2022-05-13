# Reminderbot
This is a simple bot that logs things from a discord bot to remind me when I get home.

It stores the entries in a list, then when I get home, I scan an NFC tag and the flask webhook records it and sends me a list of the entries along with a ping.

Tried to get it running on docker, but it took too long and I couldn't figure out how to publish the port to access outside of localhost, so I ditched it and just run it in rc.local on my homelab.
