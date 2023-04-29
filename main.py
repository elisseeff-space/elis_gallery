import logging
from create_bot import dp, on_startup, on_shutdown
#from data_base import sqllite_db
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
logging.warning("Elisseeff Gallery Bot logging is ON!")

#async def on_startup(_):
#    print('Gallery Bot online!')
#    sqllite_db.sql_start()

#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=8343,
        )