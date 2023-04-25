from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import json

file = open('config.json', 'r')
config = json.load(file)

bot = Bot(token = config['TelegramBotToken'])
dp = Dispatcher(bot)
