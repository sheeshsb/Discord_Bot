import discord
from discord.ext import commands
import random

#list dump

colors = [0x4B22CA, 0xF55501, 0x57D319, 0x4268D7, 0xCB4575, 0x892EDC, 0xDC143C, 0x297AF8, 0xE928CA, 0x3CE2FD, 0x2AFBF0, 0xC27969, 0xD6D479, 0xEEA9E0, 0x0089D3, 0xF1F5F8 ]

sad_gifs = ['https://media.giphy.com/media/dJYoOVAWf2QkU/giphy.gif','https://media.giphy.com/media/l22ysLe54hZP0wubek/giphy.gif','https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif','https://media.giphy.com/media/ivH4UhEAPXNAI/giphy.gif','https://media.giphy.com/media/3dfEA0VTslup2/giphy.gif','https://media.giphy.com/media/TU76e2JHkPchG/giphy.gif',
'https://media.giphy.com/media/k61nOBRRBMxva/giphy.gif','https://media.giphy.com/media/O3JyUHiKqsviE/giphy.gif','https://media.giphy.com/media/Z9hZLKflOlXjo349De/giphy.gif','https://media.giphy.com/media/14iZJ2agTAAb6w/giphy.gif']



happy_gifs = ['https://media.giphy.com/media/b5LTssxCLpvVe/giphy.gif','https://media.giphy.com/media/AAm2JkkJBauTWkYKoe/giphy.gif','https://media.giphy.com/media/wCXncO2394zRe/giphy.gif','https://media.giphy.com/media/xuXzcHMkuwvf2/giphy.gif','https://media.giphy.com/media/1xVfHenZgbysbdumIP/giphy.gif','https://media.giphy.com/media/iPTTjEt19igne/giphy.gif','https://media.giphy.com/media/WsKVAem02Efuw/giphy.gif','https://media.giphy.com/media/HVp1HhQyeb58Q/giphy.gif','https://media.giphy.com/media/kNA1sKSqxgFDq/giphy.gif','https://media.giphy.com/media/sIV0wFDrsKNxe/giphy.gif']


wtf_gifs = ['https://media.giphy.com/media/bzOwkffoJcEXcP2OxW/giphy.gif','https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif','https://media.giphy.com/media/p5BLHbXjetrfq/giphy.gif','https://media.giphy.com/media/3oEjI2g6msAy8jw3SM/giphy.gif','https://media.giphy.com/media/ypX8YZszkIXFC/giphy.gif','https://media.giphy.com/media/y7LLt6Cmv62Lm/giphy.gif','https://media.giphy.com/media/9DcrUwUGuAGkWM0qvx/giphy.gif','https://media.giphy.com/media/26DNiPEllpCp0Aqo8/giphy.gif','https://media.giphy.com/media/8wfu3AjTdgNyxfCF3z/giphy.gif','https://media.giphy.com/media/NeDuhuEngZ5ny/giphy.gif']



wow_gifs = ['https://media.giphy.com/media/vKHKDIdvxvN7vTAEOM/giphy.gif','https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif','https://media.giphy.com/media/aWPGuTlDqq2yc/giphy.gif','https://media.giphy.com/media/WuGSL4LFUMQU/giphy.gif','https://media.giphy.com/media/6nWhy3ulBL7GSCvKw6/giphy.gif','https://media.giphy.com/media/Lcn0yF1RcLANG/giphy.gif','https://media.giphy.com/media/xT77XWum9yH7zNkFW0/giphy.gif','https://media.giphy.com/media/Sqfu14lSonVN219Zb6/giphy.gif','https://media.giphy.com/media/R8n7YlPHe34dy/giphy.gif','https://media.giphy.com/media/M33UV4NDvkTHa/giphy.gif']


bored_gifs = ['https://media.giphy.com/media/l2JhpjWPccQhsAMfu/giphy.gif','https://media.giphy.com/media/ZgqJGwh2tLj5C/giphy.gif','https://media.giphy.com/media/dYQh2AcRNN6Jq/giphy.gif','https://media.giphy.com/media/NWg7M1VlT101W/giphy.gif','https://media.giphy.com/media/dT7LBdAZP1Rh6/giphy.gif','https://media.giphy.com/media/hSFGpAAuz3REzMXrkv/giphy.gif','https://media.giphy.com/media/ARH12W5IVAbni/giphy.gif','https://media.giphy.com/media/l378AEZceMwWboAQE/giphy.gif','https://media.giphy.com/media/tCSw9mQpVnAvS/giphy.gif','https://media.giphy.com/media/3o7qDGam0NCE46jja0/giphy.gif']

#partner_hug
#'https://media.giphy.com/media/U4LhzzpfTP7NZ4UlmH/giphy.gif'


#list dump ends


class GIFS(commands.Cog):
	def __init__(self,client):
		self.client = client

	


	@commands.command()
	async def sad(self,ctx):
		emb = discord.Embed(title =f"{ctx.author.display_name} is Sad!",color =random.choice(colors))
		emb.set_image(url = random.choice(sad_gifs))
		await ctx.send(embed = emb)

	@commands.command()
	async def happy(self,ctx):
		emb = discord.Embed(title =f"{ctx.author.display_name} is Happy!",color =random.choice(colors))
		emb.set_image(url = random.choice(happy_gifs))
		await ctx.send(embed = emb)
	
	@commands.command()
	async def wtf(self,ctx):
		emb = discord.Embed(title =f"{ctx.author.display_name} is like:",color =random.choice(colors))
		emb.set_image(url = random.choice(wtf_gifs))
		await ctx.send(embed = emb)
	

	@commands.command()
	async def wow(self,ctx):
		emb = discord.Embed(title =f"{ctx.author.display_name} is like:",color =random.choice(colors))
		emb.set_image(url = random.choice(wow_gifs))
		await ctx.send(embed = emb)


	@commands.command()
	async def bored(self,ctx):
		emb = discord.Embed(title =f"{ctx.author.display_name} is like:",color =random.choice(colors))
		emb.set_image(url = random.choice(bored_gifs))
		await ctx.send(embed = emb)





	






def setup(client):
	client.add_cog(GIFS(client))