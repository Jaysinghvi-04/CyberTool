import requests # type: ignore
from colorama import Fore, Style, init # type: ignore
from urllib.parse import urlparse, urljoin

init(autoreset=True)

# Fake a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def check_sql_injection(url):
    print(f"\n{Fore.CYAN}[*] Testing for SQL Injection (SQLi)...")
    
    # If URL has no parameters (like ?id=1), warn the user but try anyway
    if "?" not in url:
        print(f"{Fore.YELLOW}[!] Note: Target has no parameters (e.g., ?id=1). SQLi test may not work effectively.")
    
    payload = "'"
    # LOGIC FIX: Ensure we don't break the domain name
    if "?" in url:
        target_url = f"{url}{payload}" # Append to parameter
    else:
        # If it's just a domain, add a slash first so we test the path, not the domain
        if not url.endswith("/"):
            target_url = f"{url}/{payload}" 
        else:
            target_url = f"{url}{payload}"

    try:
        res = requests.get(target_url, headers=HEADERS, timeout=10)
        errors = ["syntax error", "mysql_fetch", "You have an error in your SQL syntax"]
        
        if any(error in res.text for error in errors):
            print(f"{Fore.RED}[!!!] VULNERABILITY FOUND: SQL Injection detected!")
        else:
            print(f"{Fore.GREEN}[+] No obvious SQL errors found.")
    except Exception as e:
        print(f"{Fore.RED}[!] Connection failed: {e}")

def check_xss(url):
    print(f"\n{Fore.CYAN}[*] Testing for Cross-Site Scripting (XSS)...")
    
    payload = "<script>alert('XSS')</script>"
    
    # LOGIC FIX: Same protection for XSS
    if "?" in url:
        target_url = f"{url}{payload}"
    else:
        if not url.endswith("/"):
            target_url = f"{url}/{payload}"
        else:
            target_url = f"{url}{payload}"
            
    try:
        res = requests.get(target_url, headers=HEADERS, timeout=10)
        if payload in res.text:
            print(f"{Fore.RED}[!!!] VULNERABILITY FOUND: Reflected XSS detected!")
        else:
            print(f"{Fore.GREEN}[+] No basic XSS reflection found.")
    except Exception as e:
        print(f"{Fore.RED}[!] Connection failed: {e}")

def scan_backdoors(url):
    print(f"\n{Fore.CYAN}[*] Scanning for Backdoors (Web Shells)...")
    backdoors = ["shell.php", "c99.php", "b374k.php", "wso.php", "wp-config.php.bak"]
    
    # Ensure base URL ends with slash for joining
    if not url.endswith("/"):
        base_url = url + "/"
    else:
        base_url = url

    found = False
    for page in backdoors:
        target_path = base_url + page
        try:
            res = requests.get(target_path, headers=HEADERS, timeout=5)
            if res.status_code == 200:
                print(f"{Fore.RED}[!!!] POTENTIAL BACKDOOR FOUND: {target_path}")
                found = True
        except:
            pass
            
    if not found:
        print(f"{Fore.GREEN}[+] No common backdoors found.")

def run_vuln_scan():
    target = input("\n[*] Enter Target URL: ").strip()
    
    if not target.startswith("http"):
        target = "https://" + target

    print(f"\n--- Starting Vulnerability Scan on {target} ---")
    
    check_sql_injection(target)
    check_xss(target)
    
    # Clean URL for backdoor scan (remove parameters)
    clean_url = target.split('?')[0]
    scan_backdoors(clean_url)
    
    print("\n--- Scan Complete ---")