import tkinter as tk
import platform
import socket
import psutil # type: ignore

# --- LOGIC FUNCTIONS ---
def get_system_info():
    try:
        uname = platform.uname()
        os_info = f"{uname.system} {uname.release}"
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        cpu = f"{psutil.cpu_percent()}%"
        ram = f"{psutil.virtual_memory().percent}%"
        return os_info, ip_addr, cpu, ram
    except Exception:
        return "Error", "Error", "Error", "Error"

# --- GUI ACTION ---
def show_info():
    os_text, ip_text, cpu_text, ram_text = get_system_info()
    lbl_os_res.config(text=os_text, fg="#00ff00")
    lbl_ip_res.config(text=ip_text, fg="#00ff00")
    lbl_cpu_res.config(text=cpu_text)
    lbl_ram_res.config(text=ram_text)

# --- SETUP WINDOW ---
root = tk.Tk()
root.title("Security Tool GUI")
root.geometry("400x300")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="System Monitor", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

# Frame for details
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

def create_row(txt):
    row = tk.Frame(frame, bg="#1e1e1e")
    row.pack(fill="x", pady=2)
    tk.Label(row, text=txt, width=15, anchor="w", bg="#1e1e1e", fg="white").pack(side="left")
    res = tk.Label(row, text="---", width=20, anchor="w", bg="#1e1e1e", fg="gray")
    res.pack(side="left")
    return res

lbl_os_res = create_row("OS Version:")
lbl_ip_res = create_row("IP Address:")
lbl_cpu_res = create_row("CPU Usage:")
lbl_ram_res = create_row("RAM Usage:")

# Button
tk.Button(root, text="SCAN NOW", command=show_info, bg="gray", fg="black", font=("Arial", 10, "bold")).pack(pady=20)

# --- CRITICAL LINE: KEEPS WINDOW OPEN ---
root.mainloop()