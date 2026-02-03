import os
import requests

OPENROUTER = os.environ["OPENROUTER_API_KEY"]
GITHUB = os.environ["GH_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]

log = os.environ.get("CI_LOG", "No logs")

prompt = f"""
You are a DevOps engineer.
Explain this CI failure and write a short bug report.

{log}
"""

ai = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com",
        "X-Title": "CI Agent"
    },
    json={
        "model": "mistralai/mistral-7b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }
).json()

report = ai["choices"][0]["message"]["content"]

issue = requests.post(
    f"https://api.github.com/repos/{REPO}/issues",
    headers={
        "Authorization": f"Bearer {GITHUB}",
        "Accept": "application/vnd.github+json"
    },
    json={
        "title": "🚨 CI Failure Detected",
        "body": report
    }
)

print("Issue created:", issue.status_code)
