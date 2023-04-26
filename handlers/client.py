from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Guten Appetit!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через личку. Напишите ему:\nhttps://t.me/elis_gallery_bot')

async def working_time_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Работает круглый сутки! Приходите все!')

async def destination_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Blumenstrasse, 13!', reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(working_time_command, commands=['working_time', 'help'])
    dp.register_message_handler(destination_command, commands=['destination', 'help'])