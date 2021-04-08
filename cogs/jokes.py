from discord.ext import commands
import discord




class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Kleiner Joke")
    async def joke(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://sv443.net/jokeapi/v2") as r:
                    data = await r.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="https://sv443.net/jokeapi/v2")

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jokes(bot))