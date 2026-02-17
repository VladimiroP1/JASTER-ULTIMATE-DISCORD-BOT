from disnake.ext import commands
import disnake



class MemberJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_member_join(member):
            channel = bot.get_channel(1048339377408966676)
            if channel is not None:
                welcome_message = f'Добро пожаловать, {member.mention}! Приветствуем тебя на нашем сервере!'
                await channel.send(welcome_message)




def setup(bot):
    bot.add_cog(MemberJoinCog(bot))
