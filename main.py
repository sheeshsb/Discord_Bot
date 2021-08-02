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


#run the bot

#loop through cogs
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')



keep_alive()
client.run(os.environ['TOKEN'])


