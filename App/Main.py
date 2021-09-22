import discord
from discord.ext import commands
from discord.flags import Intents

import Music

cogs = [Music]

client = commands.Bot(command_prefix="-m", Intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)




client.run("ODkwMjQ2NDAyMDY2NzYzODA2.YUtAkg.hH70ZrzEK7CuGG-Kf0ioyM9vau4")



