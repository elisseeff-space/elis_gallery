# elis_gallery
 elis_gallery telegram bot

 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
 .\venv\Scripts\activate

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
