import os
from dotenv import load_dotenv

load_dotenv()


CANVAS_BASE_URL = "https://csusm.instructure.com"
CANVAS_API_TOKEN = os.getenv("CANVAS_API_TOKEN")

if not CANVAS_API_TOKEN:
    raise RuntimeError("CANVAS_API_TOKEN not set")
