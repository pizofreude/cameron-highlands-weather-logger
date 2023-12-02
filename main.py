# import necessary libraries
import logging
import logging.handlers
import os

import requests

# initiate logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# error handling
try:
    CHWL_SECRET = os.environ["CHWL_SECRET"]
except KeyError:
    CHWL_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {CHWL_SECRET}")

    # request weather data for Cameron Highlands, Tanah Rata, Pahang, MY
    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Tanah%20Rata&country=MY')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Cameron Highlands: {temperature}')