import discord  # discord package

class shopOjet:
    """ Shop object"""

    def __init__(self, name, price, owner):
        self.price = price,
        self.name = name,
        self.owner = owner

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.price = new_price

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_owner(self):
        return self.owner

    def set_owner(self, new_owner):
        self.owner = new_owner



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
            commandes_dico = {
                "S!Help": "-> Si vous savez pas quoi faire :)",
                "S!Commandes": "-> Pour visualiser toutes les commandes disponibles",
                "S!Shop": "-> En construction"
            }
            commands_string = ""  # final string

            # list creation
            for command, text in commandes_dico.items():
                commands_string += f"-{command} {text}\n"

            await message.channel.send(f"Liste des commandes :\n\n{commands_string}")  # message

        # Shop command response
        async def Shop():
            await message.channel.send("En construction :)")

        # commands and correspond defs
        classic_messages_type_dico = {
            "S!Help": Help,
            "S!Commandes": Commandes,
            "S!Shop": Shop
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
