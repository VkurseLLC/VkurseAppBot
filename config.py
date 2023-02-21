import random
import hashlib
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '6009259093:AAHVe3QNenq9EfY_iXyxc5WRDvzCn7QuFd4'



take_code_markup = types.InlineKeyboardMarkup()
take_code_markup.add(types.InlineKeyboardButton(text = "Получить код подтверждения ", callback_data = "take_code"))

markup_number = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
markup_number.add(types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True, remove=True))



def give_code():
    code = random.randint(10000, 100000)
    return code






