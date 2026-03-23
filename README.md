# 🔍 Source Code Analyzer

> A Python reconnaissance tool for extracting security-relevant data from web source code — built for authorized penetration testing and bug bounty recon.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Purpose](https://img.shields.io/badge/Purpose-Security%20Research-red?style=flat-square)

---

## 📌 What It Does

During a web application pentest or bug bounty, analyzing page source code manually is slow and error-prone. Source Code Analyzer automates the recon phase by parsing HTML source and pulling out everything that matters — endpoints, scripts, addresses, and more — in seconds.

---

## ⚡ Features

| Feature | Description |
|---|---|
| 🔗 URL Extraction | Pulls all URLs embedded in the source |
| 📜 JavaScript Files | Lists all JS files referenced — great for further analysis |
| 🌐 IP Addresses | Extracts any hardcoded IP addresses |
| 📧 Email Addresses | Finds emails left in source code |
| 🗺️ Endpoint Discovery | Finds interesting/hidden endpoints using wordlist matching |
| 📂 Custom Wordlists | Bring your own wordlist for targeted endpoint hunting |
| 🧠 Internal Wordlist | Built-in wordlist for quick out-of-the-box recon |

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Ghost-Bl4z3/source-code-analyzer.git

# Navigate into the directory
cd source-code-analyzer

# No external dependencies required — runs on standard Python 3
python3 source_code_analyzer.py --help
```

---

## 🛠️ Usage

### Basic Analysis
```bash
python3 source_code_analyzer.py --file target.html
```

### Use Internal Wordlist (endpoint discovery)
```bash
python3 source_code_analyzer.py --file target.html --internal
```

### Use Custom Wordlist
```bash
python3 source_code_analyzer.py --file target.html --wordlist wordlist.txt
```

---

## 📸 Example Output

```
[*] Analyzing source file: target.html
[*] Running endpoint discovery with custom wordlist...

[+] URLs Found (14):
    → https://target.com/api/v1/users
    → https://target.com/static/main.js
    ...

[+] JavaScript Files (6):
    → /static/app.bundle.js
    → /vendor/jquery.min.js
    ...

[+] Interesting Endpoints (2):
    → /api/v1/admin
    → /internal/config

[+] Email Addresses (2):
    → admin@target.com

[+] IP Addresses (1):
    → 192.168.1.100
```

---

## 🧠 How It Fits Into a Recon Workflow

```
Target URL
    │
    ▼
Save page source (Ctrl+U / curl / wget)
    │
    ▼
Run source_code_analyzer.py
    │
    ├── Endpoints → Test for unauthorized access, IDOR
    ├── JS Files  → Analyze for hardcoded secrets, API keys
    ├── IPs       → Internal infrastructure exposure
    └── Emails    → OSINT / phishing simulation (authorized only)
```

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational purposes and authorized security testing only**.

Do not use this tool against systems you do not have explicit written permission to test. The author is not responsible for any misuse or damage caused by this tool. Always practice responsible disclosure.

---

## 🗺️ Roadmap

- [ ] Add support for analyzing live URLs directly (via requests)
- [ ] JSON/CSV output format
- [ ] Add secret/API key pattern detection
- [ ] Recursive JS file analysis

---

## 👻 Author

**Sphesihle Dwayisa** (Ghost-Bl4z3)
- GitHub: [@Ghost-Bl4z3](https://github.com/Ghost-Bl4z3)
- Portfolio: [ghost-bl4z3.github.io](https://ghost-bl4z3.github.io)

---

## 📄 License

MIT License — free to use, modify and distribute with attribution.
