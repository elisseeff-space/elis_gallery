from aiogram import types, Dispatcher
from create_bot import dp, bot

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Guten Appetit!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через личку. Напишите ему:\nhttps://t.me/elis_gallery_bot')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])