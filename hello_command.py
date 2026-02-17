from disnake.ext import commands
import disnake





class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Поздоровайся с ботом!")
    async def hello(self,ctx):
        hello_description_ru = "Привет, я многофункциональный бот JASTER! я написан на языке программирования Python. Во мне встроенно большое количество функций, к примеру: **ban**, **mute**, **kick**, **help**, **work**, **quiz** и так далее, ведь это самая малая часть моих функций. Для более подробного ознакомления с ботом используйте команду **/info**."
        hello_description_en = "Hi, I'm a multifunctional bot JASTER! I am written in the Python programming language. I have a large number of built-in functions, for example: **ban**, **mute**, **kick**, **help**, **work**, **quiz** and so on, because this is the smallest part of my functions. To learn more about the bot, use the command **/info**."
        embed = disnake.Embed(title="Hi! This is a little bit about me.",
                              color = disnake.Color.from_rgb(139, 69, 19))
        embed.set_footer(text="DEV: Todiro")
        embed.add_field(name="ENGLISH", value=hello_description_en, inline=False)
        embed.add_field(name="RUSSIAN", value=hello_description_ru, inline=False)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(HelloCog(bot))