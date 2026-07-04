import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DKFAB_FILE = os.path.join(PROJECT_FOLDER, "dkfab.txt")
MAIN_FILE = os.path.join(PROJECT_FOLDER, "main.py")


def run_dkfab():
    code = text_box.get("1.0", tk.END).strip()

    if not code:
        messagebox.showwarning("DK Fab", "No DK Fab code entered.")
        return

    with open(DKFAB_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    status_box.delete("1.0", tk.END)
    status_box.insert(tk.END, "Running DK Fab...\n\n")
    root.update()

    if not os.path.exists(MAIN_FILE):
        status_box.insert(tk.END, f"ERROR: Cannot find main.py here:\n{MAIN_FILE}\n")
        return

    try:
        result = subprocess.run(
            [sys.executable, MAIN_FILE],
            cwd=PROJECT_FOLDER,
            capture_output=True,
            text=True
        )

        if result.stdout:
            status_box.insert(tk.END, result.stdout)

        if result.stderr:
            status_box.insert(tk.END, "\nERROR:\n")
            status_box.insert(tk.END, result.stderr)

        status_box.insert(tk.END, "\nFinished.\n")

    except Exception as e:
        status_box.insert(tk.END, f"\nFAILED:\n{e}\n")


def clear_code():
    text_box.delete("1.0", tk.END)


def paste_code():
    try:
        clip = root.clipboard_get()
        text_box.insert(tk.INSERT, clip)
    except:
        messagebox.showwarning("DK Fab", "Clipboard is empty or unavailable.")


def load_example():
    example = """PART name=nema17_mount_plate
PLATE width=150 height=80 thickness=4

SKETCH operation=cut
CIRCLE x=-45 y=0 diameter=22
CIRCLE x=-60.5 y=-15.5 diameter=3.5
CIRCLE x=-29.5 y=-15.5 diameter=3.5
CIRCLE x=-60.5 y=15.5 diameter=3.5
CIRCLE x=-29.5 y=15.5 diameter=3.5

CIRCLE x=35 y=-20 diameter=6.5
CIRCLE x=65 y=-20 diameter=6.5
CIRCLE x=35 y=20 diameter=6.5
CIRCLE x=65 y=20 diameter=6.5
END_SKETCH

SAVE name=nema17_mount_plate
"""
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, example)


root = tk.Tk()
root.title("DK Fab")
root.geometry("1000x760")

title = tk.Label(root, text="DK Fab", font=("Arial", 22, "bold"))
title.pack(pady=8)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Paste", font=("Arial", 12), width=12, command=paste_code).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Clear", font=("Arial", 12), width=12, command=clear_code).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Load Example", font=("Arial", 12), width=14, command=load_example).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Run DK Fab", font=("Arial", 14, "bold"), width=16, command=run_dkfab).grid(row=0, column=3, padx=15)

text_box = tk.Text(root, height=28, font=("Consolas", 12), undo=True)
text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

status_label = tk.Label(root, text="Status", font=("Arial", 12, "bold"))
status_label.pack()

status_box = tk.Text(root, height=8, font=("Consolas", 10))
status_box.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

load_example()

root.mainloop()