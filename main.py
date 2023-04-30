import logging
from create_bot import dp, bot
from data_base import sqllite_db
from aiogram.utils import executor
from handlers import client, admin, other
import json
import telebot
import flask

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


#openai.api_key = config['openai']
file = open('config.json', 'r')
config = json.load(file)

logger = logging.getLogger(__name__)
logging.basicConfig(
    #level=logging.INFO,
    level=logging.DEBUG,
    filename="galery_bot.log",
)
logging.warning("Elisseeff Gallery Bot logging is ON!")

app = flask.Flask(__name__)
app.route( '/', methods=['POST'])

def webhook():
    if flask.request.headers.get('content_type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

async def on_startup(_):
    print('Gallery Bot online!')
    sqllite_db.sql_start()
    await bot.set_webhook(config['WEB_HOOK_URL'])

async def on_shutdown(_):
    print('Gallery Bot off!')
    await bot.delete_webhook()

#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=config['APP_PORT'],
        )