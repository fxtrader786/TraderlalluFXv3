from config import TOKEN, TELEGRAM_ID, MAJOR_PAIRS
import time
import random
import requests

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_ID, "text": message}
    requests.post(url, data=data)

def generate_signal():
    pair = random.choice(MAJOR_PAIRS)
    signal = random.choice(["CALL", "PUT"])
    return pair, signal

while True:
    current_time = int(time.time())
    if current_time % 120 == 105:  # 15 seconds before 2-min mark
        pair, signal = generate_signal()
        send_telegram_message(f"🕒 Trade within next 15 seconds!
Pair: {pair}
Signal: {signal}")
    time.sleep(1)
