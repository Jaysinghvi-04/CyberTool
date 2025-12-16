import socket
from colorama import Fore, init # type: ignore

init(autoreset=True)

def run_port_scan():
    target = input("\n[*] Enter Target IP (e.g., 127.0.0.1 or google.com): ").strip()
    
    # Remove http:// if user typed it by mistake
    target = target.replace("http://", "").replace("https://", "").split("/")[0]

    print(f"\n{Fore.CYAN}--- Starting Port Scan on {target} ---")
    print(f"{Fore.YELLOW}[*] Scanning top common ports (This may take a moment)...")

    # Common ports to check
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 
        3306, 3389, 8080, 8000
    ]

    open_ports = []

    for port in common_ports:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 1 second timeout so we don't wait forever
            s.settimeout(1)
            
            # Try to connect
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"{Fore.GREEN}[+] Port {port} is OPEN")
                open_ports.append(port)
            else:
                # Uncomment the line below if you want to see closed ports
                # print(f"{Fore.RED}[-] Port {port} is Closed")
                pass
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Exiting scan...")
            break
        except socket.gaierror:
            print("\n[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("\n[!] Could not connect to server.")
            break

    print(f"\n{Fore.CYAN}--- Scan Complete ---")
    if open_ports:
        print(f"Open Ports: {open_ports}")
    else:
        print("No common open ports found.")