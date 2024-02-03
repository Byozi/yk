from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://i0.wp.com/newartistmodel.com/wp-content/uploads/2015/10/Stocksy_txp9e766c1dowe000_Medium_473661.jpg")
START_IMG = getenv("START_IMG", "https://i0.wp.com/newartistmodel.com/wp-content/uploads/2015/10/Stocksy_txp9e766c1dowe000_Medium_473661.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/scrable")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/scrable")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "seramusicbot")  

FAILED = "https://i0.wp.com/newartistmodel.com/wp-content/uploads/2015/10/Stocksy_txp9e766c1dowe000_Medium_473661.jpg"
