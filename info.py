#Creadits Ivvakapothe Nee Kutha Paguludhi Owner
import re
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '20389440'))
API_HASH = environ.get('API_HASH', 'a1a06a18eb9153e9dbd447cfd5da2457')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', 'True'))

PICS = environ.get('PICS', '').split()
NOR_IMG = environ.get("NOR_IMG", "")
MELCOW_VID = environ.get("MELCOW_VID", "")
SPELL_IMG = environ.get("SPELL_IMG", "")

# Admins, Channels & Users
ADMINS = [int(admin) for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = auth_users + ADMINS if auth_users else []
PREMIUM_USER = [int(user) for user in environ.get('PREMIUM_USER', '').split()]
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', ''))
AUTH_GROUPS = [int(ch) for ch in environ.get('AUTH_GROUP', '').split()]
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', ''))
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', ''))
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", 'False'))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', '')

# Premium And Referal Settings
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '1'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
PAYMENT_QR = environ.get('PAYMENT_QR', '')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '')

# Others
VERIFY = is_enabled(environ.get('VERIFY', 'False'))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', 'False'))
DELETE_CHANNELS = [int(dch) for dch in environ.get('DELETE_CHANNELS', '').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
TUTORIAL = environ.get('TUTORIAL', '')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', 'True'))
MSG_ALRT = environ.get('MSG_ALRT', '')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', 'False'), False)
IMDB = is_enabled(environ.get('IMDB', 'True'), True)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', 'True'), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', 'True'), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', 'True'), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", 'False'), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", 'True'), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", "")
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '').split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', 'True'), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', 'False'), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', 'True'), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1", "season 2", "season 3", "season 4", "season 5", "season 6", "season 7", "season 8", "season 9", "season 10"]

ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME')
HAS_SSL = bool(getenv('HAS_SSL', False))
if HAS_SSL:
    URL = f"https://{APP_NAME}.herokuapp.com/"
else:
    URL = f"http://{APP_NAME
                    
