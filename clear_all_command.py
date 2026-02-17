from disnake.ext import commands
import disnake



class ClearAllCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def clear_all(self, ctx):
        await ctx.channel.purge()
        embed = disnake.Embed(title="Clear all: done",
                              description="I have cleared all the chat messages.",
                              color=disnake.Color.from_rgb(139, 69, 19))
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(ClearAllCog(bot))
