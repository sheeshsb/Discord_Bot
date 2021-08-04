import discord
from discord.ext import commands
from googleapiclient.discovery import build
import random

class images(commands.Cog):
	def __init__(self, client):
		self.client = client



	@commands.command(aliases=["img"])
	async def search(self, ctx, *, search):
			api_key = "AIzaSyDHvTXtnHflihoKBiBrEP0mCcj1zDsfhGY"
			ran = random.randint(0, 9)
			resource = build("customsearch", "v1", developerKey=api_key).cse()
			result = resource.list(
					q=f"{search}", cx="bf8cb25ceadf0419b", searchType="image"
			).execute()
			url = result["items"][ran]["link"]
			embed1 = discord.Embed(title=f"Here Is Your Image ({search.title()})")
			embed1.set_image(url=url)
			embed1.set_footer(text = f'Image requested by {ctx.author}')
			await ctx.send(embed=embed1)









def setup(client):
	client.add_cog(images(client))




