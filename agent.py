import requests
import os

GITHUB_REPO = "Rugved626/ci-cd-demo"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

def get_latest_run():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data["workflow_runs"][0]["id"]

def get_logs(run_id):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/actions/runs/{run_id}/logs"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    return r.text

def explain_error(logs):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"""
You are a DevOps AI agent.
Explain this CI failure and suggest fix:

{logs[:2000]}
"""
            }]
        }]
    }

    r = requests.post(url, json=payload)
    return r.json()["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    print("Fetching CI run...")
    run_id = get_latest_run()
    print("Run ID:", run_id)

    print("Fetching logs...")
    logs = get_logs(run_id)

    print("Sending to Gemini...")
    explanation = explain_error(logs)

    print("\n=== AI Explanation ===\n")
    print(explanation)
