import discord # discord package

class MyBot(discord.Client):
    """ Discord Bot entity """

    # launch bot
    async def onReady(self):
        pass

    # bot comportment on receiving messages
    async def onMessage(self, message):
        pass

# token recuperation
def TOKEN_recuperation():
    with open("TOKEN.txt", "r") as token_file:      # open TOKEN file
        return token_file.read()                        # return TOKEN


client = MyBot()                        # Bot Object
client.run(TOKEN_recuperation())        # run Bot