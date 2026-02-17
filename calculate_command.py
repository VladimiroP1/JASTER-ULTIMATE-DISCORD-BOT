from disnake.ext import commands
import disnake




class CalculateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def calculate(self, ctx, first_number: int, operation, second_number: int):
        if operation == '+':
            answer = first_number + second_number
        elif operation == '-':
            answer = first_number - second_number
        elif operation == '*':
            answer = first_number * second_number
        elif operation == '/':
            answer = first_number / second_number
        else:
            await ctx.send("Такой операции пока что не существует. пожалуйста, введите одну операцию из этих: +, -, *, /")
            return
        await ctx.send(answer)





def setup(bot):
    bot.add_cog(CalculateCog(bot))