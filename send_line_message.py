# send_line_message.py
import requests
from datetime import datetime
import pytz
import os

def send_line_message(user_id, message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.environ["0d1f711d93c98abe36f2de03a7cd3ad7"]}',
    }
    body = {
        "to": user_id,
        "messages": [{
            "type": "text",
            "text": message
        }]
    }
    res = requests.post(url, headers=headers, json=body)
    print(res.status_code, res.text)

if __name__ == "__main__":
    tz = pytz.timezone('Asia/Taipei')
    now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    msg = f"🌄 早安！今天是 {now}，祝你順心愉快！"
    send_line_message(os.environ["LINE_USER_ID"], msg)
