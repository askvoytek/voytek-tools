import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3:mini"

def ask_klaudiusz(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": "You are Klaudiusz, a helpful AI assistant built by Voytek Kopcewicz in Atlanta, Georgia. You run locally on a Raspberry Pi 5. You are named after Claude AI in Polish. You are knowledgeable about technology, Linux, Docker, Python, cryptocurrency, and home lab setups. Keep responses concise and friendly.",
        "stream": False
    }
    try:
        print("\n🤖 Klaudiusz is thinking...\n")
        response = requests.post(OLLAMA_URL, json=payload, timeout=300)
        data = response.json()
        return data.get("response", "No response received")
    except Exception as e:
        return f"Error: {e}"

print("=" * 50)
print("🤖  KLAUDIUSZ — Your Local AI Assistant")
print("    Powered by Mistral on Raspberry Pi")
print("=" * 50)
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("\nKlaudiusz: Do widzenia! 🇵🇱\n")
        break
    if not user_input:
        continue
    response = ask_klaudiusz(user_input)
    print(f"\nKlaudiusz: {response}\n")
