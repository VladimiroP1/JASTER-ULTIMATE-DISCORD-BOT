from disnake.ext import commands
import disnake



class ViktorinaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.slash_command()
    async def quiz(ctx, *, question, option1, option2, option3, option4, answer):
        embed = disnake.Embed(title="QUIZ", description=question, color=disnake.Color.yellow())

        # Добавляем варианты ответов во встроенное сообщение
        embed.add_field(name="Option 1", value=option1, inline=False)
        embed.add_field(name="Option 2", value=option2, inline=False)
        embed.add_field(name="Option 3", value=option3, inline=False)
        embed.add_field(name="Option 4", value=option4, inline=False)
        message = await ctx.send(embed=embed)
        await message.add_reaction("1️⃣")  # Реакция на вариант 1
        await message.add_reaction("2️⃣")  # Реакция на вариант 2
        await message.add_reaction("3️⃣")  # Реакция на вариант 3
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ViktorinaCog(bot))









