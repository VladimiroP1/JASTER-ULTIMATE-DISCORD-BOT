from disnake.ext import commands
import disnake



class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        embed = disnake.Embed(title="Clear: done",
                              description=f"I have cleared {amount} messages.",
                              color=disnake.Color.from_rgb(139, 69, 19))
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(ClearCog(bot))