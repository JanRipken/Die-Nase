import discord
from discord.ext import commands

from utils import get_momma_jokes


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Yoooo Momma is!")
    async def insult(self, ctx, member: discord.Member = None):
        insult = await get_momma_jokes()
        if member is not None:
            print("1")
            await ctx.send("%s friss das: %s " % (member.name, insult))
        else:
            print("2")
            await ctx.send("%s Selfdiss: %s " % (ctx.message.author.name, insult))


def setup(bot):
    bot.add_cog(NSFW(bot))