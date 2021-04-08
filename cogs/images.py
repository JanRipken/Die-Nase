import random

import aiohttp
from discord.ext import commands
import discord

import praw

from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_ENABLED_MEME_SUBREDDITS, REDDIT_ENABLED_NSFW_SUBREDDITS


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_ID and REDDIT_APP_SECRET:
            self.reddit = praw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET,
                                    user_agent="Die_Nase:%s:1.0" % REDDIT_APP_ID)


    @commands.command(brief="Zufälliger reddit Content")
    async def random(self, ctx, subreddit: str = ""):
        async with ctx.channel.typing():
            if self.reddit:

                nsfw_flag = False
                chosen_subreddit = REDDIT_ENABLED_MEME_SUBREDDITS[0]
                if subreddit:

                    if subreddit in REDDIT_ENABLED_MEME_SUBREDDITS:
                        chosen_subreddit = subreddit
                    elif subreddit in REDDIT_ENABLED_NSFW_SUBREDDITS:
                        chosen_subreddit = subreddit
                        nsfw_flag = True
                    else:
                        list_memes = ", ".join(REDDIT_ENABLED_MEME_SUBREDDITS)
                        list_nsfw = ", ".join(REDDIT_ENABLED_NSFW_SUBREDDITS)

                        await ctx.send("Ne Bruder nicht so nen Shit nur das hier: %s NSFW Channels: %s" % (list_memes, list_nsfw))
                        return

                if nsfw_flag:
                    if not ctx.channel.is_nsfw():
                        await ctx.send("Digga..... nicht hier")
                        return

                submissions = self.reddit.subreddit(chosen_subreddit).hot()

                post_to_pick = random.randint(1, 80)
                for i in range(0, post_to_pick):
                    submission = next(x for x in submissions if not x.stickied)
                await ctx.send(submission.url)

            else:
                await ctx.send("ufff klappt wohl nicht Brudi.")
            



    @commands.command(brief="Zufälliges bild von einer katze")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)



    @commands.command(brief="Zufälliges bild von nem Hund")
    async def puppy(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog/")

                    await ctx.send(embed=embed)


    @commands.command(brief="Zufälliges bild von nem Fuchs")
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://randomfox.ca/floof/") as r:
                    data = await r.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")

                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Images(bot))