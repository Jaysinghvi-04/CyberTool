import platform
import socket
import psutil # type: ignore
from colorama import Fore, init # type: ignore

init(autoreset=True)

def run_sys_info():
    print(f"\n{Fore.CYAN}--- System Information Gatherer ---")
    
    # 1. OS Details
    print(f"{Fore.YELLOW}[*] Gathering OS Details...")
    uname = platform.uname()
    print(f"    System:   {uname.system}")
    print(f"    Node:     {uname.node}")
    print(f"    Release:  {uname.release}")
    print(f"    Version:  {uname.version}")
    print(f"    Machine:  {uname.machine}")

    # 2. IP Information
    print(f"\n{Fore.YELLOW}[*] Gathering Network Info...")
    hostname = socket.gethostname()
    try:
        ip_addr = socket.gethostbyname(hostname)
    except:
        ip_addr = "Could not resolve"
    print(f"    Hostname: {hostname}")
    print(f"    Local IP: {ip_addr}")

    # 3. CPU/RAM Usage
    print(f"\n{Fore.YELLOW}[*] Hardware Usage...")
    print(f"    CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"    RAM Usage: {psutil.virtual_memory().percent}%")

    print(f"\n{Fore.CYAN}--- Info Complete ---")