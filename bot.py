import discord
import random

aquatic = [
        "octopus",
        "squid",
        "shrimp",
        "lobster",
        "oyster",
        "crab",
        "blowfish",
        "tropical_fish",
        "fish",
        "dolphin",
        "whale",
        "whale2",
        "shark",
    ]

def strToEmoji(string):
    return ":"+string+":"

def randomAquatic():
    i = random.randint(0, len(aquatic)-1)
    return strToEmoji(aquatic[i])

def aquaticAll():
    string = ""
    for animal in aquatic:
        string += strToEmoji(animal)
    return string

class Bot(discord.Client):

    async def on_ready(self):
        print("We have logged in as {}".format(self.user))
        pass

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        print ("{} sent {}".format(message.author, message.content))
        if message.content.startswith("$ping"):
            await message.channel.send(
                    "@{} pong!".format(
                        message.author.mention
                        )
                    )
        
        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

        if message.content.startswith("$aquaticall"):
            await message.channel.send(aquaticAll())
            
        elif message.content.startswith("$aquatic"):
            await message.channel.send(randomAquatic())


bot = Bot()
bot.run("NzE5Njk0MDM1ODAyOTE0ODc4.Xv0eiA.lHKbn3MFvYjqvBoEND51cP_y_gA");
