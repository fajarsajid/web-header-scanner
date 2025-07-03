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

