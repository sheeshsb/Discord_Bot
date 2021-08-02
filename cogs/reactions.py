import discord
from discord.ext import commands
import aiohttp



class reactions(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def sad (self, ctx):
		await ctx.send('buildin')







def setup(client):
	client.add_cog(reactions(client))