import json
import os
import time

import discord  # discord package
from dotenv import load_dotenv  # environment variables

from Classes import Shop, Bot

load_dotenv()


class MyBot(discord.Client):
    """ Discord Bot entity """

    # launch bot
    async def on_ready(self):
        pass

    # bot comportment on receiving messages
    async def on_message(self, message):
        pass


# get objects
def getJSon():
    with open('objects.json', 'r') as JSON_file:
        return json.load(JSON_file)


Shop = Shop.ShopObject(getJSon())  # shop creation
client = Bot.MyBot()  # Bot Object

while True:
    client.run(os.getenv('DISCORD_TOKEN'))  # run Bot
    time.sleep(0.01)  # client rerun
