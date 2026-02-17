from disnake.ext import commands
import disnake



class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: disnake.Member):
        await member.kick()
        await ctx.send(f'{member.mention} был кикнут с сервера.')




def setup(bot):
    bot.add_cog(KickCog(bot))