import disnake
import sqlite3
from disnake.ext import commands
import os

bot = commands.Bot(command_prefix='/', intents=disnake.Intents.all())

def create_connection():
    return sqlite3.connect("jasterdatabase.db")

def create_users_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)"""
    )
    connection.commit()
    connection.close()

def add_new_user(user_id, user_name):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (id, name, balance) VALUES (?, ?, ?)", (user_id, user_name, 0))
    connection.commit()
    connection.close()

def get_user_balance(user_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    connection.close()
    if result:
        return result[0]
    else:
        return None

def update_user_balance(user_id, new_balance):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
    connection.commit()
    connection.close()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    create_users_table()

@bot.command()
async def balance(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.name
    user_balance = get_user_balance(user_id)
    if user_balance is None:
        add_new_user(user_id, user_name)
        user_balance = 0

    await ctx.send(f"{ctx.author.mention}, ваш баланс: {user_balance}")

@bot.command()
async def work(ctx):
    user_id = ctx.author.id
    user_name = ctx.author.name
    earnings = 100
    user_balance = get_user_balance(user_id)
    if user_balance is None:
        add_new_user(user_id, user_name)
        user_balance = 0

    new_balance = user_balance + earnings
    update_user_balance(user_id, new_balance)

    await ctx.send(f"{ctx.author.mention}, вы заработали {earnings} монет!")


@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов к использованию.')



# Загрузка когов
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')




#Запуск бота
bot.run('TOKEN')