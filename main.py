import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import platform

def generate_and_save_qr_code():
    url = url_entry.get()
    if url:
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(save_path)
                status_label.config(text=f"QR code saved as {save_path}")
                open_image_with_viewer(save_path)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL!")

def open_image_with_viewer(file_path):
    system = platform.system()
    if system == "Windows":
        subprocess.Popen(['start', file_path], shell=True)
    elif system == "Darwin":  # macOS
        subprocess.Popen(['open', file_path])
    elif system == "Linux":
        subprocess.Popen(['xdg-open', file_path])
    else:
        messagebox.showwarning("Warning", "Unsupported platform")
root = tk.Tk()
root.title("Advanced QR Code Generator")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=40)
url_entry.pack()

generate_button = tk.Button(root, text="Generate and Save QR Code", command=generate_and_save_qr_code)
generate_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
