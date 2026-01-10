import os
import requests  # Add to requirements if live

GROK_API_KEY = os.getenv("GROK_API_KEY")  # Secure env

def query_grok_api(prompt):
    if not GROK_API_KEY:
        return "Sim fallback: Mercy harmony response"  # Offline grace
    headers = {"Authorization": f"Bearer {GROK_API_KEY}"}
    data = {"model": "grok-4", "messages": [{"role": "user", "content": prompt}]}
    response = requests.post("https://api.x.ai/v1/chat/completions", json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"] if response.ok else "API grace fallback"

# Use in forks: e.g., GamingForge position = query_grok_api("Strategic view on proposal...")
