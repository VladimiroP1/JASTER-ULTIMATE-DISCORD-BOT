from disnake.ext import commands
import disnake

bad_words = {
    "блять": "Блин",
    "хуй": "Хвост",
    "пизда": "Писька",
    "Долбаеб": "Идиот",
    "Idiot": "Fuck"}
class BadWordsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.event
        async def on_message(message):
            if message.author == bot.user:
                return

            content_lower = message.content.lower()

            for bad_word in bad_words.keys():
                if bad_word in content_lower:
                    new_content = message.content.replace(bad_word, bad_words[bad_word], 1)
                    await message.channel.send(f"{message.author.mention}: {new_content}")
                    await message.delete()
                    return
            await bot.process_commands(message)


def setup(bot):
    bot.add_cog(BadWordsCog(bot))



