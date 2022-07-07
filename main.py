import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random

bot = Bot(token="token_bot")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

a = 0

@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.answer("Привет! Здесь ты можешь узнать сколько у тя см хуй"
                         "\n По команде /check")
    
@dp.message_handler(commands=["check"])
async def volume(message: types.Message):
    
    rand = int(random.randint(-15, 15))
    sum = rand + sum + a
    
    await message.answer("Вот твой хуёк" + sum)
