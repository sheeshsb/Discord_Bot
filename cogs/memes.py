import discord
from discord.ext import commands
import random
import aiohttp


class memes(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command(aliases = ['m'])
	async def meme(self, ctx):
		async with aiohttp.ClientSession() as cs:
			async with cs.get("https://www.reddit.com/r/memes/new.json") as r:
				meme = await r.json()
				embed = discord.Embed(title = 'Meme', color = discord.Color.red())
				embed.set_image(url=meme["data"]["children"][random.randint(0,25)]["data"]["url"])
				embed.set_footer(text = f'Powered by r/memes! Meme requested by {ctx.author}')
				await ctx.send(embed=embed)





def setup(client):
	client.add_cog(memes(client))
