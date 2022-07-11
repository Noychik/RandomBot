import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random

bot = Bot(token="5477947327:AAFYzuSSYKNt7fXbY6imbK202rdDHdST-Yk")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('db/db.db', check_same_thread=False)
cursor = conn.cursor()

def db_tab_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()

a = 0
sum = 6
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Привет! Здесь ты можешь узнать сколько у тя см хуй"
                         "\n По команде /check")
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_tab_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    
@dp.message_handler(commands=["check"])
async def volume(message: types.Message):
    
    rand = int(random.randint(-15, 15))
    sum = str(rand + a)
    
    await message.answer("Вот твой хуёк = " + sum)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)