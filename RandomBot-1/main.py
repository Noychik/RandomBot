from email.errors import NoBoundaryInMultipartDefect
import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random

#   TOKEN   #
bot = Bot(token="5385406422:AAGnCUR7gRZ8xTZgr8rdRY4NIXbktJORlNg")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


#   CONNECT  SQL   #
conn = sqlite3.connect('db/db.db', check_same_thread=False)
cursor = conn.cursor()

def db_tab_val(user_id: int, user_name: str, user_surname: str, username: str, us_starting:str):
    cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username, us_starting) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, us_starting))
    conn.commit()
def upd_tab_val(user_id, us_starting):
    cursor.execute("UPDATE `test` SET `us_starting` = ? WHERE `user_id` = ?", (us_starting, user_id(user_id)))
    return conn.commit()


#      VARIABLE      #
a = 0
xr = 0
nufl = None


#      MESSAGE      #
@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Добавить бота в группу", url="http://t.me/djdbddjdiekemehzoakwbot?startgroup=Lichka")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)

    nufl = 1
    
    await message.answer("Привет! Здесь ты можешь узнать сколько у тебя хромосом"
                         "\nОт -5, до +10 за одну команду"
                         "\nПо команде /check", reply_markup=keyboard)
    
    
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username

    db_tab_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

@dp.message_handler(commands=["check"])
async def volume(message: types.Message):
    global xr
    rand = int(random.randint(-5, 10))
    su = rand + a + int(xr)
    #      FIRST   NAME     #   
    if rand == 0:
        xr = str(su)
        await message.answer(f"{message.from_user.first_name}, твоё количство хромосом не изменилось, их количество равно " + xr + ' шт')
    elif rand > 0:
        xr = str(su)
        await message.answer(f"{message.from_user.first_name}, твоё количство хромосом увеличилось, их количество равно " + xr + ' шт')
    elif rand < 0:
        xr = str(su)
        await message.answer(f"{message.from_user.first_name}, твоё количство хромосом уменьшилось, их количество равно " + xr + ' шт')

    us_id = message.from_user.id
    xr = str(su)
    usvol = xr
    upd_tab_val(user_id=us_id, us_starting=usvol)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)