import logging
import os
from dotenv import load_dotenv

load_dotenv()

log_level = os.getenv("LOG_LEVEL")
log_format = os.getenv("LOG_FORMAT")

logging.basicConfig(
    level=log_level,
    format=log_format,
    filename="bot.log",
    filemode = "w",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)