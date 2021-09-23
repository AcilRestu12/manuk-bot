import discord
from discord.ext import commands
from discord.flags import Intents

import Music

cogs = [Music]

client = commands.Bot(command_prefix="`", Intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("ODkwMjQ2NDAyMDY2NzYzODA2.YUtAkg.j63IjtaoA1psjbG_DJPUg12HA40")



