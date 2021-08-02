import discord
from discord.ext import commands

class misc(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def avatar(self, ctx,member: discord.Member = None):
		if member == None:
			member = ctx.author
		
		member_avatar = member.avatar_url
		avatar_embed = discord.Embed(title = f"{member.name}'s Avatar", color = discord.Color.green())
		avatar_embed.set_image(url = member_avatar)
		await ctx.send(embed = avatar_embed)






def setup(client):
	client.add_cog(misc(client))