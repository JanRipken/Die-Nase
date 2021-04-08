import random

from discord.ext import commands


class Raten(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Zahl zwischen 1 und 100")
    async def numbers(self, ctx):
        n = random.randrange(1, 101)
        await ctx.send(n)

    @commands.command(brief="Zahl zwischen 1 und 6")
    async def dice(self, ctx):
        n = random.randrange(1, 6)
        await ctx.send(n)

    @commands.command(brief="Kopf oder Zahl")
    async def coin(self, ctx):
        n = random.randint(0, 1)
        await ctx.send("Kopf" if n == 1 else "Zahl")


def setup(bot):
    bot.add_cog(Raten(bot))