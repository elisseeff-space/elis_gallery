# elis_gallery
elis_gallery telegram bot

virtualenv venv
source venv/bin/activate

export PYTHONPATH="/home/pavel/github/AudioTelega"

# Start the bot
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass
        
Serverless Yandex DB

ydb config profile update elis-db-profile --sa-key-file .\cfg\elis-sa-key-file.json
ydb config profile get elis-db-profile

endpoint: grpcs://ydb.serverless.yandexcloud.net:2135
database: /ru-central1/b1gc56a5qpgnma6uuce7/etndqq2oc8du160nbqc0
sa-key-file: .\cfg\elis-sa-key-file.json

ydb -v --profile elis-db-profile scheme ls

ydb -v --profile elis-db-profile yql --script "SELECT * FROM episodes;"

chcp 65001
python -m pip install iso8601

"""
executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=config['APP_PORT'],
        )
"""
