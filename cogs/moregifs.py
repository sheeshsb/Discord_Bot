import discord
import random
from discord.ext import commands


colors = [0x4B22CA, 0xF55501, 0x57D319, 0x4268D7, 0xCB4575, 0x892EDC, 0xDC143C, 0x297AF8, 0xE928CA, 0x3CE2FD, 0x2AFBF0, 0xC27969, 0xD6D479, 0xEEA9E0, 0x0089D3, 0xF1F5F8 ]

hug_gifs = ['https://media.giphy.com/media/U4LhzzpfTP7NZ4UlmH/giphy.gif','https://media.giphy.com/media/l8ooOxhcItowwLPuZn/giphy.gif','https://media.giphy.com/media/KL7xA3fLx7bna/giphy.gif','https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif','https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif','https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif','https://media.giphy.com/media/ShAchOHe38Aak/giphy.gif']

slap_gifs = ['https://media.giphy.com/media/10DRaO76k9sgHC/giphy.gif','https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif','https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif','https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif','https://media.giphy.com/media/Qv7WFppXtkqkM/giphy.gif','https://media.giphy.com/media/LSc9OoFCKcVlLYYb3d/giphy.gif','https://media.giphy.com/media/WR38ZOQlzRowS6OmrR/giphy.gif']


class PARTNER_GIFS(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def hug(self,ctx,member: discord.Member = None):
		if member == None:
			await ctx.send('Who do you wanna hug ? <3')

		else:
		
			emb = discord.Embed(title =f"{ctx.author.display_name} hugs {member.display_name}",color =random.choice(colors))
			emb.set_image(url = random.choice(hug_gifs))
			await ctx.send(embed = emb)

	
		@commands.command()
		async def slap(self,ctx,member: discord.Member = None):
			if member == None:
				await ctx.send('Who deserves a slap?')

			else:
			
				emb = discord.Embed(title =f"{ctx.author.display_name} slaps {member.display_name}",color =random.choice(colors))
				emb.set_image(url = random.choice(slap_gifs))
				await ctx.send(embed = emb)




def setup(client):
	client.add_cog(PARTNER_GIFS(client))











	









