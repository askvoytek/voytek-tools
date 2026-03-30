# 🛠️ voytek-tools

A growing collection of Python scripts built for managing and monitoring my self-hosted home lab infrastructure.

## Scripts

### 🌐 check_voytek.py
Checks if voytek.ai is online and returns the response time.
```bash
python3 check_voytek.py
```

### 🖥️ lab_monitor.py
Monitors all home lab services at once — Portainer, Uptime Kuma, Homer, Open WebUI, Ollama, and voytek.ai. Displays status and response time for each.
```bash
python3 lab_monitor.py
```

### 🤖 klaudiusz.py
Klaudiusz v0.1 — a local AI assistant running on Mistral/Phi3 via Ollama on a Raspberry Pi 5. Named after Claude AI in Polish.
```bash
python3 klaudiusz.py
```

## Stack
- Python 3
- Raspberry Pi 5 (Ubuntu)
- Ollama (local AI inference)
- Docker

## Author
**Voytek Kopcewicz** — [voytek.ai](https://voytek.ai) | [GitHub](https://github.com/askvoytek)

*Built in Atlanta, GA 🍑*
