# bot.py
import time
import random
import requests

# 🔹 Dán token bot của bạn vào dòng dưới (thay YOUR_TOKEN_HERE)
TOKEN = "8274924758:AAEejL6RfRWjT_HbEfMMRbHTbQuvOyBTPxc"
# 🔹 Chat ID của bạn
CHAT_ID = "6794824681"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": "💵 Nhận Miễn Phí"}
    try:
        response = requests.post(url, data=data)
        print("Message sent:", response.text)
    except Exception as e:
        print("Error:", e)

while True:
    send_message()
    sleep_time = random.randint(600, 900)  # 10–15 phút
    print(f"Sleeping for {sleep_time // 60} minutes...")
    time.sleep(sleep_time)