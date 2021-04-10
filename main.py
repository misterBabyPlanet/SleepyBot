import json
import time
from Classes import Shop, Bot


# token recuperation
def TOKEN_recuperation():
    with open("TOKEN.txt", "r") as token_file:  # open TOKEN file
        return token_file.read()  # return TOKEN


# get objects
def getJSon():
    with open('objects.json', 'r') as JSON_file:
        return json.load(JSON_file)


Shop = Shop.ShopObject(getJSon())  # shop creation
client = Bot.MyBot()  # Bot Object

while True:
    client.run(TOKEN_recuperation())  # run Bot
    time.sleep(0.01)  # client rerun
