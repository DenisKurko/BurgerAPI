from dotenv import find_dotenv, load_dotenv
import os


DOTENV_PATH = find_dotenv()
load_dotenv(dotenv_path=DOTENV_PATH)


REQUEST_HEADERS = os.getenv("REQUEST_HEADERS", "")

FULLMENU_URL = os.getenv("FULLMENU_URL", "")
PRODUCT_URL = os.getenv("PRODUCT_URL", "")

HOST = os.getenv("host", "127.0.0.1")