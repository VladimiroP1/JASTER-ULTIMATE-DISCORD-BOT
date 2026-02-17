import disnake
from disnake.ext import commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} был разблокирован.')
                return

        await ctx.send('Пользователь не найден в списке забаненных.')

def setup(bot):
    bot.add_cog(UnbanCog(bot))