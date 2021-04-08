from discord.ext import commands
import discord

from utils import text_to_owo, notify_user


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send(" Bitte überprüfe mit Hilfe des !help commands oder frage einen Admin")

    @commands.command(brief="OwO")
    async def OwO(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command(brief="Invite Link")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=3)
        await ctx.send(link)

    @commands.command(brief="Anstupsen")
    async def poke(self, ctx, member: discord.Member = None):

        if member is not None:
            message = "%s poked you!!!!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")


def setup(bot):
    bot.add_cog(Basic(bot))