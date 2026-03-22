# Source Code Analyzer 🔍

A simple python tool for analyzing web source code and extracting useful recon data

## 🚀 Features

- Extracts URLS
- Extracts Javascript Files
- Extracts Ip Addresses
- Extracts Emails
- Extracts interesting endpoints using:
  -Custom wordlist
  -internal wordlist

# ☠️ Usage

### Analyze a file
- python Source_Code_Analyzer.py -f sample-source.html

## Use Internal Wordlist
- python Source_Code_Analyzer.py -f sample-source.html -i

## Use Custom Wordlist
- python Source_Code_Analyzer.py -f sample-source.html -w wordlist.txt

## Example Output

[KEYWORDS FOUND - 24]
/.env
/admin
/admin/stats/overview
/api/backup
...


IPS FOUND: 3
192.168.1.105
10.0.0.23
172.16.4.88

EMAILS FOUND: 7
press@acmecorp.io
john@acmecorp.io
...

URLS FOUND: 13
https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
http://172.16.4.88:5432
https://js.stripe.com/v3/
...


JS FILES FOUND: 12
/static/js/app.js
/static/js/auth.js
...

## ⚠️ DISCLAIMER
This tool is intended for educational purposes and authorized security testing only

## 👻 Author
-Gh0$t_Bl4z3
