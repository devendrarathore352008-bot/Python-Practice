import tkinter as tk
from tkinter import messagebox, filedialog

alphabet_keys  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 (){}[]!@#$%^&*-_+=:;><?/`~"
secret_keys = "QRSTUVWXYZ0123456789 !@#$%^&*-_+=:;><?/`~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP(){}[]"

def update_status(msg, color="white"):
    status_label.config(text=msg, fg=color)

def process_text(mode):
    user_message = input_text.get("1.0", tk.END).strip("\n")
    if not user_message:
        messagebox.showwarning("Empty Input", "Please enter a message first!")
        return

    result = ""
    for char in user_message:
        if mode == "encrypt":
            if char in alphabet_keys:
                pos = alphabet_keys.index(char)
                result += secret_keys[pos]
            else:
                result += char
        elif mode == "decrypt":
            if char in secret_keys:
                pos = secret_keys.index(char)
                result += alphabet_keys[pos]
            else:
                result += char
                
    # Unlock output box, paste result, lock it again
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", result)
    output_text.config(state=tk.DISABLED)
    
    action = "Encrypted" if mode == "encrypt" else "Decrypted"
    update_status(f"Success: Message {action} successfully!", "#4caf50")

def copy_clipboard():
    content = output_text.get("1.0", tk.END).strip("\n")
    if content:
        window.clipboard_clear()
        window.clipboard_append(content)
        update_status("Success: Copied to clipboard!", "#4caf50")
    else:
        update_status("Error: Nothing to copy.", "#f44336")

def save_file():
    content = output_text.get("1.0", tk.END).strip("\n")
    if content:
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "w") as file:
                file.write(content)
            update_status(f"Success: Saved to {filepath}", "#4caf50")
    else:
        update_status("Error: Nothing to save.", "#f44336")

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    update_status("Ready", "white")

# --- WINDOW ARCHITECTURE ---
window = tk.Tk()
window.title("Advanced Substitution Cipher - Project 8")
window.geometry("750x650")
window.configure(bg="#1e1e1e")

font_title = ("Segoe UI", 20, "bold")
font_label = ("Segoe UI", 11, "bold")
font_text = ("Consolas", 13)
bg_color = "#1e1e1e"

# Header
header = tk.Frame(window, bg="#007acc", pady=15)
header.pack(fill=tk.X)
tk.Label(header, text="🛡️ Substitution Cipher Protocol", font=font_title, bg="#007acc", fg="white").pack()

# Input Section
input_frame = tk.Frame(window, bg=bg_color, pady=10, padx=20)
input_frame.pack(fill=tk.BOTH, expand=True)
tk.Label(input_frame, text="INPUT MESSAGE:", font=font_label, bg=bg_color, fg="#007acc").pack(anchor="w")
input_text = tk.Text(input_frame, height=6, font=font_text, bg="#2d2d2d", fg="white", insertbackground="white", relief=tk.FLAT, padx=10, pady=10)
input_text.pack(fill=tk.BOTH, expand=True, pady=5)

# Core Control Panel
ctrl_frame = tk.Frame(window, bg=bg_color, pady=10)
ctrl_frame.pack()
tk.Button(ctrl_frame, text="🔒 ENCRYPT", font=font_label, bg="#d84315", fg="white", width=12, relief=tk.FLAT, command=lambda: process_text("encrypt")).grid(row=0, column=0, padx=5)
tk.Button(ctrl_frame, text="🔓 DECRYPT", font=font_label, bg="#2e7d32", fg="white", width=12, relief=tk.FLAT, command=lambda: process_text("decrypt")).grid(row=0, column=1, padx=5)
tk.Button(ctrl_frame, text="🗑️ CLEAR", font=font_label, bg="#333333", fg="white", width=12, relief=tk.FLAT, command=clear_all).grid(row=0, column=2, padx=5)

# Output Section
output_frame = tk.Frame(window, bg=bg_color, pady=10, padx=20)
output_frame.pack(fill=tk.BOTH, expand=True)
tk.Label(output_frame, text="OUTPUT MESSAGE:", font=font_label, bg=bg_color, fg="#007acc").pack(anchor="w")
output_text = tk.Text(output_frame, height=6, font=font_text, bg="#2d2d2d", fg="#4caf50", relief=tk.FLAT, padx=10, pady=10, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True, pady=5)

# Extra Features Panel
action_frame = tk.Frame(window, bg=bg_color, pady=10)
action_frame.pack()
tk.Button(action_frame, text="📋 Copy to Clipboard", font=font_label, bg="#333333", fg="white", width=18, relief=tk.FLAT, command=copy_clipboard).grid(row=0, column=0, padx=5)
tk.Button(action_frame, text="💾 Save to .txt File", font=font_label, bg="#333333", fg="white", width=18, relief=tk.FLAT, command=save_file).grid(row=0, column=1, padx=5)

# Status Bar
status_frame = tk.Frame(window, bg="#007acc", pady=5)
status_frame.pack(fill=tk.X, side=tk.BOTTOM)
status_label = tk.Label(status_frame, text="Ready", font=("Segoe UI", 10, "italic"), bg="#007acc", fg="white")
status_label.pack(anchor="w", padx=20)

window.mainloop()