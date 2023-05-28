from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import json
from aiogram.contrib.fsm_storage.memory import MemoryStorage

file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

storage = MemoryStorage()

bot = Bot(token = config['elis_gallery_bot'])
dp = Dispatcher(bot, storage=storage)