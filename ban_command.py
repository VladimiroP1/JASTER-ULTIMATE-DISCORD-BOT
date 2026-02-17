from disnake.ext import commands
import disnake
import sqlite3




class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('jasterdatabase.db')
        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS banned_users
                         (banned_user_id INTEGER, author_id INTEGER, reason TEXT)''')
        self.conn.commit()

    def __unload(self):
        self.conn.close()

    async def add_banned_user(self, banned_user_id, author_id, reason):
        self.c.execute("INSERT INTO banned_users (banned_user_id, author_id, reason) VALUES (?, ?, ?)",
                       (banned_user_id, author_id, reason))
        self.conn.commit()

    async def get_banned_user(self, banned_user_id):
        self.c.execute("SELECT * FROM banned_users WHERE banned_user_id=?", (banned_user_id,))
        result = self.c.fetchone()
        return result

    @commands.slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: disnake.Member, reason):
        author_of_ban_nick = ctx.author.nick
        if member.top_role >= ctx.author.top_role:
            embed = disnake.Embed(
                title="Ошибка",
                description="Вы не можете забанить пользователя с более высокой или равной ролью.",
                color=disnake.Color.red()
            )
            await ctx.send(embed=embed)
            return

        await member.ban(reason=reason)
        await ctx.guild.ban(member)

        await self.add_banned_user(member.id, ctx.author.id, reason)

        embed = disnake.Embed(title="BAN", color=disnake.Color.red())
        embed.add_field(name="Banned user:", value=member, inline=False)
        embed.add_field(name="Who banned:", value=author_of_ban_nick, inline=False)
        embed.add_field(name="Reason:", value=reason, inline=False)
        embed.set_thumbnail(url='https://wampi.ru/image/R9MYVdx')
        embed.set_image(url='https://wampi.ru/image/R9MYBfH')

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(BanCog(bot))