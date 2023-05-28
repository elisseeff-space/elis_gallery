from aiogram import types, Dispatcher
from create_bot import dp, bot
from client_kb import kb_client
from aiogram.types import ReplyKeyboardRemove
from sqlite_db import sql_read

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствую Вас в моей картинной галерее!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личку. Напишите ему:\nhttps://t.me/elis_gallery_bot')

async def working_time_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Работает круглый сутки! Приходите все!')

async def destination_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Blumenstrasse, 13!', reply_markup=ReplyKeyboardRemove())

async def gallery_menu_command(message : types.Message):
    await sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(working_time_command, commands=['working_time'])
    dp.register_message_handler(destination_command, commands=['destination'])
    dp.register_message_handler(gallery_menu_command, commands=['gallery'])