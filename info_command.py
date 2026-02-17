from disnake.ext import commands
import disnake



class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def info(self, ctx):
        embed = disnake.Embed(title="Информация о боте.",
                              description="RU: Я - Discord бот JASTER. Мой разработчик Todiro, написан я на языке программирования Python вместе в библиотекой Disnake. Во мне встроенны такие функции как:",
                              color=disnake.Color.green())
        embed.add_field(name="Поле 1", value="Значение 1", inline=False)
        embed.add_field(name="Поле 2", value="Значение 2", inline=False)
        embed.set_footer(text="Это нижний колонтитул")
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(InfoCog(bot))
