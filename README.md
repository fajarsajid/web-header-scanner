# 🔐 Web Security Header Scanner

A simple Python tool to scan a website for missing or misconfigured **security headers**.

## 🚀 What It Does

This tool checks if the following HTTP security headers are present in a site's response:

- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`

These headers help protect against:

✅ Clickjacking  
✅ MIME-type sniffing  
✅ Cross-origin leaks  
✅ Man-in-the-middle attacks

## 🛠️ Built With

- Python 3
- `requests` (for HTTP requests)

## 💻 How to Use

1. Install dependencies:

```bash
pip install -r requirements.txt
```
2. Run the scanner:
```bash
python header_scanner.py
or
python3 header_scanner.py --url https://github.com
```
3. Enter a website URL (e.g., https://example.com) and view results.

## 🧪 Example Output
Checking: https://example.com
--------------------------------------------------
[+] Content-Security-Policy: default-src 'self'
[-] Permissions-Policy MISSING ❌
[+] X-Frame-Options: SAMEORIGIN
...

## 📂 File Structure
web-header-scanner/
├── header_scanner.py      # Main scanner script
├── requirements.txt       # Python dependencies
├── .gitignore             # Files to ignore in repo
├── LICENSE                # MIT License
└── README.md              # This file

## 👨‍💻 Author
Fajar Sajid
Cybersecurity & Python Enthusiast
GitHub Profile

