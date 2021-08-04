import discord
from discord.ext import commands

class ERRORS(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send(':x: Missing Arguements! Please pass all required arguements.')
		elif isinstance(error, commands.CommandNotFound):
	 		await ctx.send(':x: Invalid Command! Please use .help to see all valid commands.')
		elif isinstance(error, commands.MissingPermissions):
			await ctx.send(':x: You do not have the permission to do that!')
		elif isinstance(error, commands.BadArgument):
			await ctx.send(':x: Improper Arguments Provided.')
		else:
			raise error






def setup(client):
	client.add_cog(ERRORS(client))