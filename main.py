import os


from discord.ext import commands

from settings import *



bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "_init_.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(DISCORD_BOT_TOKEN)







