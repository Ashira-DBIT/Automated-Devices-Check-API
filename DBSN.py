import subprocess
import platform
import json
import urllib.request
import time
import os
from dotenv import load_dotenv

# 1. Load Environment Variables (Security Best Practice)
load_dotenv()
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")

# 2. Configuration
CHECK_INTERVAL = 300  # Seconds
DEVICES_TO_MONITOR = {
    "Google DNS": "8.8.8.8",
    "My Laptop": "127.0.0.1",
    "CCTV Camera": "1.1.1.2"
}

def send_line_notification(message_text):
    """Sends notification via LINE Messaging API"""
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    payload = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message_text}]
    }
    
    encoded_data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=encoded_data, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            return response.getcode()
    except Exception as error:
        print(f"❌ Notification Error: {error}")

def ping_device(ip_address):
    """Checks device status using ping"""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        subprocess.check_output(["ping", param, "1", ip_address], stderr=subprocess.STDOUT, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

# 3. Main Execution Loop
if __name__ == "__main__":
    print(f"--- 🛡️ Drawbridge Sentinel (DBSN) Started ---")
    
    try:
        while True:
            timestamp = time.strftime("%H:%M:%S")
            print(f"\n[Cycle Time: {timestamp}]")
            
            for name, ip in DEVICES_TO_MONITOR.items():
                is_alive = ping_device(ip)
                
                if not is_alive:
                    print(f"❌ {name} ({ip}) is OFFLINE")
                    # แจ้งเตือนเป็นภาษาไทยเพื่อให้เข้ากับกลุ่มลูกค้าหลัก
                    alert = f"⚠ [DBSN Alert]\nเวลา: {timestamp}\nพบปัญหา: {name} ขาดการติดต่อ!"
                    send_line_notification(alert)
                else:
                    print(f"✅ {name} is Normal")
            
            print(f"💤 Waiting for next scan in {CHECK_INTERVAL}s...")
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n🛑 System terminated by user.")