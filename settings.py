"""Настройки для PetFriends API"""

import os
from dotenv import load_dotenv

load_dotenv()

VALID_EMAIL = os.getenv("EMAIL")
VALID_PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL", "https://petfriends.skillfactory.ru/")