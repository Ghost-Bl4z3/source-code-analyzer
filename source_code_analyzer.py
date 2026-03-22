import argparse
import re
import time
import os

ip_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b|\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b|\b(?:[A-Fa-f0-9]{1,4}:){1,7}:[A-Fa-f0-9]{1,4}\b|\b(?:[A-Fa-f0-9]{1,4}:){1,6}:(?:[A-Fa-f0-9]{1,4}:){0,5}[A-Fa-f0-9]{1,4}\b|\b::(?:[A-Fa-f0-9]{1,4}:){0,6}[A-Fa-f0-9]{1,4}\b|\b[A-Fa-f0-9]{1,4}::\b"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
url_pattern = r"https?://[^\s\"']+"
Js_pattern = r"<script[^>]+src=[\"'](.*?\.js)[\"']"

print()
print('THANK YOU FOR USING SOURCE_CODE_ANALYZER!!!!')
time.sleep(0.1)
print()

def extract_ips(data):
    set()
    print()
    return set(re.findall(ip_pattern, data))
    
def extract_emails(data):
    set()
    return set(re.findall(email_pattern, data))
        
def extract_urls(data):
    set()
    return set(re.findall(url_pattern, data))

def extract_Js(data):
    set()
    return set(re.findall(Js_pattern, data))

def extract_keywords(data, words):
    matches = set()

    for word in words:
         word = word.strip()

         if not word:
            continue
         
         pattern = rf"{word}[^\s\"']*"

         results = re.findall(pattern, data)

         for r in results:
          matches.add(r)

    return matches   
    

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', required=True, help='File Containing The Source Code')
    parser.add_argument('-w', '--wordlist',   help='Words To Look For In The Source Code')
    parser.add_argument('-i', '--internal',   action='store_true', help='Uses internal Wordlist')

    args = parser.parse_args()

    base_dir = os.path.dirname(__file__)
    internal_path = os.path.join(base_dir, "wordlist", "ghost.txt")

    if args.file:
     with open(args.file, 'r') as f:
        data = f.read()

    if args.wordlist and args.internal:
     print("PLEASE USE ONE, EITHER -w or -i, not both")
     print()
     exit()

    if args.wordlist:
       with open(args.wordlist, 'r') as f:
          words = f.readlines()

    elif args.internal:
       with open(internal_path, "r") as f:
          words = f.readlines()

    else:
       words = []

    if words:
       keywords = extract_keywords(data, words)
       print(f'\n[KEYWORDS FOUND - {len(keywords)}]')
       for k in sorted(keywords):
          print(k)       
                    
    ips = extract_ips(data)
    print()
    print(f'IPS FOUND: {len(ips)}')
    for ip in ips:
       print(ip)
     
     
    emails = extract_emails(data)
    print()
    print(f'EMAILS FOUND: {len(emails)}')
    for email in emails:
       print(email)   
            
    urls = extract_urls(data)
    print()
    print(f'URLS FOUND: {len(urls)}')
    for url in urls:
     print(url)

    js = extract_Js(data)
    print()
    print(f'JS FILES FOUND: {len(js)}')
    for j in js:
     print(j)
    print()

if __name__ == "__main__":
    main()

        

    