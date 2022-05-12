from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
token = '5199205252:AAFrR3BtwQMK1CjOBIbhQtPlUQYuQT8aB7E'

bot = Bot(token)
dp = Dispatcher(bot, storage=storage)