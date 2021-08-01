#setup 
import discord
import os
import json
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from keep_alive import keep_alive


def get_prefix(client, message):
	with open('json/prefixes.json','r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(status=discord.Status.idle, activity = discord.Game('Somewhere Only We Know'))
#setup ends



#load and unload cogs
@client.command()
async def load(ctx,extension):
	client.load.extension(f'cogs.{extensions}')

@client.command()
async def unload(ctx,extension):
	client.unload.extension(f'cogs.{extensions}')
	

#load and unload ends

#ping
@client.command()
async def ping(ctx):
		await ctx.send(f'pong! latency: {round(client.latency*1000)}ms')

#ping ends

# client.remove_command('help')

# @client.command()
# async def help(ctx):
# 	await ctx.send('buildin')






#reaction role for all servers
@client.command()
@commands.has_permissions(manage_roles=True)
async def reactionrole(ctx, emoji, role : discord.Role, *, message):

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




@client.event
async def on_raw_reaction_add(payload):

	if payload.member.bot:
		pass
	else:
		with open('json/reactrole.json') as react_file:

			data =  json.load(react_file)
			for x in data:
				if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
					role = discord.utils.get(client.get_guild(payload.guild_id).roles, id = x['role_id'])

					await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):

	with open('json/reactrole.json') as react_file:

		data =  json.load(react_file)
		for x in data:
			if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
				role = discord.utils.get(client.get_guild(payload.guild_id).roles, id = x['role_id'])

				await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

				
#reaction role for all ends




#run the bot

#loop through cogs
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
client.run(os.environ['TOKEN'])


