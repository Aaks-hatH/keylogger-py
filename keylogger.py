import json
import urllib.request
from datetime import datetime
from pynput.keyboard import Key, Listener

WEBHOOK_URL = "https://discord.com/api/webhooks/1553030675525931033/AF3-QESHAxVtCd4e2g9WJX05tEHmBfr4QJU5DGFc38vy_4cpC_Kp8LY8cJxmXq3APAds"

ALLOWED_KEYS = {
    Key.esc,
    Key.up,
    Key.down,
    Key.left,
    Key.right,
}

def send_demo_event(key):
    payload = {
        "event": "keyboard_demo",
        "key": str(key),
        "timestamp": datetime.now().isoformat(),
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            print("Webhook response:", response.status)
    except Exception as e:
        print("Webhook error:", e)

def on_press(key):
    if key in ALLOWED_KEYS:
        send_demo_event(key)

    if key == Key.esc:
        return False

print("Safe keyboard webhook demo running.")
print("Press an arrow key to send a demo event.")
print("Press Escape to stop.")

with Listener(on_press=on_press) as listener:
    listener.join()
