import discord
from discord.ext import commands
import json

class prefixes(commands.Cog):
	def __init__(self,client):
		self.client = client


	@commands.Cog.listener()
	async def on_guild_join(self, guild):

		with open('json/prefixes.json','r') as f:
			prefixes = json.load(f)
		
		prefixes[str(guild.id)] = '.'

		with open('json/prefixes.json','w') as f:
			json.dump(prefixes,f,indent = 4)

	

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		with open('json/prefixes.json','r') as f:
			prefixes = json.load(f)

		prefixes.pop(str(guild.id))

		with open('json/prefixes.json','w') as f:
			json.dump(prefixes,j,indent = 4)



	@commands.command(aliases=['cp'])
	@commands.has_permissions(administrator = True)
	async def change_prefix(self, ctx, prefix):
		with open('json/prefixes.json','r') as f:
			prefixes = json.load(f)

		prefixes[str(ctx.guild.id)] = prefix

		with open('json/prefixes.json', 'w') as f:
			json.dump(prefixes, f, indent = 4)
		await ctx.send(f':white_check_mark: The prefix for this server has been changed to {prefix}')









def setup(client):
	client.add_cog(prefixes(client))
