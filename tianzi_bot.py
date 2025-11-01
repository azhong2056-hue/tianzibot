# -*- coding: utf-8 -*-
import logging, requests
from datetime import datetime
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters

BOT_TOKEN      = "8249732366:AAERXVI64jS8LTFr79Wr0WVL9CEYVRRTgFg"
BOT_USERNAME   = "tzgj_bot"
ADMIN_GROUP_ID = 3234203217

OFFICIAL_SITE_TEXT = "0597.com"
OFFICIAL_SITE_URL  = "https://0597vip3.com"
GAME_SHORT_NAME    = "tzyl"

WELCOME_IMAGE  = "https://t.me/tztz/26"
PROMO_IMAGE    = "https://t.me/tztz/13"
DOWNLOAD_IMAGE = "https://t.me/tztz/18"
INVITE_IMAGE   = "https://t.me/tztz/81"

IOS_URL     = "https://hj-hashgo.s3.ap-southeast-1.amazonaws.com/99999999/app/tz0597.mobileconfig"
ANDROID_URL = "https://d179n5kbhqvh4f.cloudfront.net/sw2xs-ik5tg.apk"
SUPPORT_URL = "https://t.me/tzkf"
CHANNEL_URL = "https://t.me/tztz"

API_GET_INVITE = "https://h5.usdt-prod.com/finance-api/user/getInviteCode"

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("tianzibot")

STATE = {}

# ...（此处省略原始大段代码，为节省空间）
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("✅ 天子机器人已启动！")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Tianzibot is running!"

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 🔹 在主程序开始前调用它
if __name__ == "__main__":
    keep_alive()

    # 你的 Telegram 机器人启动逻辑
    from telegram.ext import ApplicationBuilder
    import logging

    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(os.environ["TOKEN"]).build()
    print("✅ TianziBot is running on Render...")
    app.run_polling()
