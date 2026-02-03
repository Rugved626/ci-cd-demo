import os
import requests

OPENROUTER = os.environ["OPENROUTER_API_KEY"]
GH = os.environ["GH_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]

CI_LOG = os.environ.get("CI_LOG", "No CI logs")

# 1️⃣ Ask AI to analyze the failure
prompt = f"""
You are a senior DevOps engineer.
Explain this CI failure and suggest a fix.

{CI_LOG}
"""

ai = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "CI Debug Agent"
    },
    json={
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
).json()

report = ai["choices"][0]["message"]["content"]

print("\n🤖 AI REPORT:\n", report)

# 2️⃣ Create GitHub Issue
requests.post(
    f"https://api.github.com/repos/{REPO}/issues",
    headers={
        "Authorization": f"Bearer {GH}",
        "Accept": "application/vnd.github+json"
    },
    json={
        "title": "🚨 CI Failure Detected",
        "body": report
    }
)

# 3️⃣ Send failure to your Flask dashboard
DASHBOARD_URL = "https://YOUR_NGROK_URL/api/failure"   # ⬅️ change this

requests.post(
    DASHBOARD_URL,
    json={"message": report}
)
