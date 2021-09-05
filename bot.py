import os

import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
