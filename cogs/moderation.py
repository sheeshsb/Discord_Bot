import discord
from discord.ext import commands

class MODERATION(commands.Cog):
	def __init__(self,client):
		self.client = client
	
	@commands.command()
	@commands.has_permissions(kick_members = True) 
	async def kick(self,ctx, member : discord.Member, *,reason=None):
		await member.kick(reason=reason)
		await ctx.send(f'{member.mention} was kicked due to the reason:  {reason}')

	@commands.command()
	@commands.has_permissions(ban_members=True) 
	async def ban(self,ctx, member: discord.Member, *,reason=None):
		await member.ban(reason=reason)
		await ctx.send(f'{member.mention} was banned due to the reason:  {reason}')

	@commands.command()
	@commands.has_permissions(ban_members=True) 
	async def unban(self,ctx, *,member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.discriminator)==(member_name , member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {user.mention}')
				return

	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx, amount =5):
		await ctx.channel.purge(limit=amount+1)
		await ctx.send(f':white_check_mark: {amount} messages deleted!', delete_after=3)




def setup(client):
	client.add_cog(MODERATION(client))

