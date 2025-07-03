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
        print(f"\nChecking: {url}\n{'-'*50}")
        headers = response.headers

        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"[+] {header}: {headers[header]}")
            else:
                print(f"[-] {header} MISSING ❌")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target = input("Enter website URL (e.g. https://example.com): ")
    check_security_headers(target)
