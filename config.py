import os
import ProxyCloud

#Bot Config
BOT_TOKEN = os.environ.get('bot_token','5696924720:AAEv8i9dPG_GS4VIvTNTd_5QixIh8CZGFAM')
#Storage Config
BASE_ROOT_PATH = 'root/'
#Account Config
OWN_USER = os.environ.get('account_user','aosorio')
OWN_PASSWORD = os.environ.get('account_password','Mayelin96-*/')
# Proxy Config
PROXY_OBJ = ProxyCloud.parse(os.environ.get('proxy_enc','http://KGGIJIYIJILIFIYIDIGIYIJIHICIRIDILIDILI'))
# Sync Options
SPLIT_SYNC = 1024 * 1024 * int(os.environ.get('split_sync',10))
UPLOAD_SYNC = 3
