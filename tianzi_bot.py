# -*- coding: utf-8 -*-
import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ================== Flask 保活部分 ==================
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ TianziBot is running on Render (keep-alive active)"

def run():
    """启动 Flask 保活线程"""
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    """启动独立线程保持服务运行"""
    t = Thread(target=run)
    t.daemon = True
    t.start()

# ================== 从环境变量读取配置 ==================
TOKEN = os.environ.get("TOKEN")  # Telegram Bot Token
OFFICIAL_SITE_URL = os.environ.get("OFFICIAL_SITE_URL", "https://example.com")
DOWNLOAD_IMAGE = os.environ.get("DOWNLOAD_IMAGE", "")
INVITE_IMAGE = os.environ.get("INVITE_IMAGE", "")
SUPPORT_URL = os.environ.get("SUPPORT_URL", "")
CHANNEL_URL = os.environ.get("CHANNEL_URL", "")
ADMIN_GROUP_ID = os.environ.get("ADMIN_GROUP_ID", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "tianzibot")

# ================== 日志配置 ==================
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("tianzibot")

# ================== 机器人功能 ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """启动命令"""
    await send_main_menu(update)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """菜单命令"""
    await send_main_menu(update)

async def send_main_menu(update: Update):
    """显示主菜单"""
    keyboard = [
        [InlineKeyboardButton("🌐 官方网站", url=OFFICIAL_SITE_URL)],
        [InlineKeyboardButton("📱 下载应用", url=DOWNLOAD_IMAGE)],
        [InlineKeyboardButton("🎁 邀请好友", url=INVITE_IMAGE)],
        [InlineKeyboardButton("💬 支持群", url=SUPPORT_URL)],
        [InlineKeyboardButton("📺 官方频道", url=CHANNEL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "✅ 欢迎使用 <b>天子机器人</b>！\n\n"
        "请从下方菜单中选择功能："
    )

    await update.message.reply_text(
        text, parse_mode="HTML", reply_markup=reply_markup
    )

# ================== 启动主程序 ==================
if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("❌ 未检测到 TOKEN 环境变量，请在 Render 环境中设置 TOKEN")

    keep_alive()

    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("menu", menu))

    print("✅ TianziBot 已启动并在 Render 上运行中...")
    app_bot.run_polling()
