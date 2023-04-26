import logging
from create_bot import dp

from aiogram.utils import executor

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


#openai.api_key = config['openai']

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    filename="galery_bot.log",
)
logging.warning("Elisseeff Audio Bot logging is ON!")

async def on_startup(_):
    print('Gallery Bot online!')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)