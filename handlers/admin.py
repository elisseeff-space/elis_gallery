from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

# Get Moderator Id 
# @dp.message_handler(commands=['Moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global idd
    idd = message.from_user.id
    await bot.send_message(message.from_user.id, 'What do you want Sir?') #, reply_markup=button_case_admin)
    await message.delete()


# Start Menu Load Dialog
# @dp.message_handler(commands='Load', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == idd:
        await FSMAdmin.photo.set()
        await message.reply('Pls load a photo')

# Go Out from States
# @dp.message_handler(state="*", commands='Cancel')
# @dp.message_handler(Text(equals='Cancel', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')
    
# Catch the first answer from user and write in Dictionary
# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == idd:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Now enter pls name')

# Catch the second answer
# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == idd:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Now enter The Description')

# Catch the third answer
# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == idd:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Now enter The Price')

# Catch the last answer
# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == idd:
        async with state.proxy() as data:
            data['price'] = float(message.text)
    
        async with state.proxy() as data:
            await message.reply(str(data))

        await state.finish()

# Handlers Registration
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands='Load', state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='Cancel')
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['Moderator'], is_chat_admin=True)