# Author: Fahim Anzam Dip
# Date: 8th July, 2024

import tkinter as tk
from tkinter import filedialog
import time
from generator.convert_to_excel import generate_adspower
from generator.convert_to_excel_dolphin import generate_dolphin
import os

filepath = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def browse_files():
    global filepath
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select a file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filepath)

def generate_chunks():
    output_path = None

    loading_label.config(text="⚙️ Generating...", fg="orange", font=("Arial", 13, "bold"))
    root.update()
    
    selection = browser_var.get()
    if filepath and selection and chunk_count.get():
        if selection == "adspower":
            output_path = generate_adspower(filepath, int(chunk_count.get()))
        elif selection == "dolphin":
            output_path = generate_dolphin(filepath, int(chunk_count.get()))
        else:
            loading_label.config(text="Something Went Wrong!", fg="red", font=("Arial", 13, "bold"))

        loading_label.config(text=f"📁 Complete! {output_path}", fg="green", font=("Arial", 13, "bold"), wraplength=300)
    else:
        loading_label.config(text="Please fill all the fields!", fg="red", font=("Arial", 13, "bold"))

    root.update()

def clear_inputs():
    file_entry.delete(0, tk.END)
    browser_var.set(None)
    chunk_count.delete(0, tk.END)
    loading_label.config(text="")

root = tk.Tk()
root.title("By, Fahim Anzam Dip")
root.geometry("400x500")  # Set the window size
root.iconbitmap(default=resource_path('icon.ico')) # Set the window icon

# Title red color
title_label = tk.Label(root, text="Batch Generator", font=("Arial", 16, "bold"), fg="teal")
title_label.pack(pady=15)

# File input
file_label = tk.Label(root, text="Select text file ⬇️", font=("Arial", 12), fg="blue")
file_label.pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)
browse_button = tk.Button(root, text="Browse Files", command=browse_files, font=("Arial", 10), cursor="hand2")
browse_button.pack(pady=(5, 15))

# Radio button options
browser_var = tk.StringVar()
browser_var.set(None)  # Initialize the radio button variable
browser_label = tk.Label(root, text="Select browser ⬇️", font=("Arial", 12), fg="blue")
browser_label.pack(pady=5)
dolphin_radio = tk.Radiobutton(root, text="Dolphin Anty", variable=browser_var, value="dolphin", font=("Arial", 10), cursor="hand2")
dolphin_radio.pack(pady=2)
adspower_radio = tk.Radiobutton(root, text="Adspower Browser", variable=browser_var, value="adspower", font=("Arial", 10), cursor="hand2")
adspower_radio.pack(pady=(2, 15))

# Chunk count input
chunk_label = tk.Label(root, text="How many proxies in a file? ⬇️", font=("Arial", 12), fg="blue")
chunk_label.pack(pady=5)
chunk_count = tk.Entry(root, width=10)
chunk_count.pack(pady=5)

# Loading label
loading_label = tk.Label(root, text="", font=("Arial", 12))
loading_label.pack(pady=5)

# Create frame for buttons
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Generate button
generate_button = tk.Button(frame, text="Generate ✅", command=generate_chunks, font=("Arial", 10), cursor="hand2", bg="green", fg="white")
generate_button.grid(row=0, column=0, pady=5, padx=5)

# Clear button
clear_button = tk.Button(frame, text="Clear ❎", command=clear_inputs, font=("Arial", 10), cursor="hand2", bg="red", fg="white")
clear_button.grid(row=0, column=1, pady=5, padx=5)

root.mainloop()
