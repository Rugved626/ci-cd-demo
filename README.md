# 🚀 CI AI Monitor – Agentic DevOps System

An AI-powered CI/CD monitoring platform that automatically analyzes build failures, creates GitHub issues, and displays live reports on a dashboard.

This project simulates how modern engineering teams can use **Agentic AI** to manage and debug software pipelines autonomously.

---

## 🧠 What this system does

Whenever code is pushed to GitHub:

1. GitHub Actions runs automated tests  
2. If tests fail:
   - An AI agent reads CI logs  
   - Explains the error in natural language  
   - Creates a GitHub Issue automatically  
   - Sends the failure to the dashboard  
3. If tests pass:
   - The code is deployed automatically  

---

## 🖥 Dashboard Features

- Total CI failures  
- Last failure reason  
- Recent AI-generated debugging reports  
- Clean SaaS-style UI  

---

## 🧩 Tech Stack

- GitHub Actions (CI/CD)  
- OpenRouter (LLM for AI reasoning)  
- Python  
- Flask  
- SQLite  
- GitHub REST API  
- HTML + CSS  

---

## 🏗 Architecture

```
Developer Push
     ↓
GitHub Actions
     ↓
Tests
     ↓
AI Agent (OpenRouter)
     ↓
GitHub Issue + Dashboard API
     ↓
Flask + SQLite
     ↓
CI AI Monitor UI
```

---

## 🚀 Why this matters

Most CI systems only show logs.  
This system **understands** them.

It demonstrates how AI agents can:
- Perform root-cause analysis  
- Write human-readable bug reports  
- Automate DevOps workflows  

---

## 🧪 How to Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:
```
http://127.0.0.1:5000
```

---

## 🔥 Future Plans

- Slack & email alerts  
- Multi-repo monitoring  
- Production deployment  
- Predictive failure detection  

---

Built with ❤️ to explore the future of **Agentic AI + DevOps**
