import requests
from datetime import datetime

# Your lab services
services = [
    {"name": "voytek.ai",    "url": "https://voytek.ai"},
    {"name": "Portainer",    "url": "http://192.168.50.160:9000"},
    {"name": "Uptime Kuma",  "url": "http://192.168.50.160:3001"},
    {"name": "Homer",        "url": "http://192.168.50.160:8902"},
    {"name": "Open WebUI",   "url": "http://192.168.50.13:8080"},
    {"name": "Ollama",       "url": "http://localhost:11434/api/tags"},
]

def check_service(service):
    try:
        response = requests.get(service["url"], timeout=5)
        status = "✅ UP" if response.status_code < 400 else "❌ DOWN"
        ms = round(response.elapsed.total_seconds() * 1000)
        return f"{status}  {service['name']:<15} {ms}ms"
    except:
        return f"❌ DOWN  {service['name']:<15} unreachable"

print(f"\n🖥️  VOYTEK LAB MONITOR — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

for service in services:
    print(check_service(service))

print("=" * 50)
print("✅ = Online  ❌ = Offline\n")
