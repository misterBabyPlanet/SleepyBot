import discord # discord package

class MyBot(discord.Client):
    """ Discord Bot entity """

    # launch bot
    async def on_ready(self):
        print(f"{self.user} launched\n")

    # bot comportment on receiving messages
    async def on_message(self, message):

        async def Help():
            await message.channel.send('Bot en construction.\nPlein de trucs cool à terme :)')

        async def Commandes():
            commandes_list = ["S!Help"]
            commands_string = ""

            for command in commandes_list:
                commands_string += f"-{command}\n"

            await message.channel.send(f"Liste des commandes :\n{commands_string}")

        classic_messages_type_dico = {
            "S!Help" : Help,
            "S!Commandes" : Commandes
        }

        if message.author == self.user:
            pass

        for key, value in classic_messages_type_dico.items():
            if message.content == key:
                await value()

# token recuperation
def TOKEN_recuperation():
    with open("TOKEN.txt", "r") as token_file:      # open TOKEN file
        return token_file.read()                        # return TOKEN


client = MyBot()                        # Bot Object
client.run(TOKEN_recuperation())        # run Bot