from discord.ext import commands
import discord

import datetime

from settings import MODERATOR_ROLE_NAME


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, *args):
        guild = ctx.guild

        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)

        embed = discord.Embed(description="Server Status",
                            colour=discord.Colour.dark_purple())


        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Custom Emojies",
                        value=emoji_string or "No emojis available", inline=False)

        embed.add_field(name="Server Name", value=guild.name, inline=False)

        embed.add_field(name="# Voice Channels", value=no_voice_channels)

        embed.add_field(name="# Text Channels", value=no_text_channels)

        embed.add_field(name="# AFK Channel:", value=guild.afk_channel)
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))