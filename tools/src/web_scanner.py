import requests # type: ignore

def run_web_scan():
    target = input("\n[*] Enter Target URL (e.g., https://example.com): ").strip()
    
    # Ensure URL has schema
    if not target.startswith("http"):
        target = "https://" + target

    print(f"\n--- Scanning {target} ---")

    try:
        # 1. Check Server Headers
        response = requests.get(target, timeout=5)
        print(f"[+] Status: {response.status_code} OK")
        
        server = response.headers.get("Server", "Unknown")
        print(f"[+] Server Software: {server}")

        # 2. Check for Common Files (Enumeration)
        common_paths = ["robots.txt", "admin", "login", "sitemap.xml", ".env"]
        print("\n[*] Checking common paths...")
        
        for path in common_paths:
            full_url = f"{target}/{path}"
            res = requests.get(full_url, timeout=3)
            
            if res.status_code == 200:
                print(f"  [FOUND] {full_url} (200 OK)")
            elif res.status_code == 403:
                print(f"  [LOCKED] {full_url} (403 Forbidden)")
            else:
                # We usually ignore 404s to keep output clean
                pass

    except requests.exceptions.ConnectionError:
        print("[-] Error: Could not connect to target.")
    except Exception as e:
        print(f"[-] Error: {e}")

    print("\n--- Scan Complete ---")