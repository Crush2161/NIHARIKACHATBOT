from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "27041759"
# -------------------------------------------------------------
API_HASH = "1851b8697ae0cfc06958257c55c44292"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7884638799"))
SUPPORT_GRP = "Crush_Forever_Support"
UPDATE_CHNL = "Crush_Forever"
OWNER_USERNAME = "Forever_Crush"
