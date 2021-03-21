import discord  # discord package


class MyBot(discord.Client):
    """ Discord Bot entity """

    # launch bot
    async def on_ready(self):
        print(f"{self.user} launched\n")

    # bot comportment on receiving messages
    async def on_message(self, message):

        # Help command response
        async def Help():
            await message.channel.send('Bot en construction.\nPlein de trucs cool à terme :)')  # message

        # Commandes command response
        async def Commandes():
            commandes_list = ["S!Help"]  # commandes list
            commands_string = ""  # final string

            # list creation
            for command in commandes_list:
                commands_string += f"-{command}\n"

            await message.channel.send(f"Liste des commandes :\n\n{commands_string}")  # message

        # commands and correspond defs
        classic_messages_type_dico = {
            "S!Help": Help,
            "S!Commandes": Commandes
        }

        # if message authore is Sleepy bot
        if message.author == self.user:
            pass

        # recuperation of commands and Defs
        for key, value in classic_messages_type_dico.items():
            if message.content == key:  # if command in message
                await value()  # def


# token recuperation
def TOKEN_recuperation():
    with open("TOKEN.txt", "r") as token_file:  # open TOKEN file
        return token_file.read()  # return TOKEN


client = MyBot()  # Bot Object
client.run(TOKEN_recuperation())  # run Bot
