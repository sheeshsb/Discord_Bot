import discord
from discord.ext import commands
import json


class role_react(commands.Cog):
	def __init__(self,client):
		self.client = client


	
	@commands.command(aliases=['rr'])
	@commands.has_permissions(manage_roles=True)
	async def reactionrole(self, ctx, emoji, role : discord.Role, *, message):

		emb = discord.Embed(title='Reaction Role',description=message, colour=0x87CEEB)
		msg = await ctx.channel.send(embed=emb)
		await msg.add_reaction(emoji)

		with open('json/reactrole.json') as json_file:
			data = json.load(json_file)


			new_react_role = {
				'role_name':role.name,
				'role_id': role.id,
				'emoji': emoji,
				'message_id': msg.id
			}
			
			data.append(new_react_role)

		with open('json/reactrole.json','w') as j:
			json.dump(data,j,indent=4)




	@commands.Cog.listener()
	async def on_raw_reaction_add(self,payload):

		if payload.member.bot:
			pass
		else:
			with open('json/reactrole.json') as react_file:

				data =  json.load(react_file)
				for x in data:
					if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
						role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['role_id'])

						await payload.member.add_roles(role)


	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):

		with open('json/reactrole.json') as react_file:

			data =  json.load(react_file)
			for x in data:
				if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
					role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['role_id'])

					await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)






def setup(client):
	client.add_cog(role_react(client))