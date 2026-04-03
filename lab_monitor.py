import subprocess
import datetime

# Voytek Homelab Devices
from config import devices

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def check_lab():
    print(f"\n🏠 Voytek Homelab Status")
    print(f"🕐 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 45)
    for name, ip in devices.items():
        status = "✅ ONLINE " if ping(ip) else "❌ OFFLINE"
        print(f"  {status}  {name}  {ip}")
    print("-" * 45 + "\n")

check_lab()
