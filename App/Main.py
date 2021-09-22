import discord
from discord.ext import commands
from discord.flags import Intents

import Music

cogs = [Music]

client = commands.Bot(command_prefix="-m", Intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

# Ur
# client.run("")



