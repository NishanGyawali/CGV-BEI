import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
import os

# ===== Folder & Scripts =====
current_folder = os.path.dirname(os.path.abspath(__file__))
scripts = {}
for file in os.listdir(current_folder):
    if file.endswith(".py") and file != os.path.basename(__file__):
        display_name = file.rsplit(".py", 1)[0].replace("_", " ").title()
        scripts[display_name] = os.path.join(current_folder, file)

# ===== Function to run scripts =====
def run_script(script_name):
    script_file = scripts[script_name]
    if not os.path.exists(script_file):
        messagebox.showerror("Error", f"{script_file} not found!")
        return
    try:
        subprocess.run([sys.executable, script_file])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run {script_name}:\n{e}")

# ===== Hover effect for buttons =====
def on_enter(e):
    e.widget['background'] = '#444444'

def on_leave(e):
    e.widget['background'] = '#333333'

# ===== Main Window =====
root = tk.Tk()
root.title("Computer Graphics Project Roll no: 41")
root.geometry("400x300")
root.configure(bg="#2E2E2E")

# ===== Header =====
header = tk.Label(
    root, 
    text="Select a Module to Run", 
    font=("Helvetica", 14, "bold"), 
    fg="#FFFFFF", 
    bg="#2E2E2E"
)
header.pack(pady=15)

# ===== Script Buttons =====
for name in scripts:
    btn = tk.Button(
        root, text=name, width=30, height=2,
        fg="#FFFFFF", bg="#333333", activebackground="#555555",
        activeforeground="#FFFFFF", bd=0, font=("Helvetica", 12)
    )
    btn.pack(pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.config(command=lambda n=name: run_script(n))

# ===== Exit Button =====
exit_btn = tk.Button(
    root, text="Exit", width=30, height=2,
    fg="#FFFFFF", bg="#AA2222", activebackground="#FF5555",
    activeforeground="#FFFFFF", bd=0, font=("Helvetica", 12),
    command=root.destroy
)
exit_btn.pack(pady=15)
exit_btn.bind("<Enter>", on_enter)
exit_btn.bind("<Leave>", on_leave)

root.mainloop()