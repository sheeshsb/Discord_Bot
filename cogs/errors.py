import discord
from discord.ext import commands

class errors(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Missing Arguements! Please pass all required arguements.')
		elif isinstance(error, commands.CommandNotFound):
	 		await ctx.send('Invalid Command! Please use .help to see all valid commands.')
		elif isinstance(error, commands.MissingPermissions):
			await ctx.send('You do not have the permission to do that!')
		else:
		 print(error)



def setup(client):
	client.add_cog(errors(client))