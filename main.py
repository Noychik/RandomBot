import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import random
 
bot = Bot(token="token_bot")
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def choose_gender(message: types.Message):
    await message.answer("Привет! Здесь ты можешь узнать сколько у тя см хуй"
                         "\n По команде /check")
    
