import discord

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
                "S!Shop": "-> En construction",
                "S!Version": "-> Version SleepyBot"
            }
            commands_string = ""  # final string

            # list creation
            for command, text in commandes_dico.items():
                commands_string += f"-{command} {text}\n"

            await message.channel.send(f"Liste des commandes :\n\n{commands_string}")  # message

        # Shop command response
        async def Shop():
            await message.channel.send("En construction :)")

        # Bot version info
        async def Version():
            await message.channel.send('Version actuelle : Dev 0.1 + quqes features possibles, bot en construction :)')  # message

        # commands and correspond defs
        classic_messages_type_dico = {
            "S!Help": Help,
            "S!Commandes": Commandes,
            "S!Shop": Shop,
            "S!Version": Version
        }

        # if message authore is Sleepy bot
        if message.author == self.user:
            pass

        # recuperation of commands and Defs
        for key, value in classic_messages_type_dico.items():
            if message.content == key:  # if command in message
                await value()  # def