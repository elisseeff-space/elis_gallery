from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import json
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data_base import sqllite_db

file = open('config.json', 'r')
config = json.load(file)

storage = MemoryStorage()

bot = Bot(token = config['TelegramBotToken'])
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
    print('Gallery Bot online!')
    sqllite_db.sql_start()
    await bot.set_webhook(config['URL_APP'])

async def on_startup(_):
    print('Gallery Bot off!')
    await bot.delete_webhook()
