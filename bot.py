import discord
import random
from hangfish import Hangfish
from command import Command as cmd

AQUATIC_EMOJIS = ( "octopus", "squid", "shrimp", "lobster", "oyster", "crab", "blowfish", "tropical_fish", "fish", "dolphin", "whale", "whale2", "shark", )
AQUATIC_ANIMALS = ( "octopus", "squid", "shrimp", "lobster", "oyster", "crab", "blowfish", "fish", "dolphin", "whale", "shark", )

def strToEmoji(string):
    return ":"+string+":"

def randomAquatic():
    return strToEmoji(AQUATIC_EMOJIS[random.randint(0, len(AQUATIC_EMOJIS)-1)])

def aquaticAll():
    string = ""
    for animal in AQUATIC_EMOJIS:
            string += strToEmoji(animal)
    return string

class Bot(discord.Client):

    hangfish_instances = {}

    async def on_ready(self):
        print("We have logged in as {}".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
                return
        
        print ("{} sent {}".format(message.author, message.content))

        await cmd.call(message.channel, message.content)

#
# Define callbacks
#

    @staticmethod
    async def aquatic(channel, *args):
        # Options
        if len(args) > 0:
            if args[0] == "-a": 
                await channel.send(aquaticAll())
            else: 
                await channel.send("Unknown Argument: {}".format(args[0]))
        # Default option
        else:
            await channel.send(randomAquatic())

    @staticmethod
    def getHangfishInstance(channel):
        return Bot.hangfish_instances.get(channel.id, None)

    @staticmethod
    async def createHangfishInstance(channel):
        word = random.choice(AQUATIC_ANIMALS)

        message = None
        if Bot.getHangfishInstance(channel) is not None:
            message = "Hangfish instance already created. Creating new instance"
        else:
            message = "Creating Hangfish instance."
        Bot.hangfish_instances[channel.id] = Hangfish(word)
        await channel.send(message)
        await channel.send("```"+Bot.getHangfishInstance(channel).getString()+"```")

    @staticmethod
    async def updateHangfishInstance(channel, guess):
        instance = Bot.getHangfishInstance(channel)
        if instance is None:
            await channel.send("Hangfish instance not created.")
        instance.guess(guess)
        await channel.send("```"+instance.getString()+"```")
        if not instance.running:
            del Bot.hangfish_instances[channel.id]
            await channel.send("Game over.")

#
# Register callbacks
#

cmd.registerCallback("aquatic", Bot.aquatic)
cmd.registerCallback("hangfish", Bot.createHangfishInstance)
cmd.registerCallback("guess", Bot.updateHangfishInstance)

#
# Ensure token on first line, with no whitespaces at the end/beginning
#

try:
    token_file = open("token.txt", "r")
    token = token_file.readline()
    token_file.close()
    print("\'"+token+"\'")
    bot = Bot()
    bot.run(token)
except discord.errors.LoginFailure:
    print("Invalid token")
