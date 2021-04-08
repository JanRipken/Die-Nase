from discord.ext import commands
import discord

from utils import mods_or_owner


class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, reason: str = "Bis dennis !"):
        if member is not None:
            await ctx.guild.kick(member, reason=reason)
        else:
            await ctx.send("Wer genau soll gekickt werden ? (Mention)")

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "BYE BYE YOU GOT FUCKED"):
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
        else:
            await ctx.send("Wer genau soll gebannt werden ? (Mention)")

    @commands.command()
    @mods_or_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: str = "", reason: str = "alles klar du darfst zurück"):
        if member == "":
            await ctx.send("genaue angabe (text)")
            return

        bans = await ctx.guild.bans()
        for b in bans:
            if b.user.name == member:
                await ctx.guild.unban(b.user, reason=reason)
                await ctx.send("jo top der ist back")
                return
        await ctx.send("sicher das der gebannt ist ?")


def setup(bot):
    bot.add_cog(Moderator(bot))