from disnake import Member
from datetime import datetime, timedelta
from disnake.ext import commands
import disnake
import asyncio

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, member: disnake.Member, time: str, reason: str):
        mute_role = disnake.utils.get(ctx.guild.roles, name="Muted")  # Проверяем, есть ли роль "Muted" на сервере

        if not mute_role:
            # Если роли "Muted" нет, создаем ее
            mute_role = await ctx.guild.create_role(name="Muted", reason="Role for muting members")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, send_messages=False)

        await member.add_roles(mute_role, reason=reason)

        unmute_time = datetime.now() + timedelta(minutes=int(time))
        await asyncio.sleep(int(time) * 60)  # Задержка на указанное количество минут
        await member.remove_roles(mute_role, reason="Mute duration expired")

        await ctx.response.send_message(f"{member.mention} был замьючен на {time} минут из-за {reason}", ephemeral=True)

def setup(bot):
    bot.add_cog(MuteCog(bot))