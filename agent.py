import os
import requests

log = os.environ.get("CI_LOG", "No CI logs found")

prompt = f"""
You are a senior DevOps engineer.
Explain the following CI failure in simple English and give a fix:

{log}
"""

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "CI Debug Agent"
    },
    json={
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
)

print("\n🤖 AI DEBUG REPORT:\n")
print(response.json()["choices"][0]["message"]["content"])
