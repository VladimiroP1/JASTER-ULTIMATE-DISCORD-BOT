from disnake.ext import commands
import disnake

class ShowRolesMsgCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def srm(self, ctx):
        embed = disnake.Embed(title='Выберите роль:',
                              description='Нажмите на реакцию, чтобы получить доступ к категории.')

        emoji1 = disnake.PartialEmoji(name='JS', id=1132311764172816474, animated=False)
        emoji2 = disnake.PartialEmoji(name='HTML/CSS', id=1132315126565961770, animated=False)

        embed.add_field(name=str(emoji1), value='JS', inline=False)
        embed.add_field(name=str(emoji2), value='HTML/CSS', inline=False)

        message = await ctx.send(embed=embed)

        await message.add_reaction(emoji1)
        await message.add_reaction(emoji2)

def setup(bot):
    bot.add_cog(ShowRolesMsgCog(bot))