import sys
import os

from hash_cracker import run_hash_cracker

# --- IMPORT ALL MODULES ---
try:
    from key_monitor import on_press, on_release
    from pynput.keyboard import Listener # type: ignore
    from web_scanner import run_web_scan
    from vuln_scanner import run_vuln_scan
    from port_scanner import run_port_scan
    from sys_info import run_sys_info       # <--- NEW

except ImportError as e:
    print(f"CRITICAL ERROR: Missing Module. {e}")
    print("Did you run 'pip install -r requirements.txt'?")
    sys.exit()

def start_keylogger_mode():
    print("\n[*] Keylogger initialized.")
    print("[*] Logs will be saved to the 'logs' folder.")
    print("[*] Press 'Esc' to stop execution.")
    
    import logging
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        filename=os.path.join(log_dir, "key_log.txt"),
        level=logging.DEBUG,
        format='%(asctime)s: %(message)s',
        force=True
    )

    with Listener(on_press=on_press, on_release=on_release) as listener: # type: ignore
        listener.join()

def main():
    while True:
        print("\n" + "="*45)
        print("   PYTHON SECURITY SWISS ARMY KNIFE")
        print("="*45)
        print("1. System: Keylogger (Monitor Inputs)")
        print("2. System: Information Gatherer (OS/Network)") # NEW
        print("3. Web: Directory Scanner (Hidden Files)")
        print("4. Web: Vulnerability Scanner (SQLi/XSS)")
        print("5. Network: Port Scanner (Open Ports)")
        print("6. Crypto: MD5 Hash Cracker")                  # NEW
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")

        if choice == '1':
            start_keylogger_mode()
        elif choice == '2':
            run_sys_info()
        elif choice == '3':
            run_web_scan()
        elif choice == '4':
            run_vuln_scan()
        elif choice == '5':
            run_port_scan()
        elif choice == '6':
            run_hash_cracker()
        elif choice == '7':
            print("Exiting Toolkit. Stay Safe!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()