# 🚀 k8s-pod-health-cli

A lightweight, production-ready CLI tool for analyzing the health of Kubernetes pods in any namespace.  
It detects problematic pods (CrashLoopBackOff, Pending, Error states), summarizes results in structured JSON, and supports both CLI usage and AI-agent integration.

Built for DevOps, SRE, and Platform Engineering teams who need fast insights and reliable troubleshooting automation.

---

## ✨ Features

- 🔍 Analyze all pods in a Kubernetes namespace  
- ⚠ Detect CrashLoopBackOff, Pending, ImagePull errors, and non-Running pod phases  
- 📊 Structured JSON output for automation, CI pipelines, and agent usage  
- 🧩 Works as a CLI and as a Python module  
- 🔌 Automatically loads kubeconfig or in-cluster configuration  
- 🧱 Modular architecture (CLI, Kubernetes client, health logic, formatting, agent tools)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/eliffkeskin/k8s-pod-health-cli.git
cd k8s-pod-health-cli
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

▶️ Usage
Basic usage
```bash
python -m pod_health.cli --namespace default
```

Example output:
```json
{
  "namespace": "default",
  "total_pods": 28,
  "unhealthy_count": 0,
  "unhealthy_pods": []
}
```

Check a specific namespace
```bash
python -m pod_health.cli --namespace myapp-prod
```

Pretty JSON output
```bash
python -m pod_health.cli --namespace shift-prod --pretty
```

🧠 Architecture Overview
```bash
src/
 └── pod_health
      ├── cli.py              # Main CLI entrypoint
      ├── k8s_client.py       # Kubernetes API configuration and client setup
      ├── health_checker.py   # Core pod health analysis logic
      ├── formatting.py       # JSON and human-readable formatting utilities
      └── agent/
           ├── tools.py       # Tool definition for AI agents (function-calling API)
           └── runner.py      # Tool execution engine for AI-driven workflows
```

🧩 Real-World Use Cases

    🛠 Quick troubleshooting during incidents

    🔁 Automated cluster validation in CI/CD pipelines

    🧪 Pre-check before load tests or deployments

    🧠 Backend tool for AI agents (OpenAI / function-calling compatible)

    📉 Early detection of unhealthy workloads

📌 Roadmap

    CrashLoopBackOff & Pending deep analyzer (with event inspection)

     Kubernetes event summary tool

     Real User HTTP Healthcheck runner

     AWS Lambda version

     Self-healing prototype (optional)

     GitHub Actions integration

📦 Release Management

This project follows Semantic Versioning:

MAJOR.MINOR.PATCH → for example: v0.1.0



🤝 Contributing

Contributions, improvements, and feature requests are welcome.
Feel free to open a PR or create an issue.

📄 License

MIT License
Free to use, modify, and distribute.

👤 Author

Elif Keskin
DevOps / Platform Engineer — Kubernetes, OpenShift, AWS, Cloud Security, Observability

GitHub: https://github.com/eliffkeskin  
LinkedIn: https://www.linkedin.com/in/eliffkeskin/

