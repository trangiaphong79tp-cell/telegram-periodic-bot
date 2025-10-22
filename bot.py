# bot.py
"""
Telegram periodic sender (safe template).
SỬ DỤNG: Đặt TELEGRAM_TOKEN và CHAT_ID trong environment variables (Render secrets).
DO NOT hardcode your token in this file.
"""

import os
import time
import random
import requests
import logging
from datetime import datetime

# --- Config ---
TOKEN = os.getenv("8274924758:AAEejL6RfRWjT_HbEfMMRbHTbQuvOyBTPxc")   # e.g. "123456789:ABC..."
CHAT_ID = os.getenv("6794824681")        # e.g. "987654321"
MESSAGE = os.getenv("MESSAGE", "💵 Nhận Miễn Phí")  # optional override
MIN_DELAY = int(os.getenv("MIN_DELAY", 600))  # seconds; default 600 (10 min)
MAX_DELAY = int(os.getenv("MAX_DELAY", 900))  # seconds; default 900 (15 min)

# --- Logging ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

if not TOKEN or not CHAT_ID:
    logger.error("Missing TELEGRAM_TOKEN or CHAT_ID environment variables. Exiting.")
    raise SystemExit("Set TELEGRAM_TOKEN and CHAT_ID environment variables.")

SEND_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_message(text: str) -> bool:
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        resp = requests.post(SEND_URL, data=payload, timeout=15)
        if resp.status_code == 200:
            logger.info("Message sent successfully.")
            return True
        else:
            logger.warning("Failed to send message: %s %s", resp.status_code, resp.text)
            return False
    except requests.RequestException as e:
        logger.exception("RequestException when sending message: %s", e)
        return False

def main_loop():
    backoff = 1
    while True:
        now = datetime.utcnow().isoformat()
        logger.info("Attempt to send at %s", now)
        ok = send_message(MESSAGE)
        if ok:
            backoff = 1
        else:
            # simple exponential backoff on failure (capped)
            logger.info("Send failed; sleeping backoff %s seconds", backoff)
            time.sleep(backoff)
            backoff = min(backoff * 2, 300)

        # Random delay between MIN_DELAY and MAX_DELAY seconds
        delay = random.randint(MIN_DELAY, MAX_DELAY)
        logger.info("Sleeping %s seconds before next send.", delay)
        time.sleep(delay)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        logger.info("Interrupted by user; exiting.")
