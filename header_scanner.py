import argparse
import requests

SECURITY_HEADERS = {
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
}

def check_security_headers(url):
    try:
        response = requests.get(url)
        print(f"\n🔍 Checking: {url}\n{'-'*50}")
        headers = response.headers

        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"[+] {header}: {headers[header]}")
            else:
                print(f"[-] {header} MISSING ❌")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to {url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a website for missing HTTP security headers.")
    parser.add_argument("--url", help="Website URL (e.g., https://example.com)")
    args = parser.parse_args()

    if args.url:
        target_url = args.url
    else:
        target_url = input("Enter website URL (e.g., https://example.com): ")

    check_security_headers(target_url)
