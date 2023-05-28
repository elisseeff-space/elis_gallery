import logging
from create_bot import dp#, bot
from sqlite_db import sql_start
from aiogram.utils import executor
from client import register_handlers_client
from admin import register_handlers_admin
from other import register_handlers_other
import json
#from datetime import datetime

register_handlers_client(dp)
register_handlers_admin(dp)
register_handlers_other(dp)


#openai.api_key = config['openai']
file = open('/home/pavel/cfg/config.json', 'r')
config = json.load(file)

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    #level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename="/home/pavel/github/elis_gallery/log/galery_bot.log"
)
#now = datetime.now()

async def on_startup(_):
    logger.warning(f"Elisseeff Gallery Bot logging is ON!")
    sql_start()
#    await bot.set_webhook(config['WEB_HOOK_URL'])

#async def on_shutdown(_):
#    print('Gallery Bot off!')
#    await bot.delete_webhook()

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    except (KeyboardInterrupt, SystemExit):
        pass