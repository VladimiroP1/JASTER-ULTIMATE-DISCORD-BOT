from disnake.ext import commands
import disnake



class MemberLeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_member_remove(member):
            channel = bot.get_channel(1128272561512390806)
            if channel is not None:
                leave_message = f'Увы, но {member} вышел с сервера...'
                await channel.send(leave_message)


 


def setup(bot):
    bot.add_cog(MemberLeaveCog(bot))