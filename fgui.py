import tkinter as tk
from tkinter import filedialog
import subprocess


def hide_file(encrypted_file, pdf_file, output_file):
    # Read the contents of the encrypted file
    with open(encrypted_file, 'rb') as f:
        encrypted_contents = f.read()

    # Read the contents of the PDF file
    with open(pdf_file, 'rb') as f:
        pdf_contents = f.read()

    # Set the marker to indicate the start of the hidden contents
    marker = b"%MESSAGE%%EOF"

    # Combine the marker and the encrypted contents
    hidden_contents = marker + b'\n' + encrypted_contents

    # Write the modified contents to the output file
    with open(output_file, 'wb') as f:
        f.write(pdf_contents + hidden_contents)

    print("File hiding completed!")


def extract_hidden_file(hidden_pdf, output_file):
    # Read the contents of the hidden PDF file
    with open(hidden_pdf, 'rb') as f:
        hidden_contents = f.read()

    # Set the marker to indicate the start of the hidden contents
    marker = b"%MESSAGE%%EOF"

    # Find the position of the marker in the hidden contents
    start_position = hidden_contents.find(marker) + len(marker) + 1

    # Extract the hidden file contents
    extracted_contents = hidden_contents[start_position:]

    # Write the extracted contents to the output file
    with open(output_file, 'wb') as f:
        f.write(extracted_contents)

    print("Hidden file extracted successfully!")


def browse_encrypted_file():
    # Open file dialog to select the encrypted file
    root = tk.Tk()
    root.withdraw()
    encrypted_file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")])
    return encrypted_file


def browse_pdf_file():
    # Open file dialog to select the PDF file
    root = tk.Tk()
    root.withdraw()
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return pdf_file


def hide_text_in_pdf():
    # Get the encrypted file and PDF file paths
    encrypted_file = browse_encrypted_file()
    pdf_file = browse_pdf_file()

    if encrypted_file and pdf_file:
        # Set the output file path
        output_file = "hidden_message.pdf"

        # Hide the text in the PDF file
        hide_file(encrypted_file, pdf_file, output_file)
        success_label.config(text="File Hidden Successfully!")
        print("Text hiding successful!")


def extract_text_from_pdf():
    # Get the hidden PDF file path
    hidden_pdf = browse_pdf_file()

    if hidden_pdf:
        # Set the output file path
        output_file = "retrieved_encrypted.txt"

        # Extract the text from the hidden PDF file
        extract_hidden_file(hidden_pdf, output_file)
        success_label.config(text="Hidden File Extracted Successfully!")
        print("Text extraction successful!")


def open_file():
    subprocess.call(["notepad.exe", "filetosecure.txt"])
    success_label.config(text="File Opened & Closed Successfully!")


def encrypt_file():
    subprocess.call(["python", "encrypt.py"])
    success_label.config(text="File Encrypted Successfully!")


def view_encrypted_file():
    subprocess.call(["notepad.exe", "encrypted.txt"])
    success_label.config(text="Encrypted File Opened & Closed Successfully!")


def decrypt_file():
    subprocess.call(["python", "decrypt.py"])
    success_label.config(text="File Decrypted Successfully!")


def view_decrypted_file():
    subprocess.call(["notepad.exe", "decrypted.txt"])
    success_label.config(text="Decrypted File Opened & Closed Successfully!")


def view_extracted_file():
    subprocess.call(["notepad.exe", "retrieved_encrypted.txt"])
    success_label.config(text="Extracted File Opened & Closed Successfully!")


root = tk.Tk()
root.title("Text Steganography")
root.configure(bg="bisque")  # Set background color to bisque

# Title
title_label = tk.Label(root, text="CRYPTOGRAPHY AND NETWORK SECURITY", font=(
    "Gill Sans Ultra Bold Condensed", 28, "bold"), bg="bisque", fg="RoyalBlue4")
title_label.grid(row=0, column=0, columnspan=4, pady=15)

steg_label = tk.Label(root, text="TEXT STEGANOGRAPHY", font=(
    "Segoe UI", 20, "bold"), bg="bisque", fg="DeepSkyBlue3")
steg_label.grid(row=1, column=0, columnspan=4, pady=5)

teacher_label = tk.Label(root, text="Course Teacher: Mr. Syed Yawar Abbas Zaidi", font=(
    "Calibiri", 16, "bold"), bg="bisque")
teacher_label.grid(row=2, column=0, columnspan=4, pady=5)

project_label = tk.Label(root, text="Project Made By: Sania Ishaq & Syed Asad Abbas", font=(
    "Calibiri", 16, "bold"), bg="bisque", fg="Black")
project_label.grid(row=3, column=0, columnspan=4, pady=15)

operation_label = tk.Label(root, text="OPERATIONS OF ENCRYPTION AND DECRYPTION:", font=(
    "Seoge UI", 16, "bold"), bg="bisque", fg="HotPink4")
operation_label.grid(row=4, column=0, columnspan=4, pady=10)

operation_label = tk.Label(root, text="ENCRYPTION", font=(
    "Seoge UI", 13, "bold"), bg="bisque", fg="black")
operation_label.grid(row=5, column=0, padx=10, pady=10)

operation_label = tk.Label(root, text="DECRYTION", font=(
    "Seoge UI", 13, "bold"), bg="bisque", fg="black")
operation_label.grid(row=5, column=1, padx=10, pady=10)

operation_label = tk.Label(root, text="STEGANOGRAPHY", font=(
    "Seoge UI", 13, "bold"), bg="bisque", fg="black")
operation_label.grid(row=5, column=2, padx=10, pady=10)

# Buttons
button_bg = "cornflower blue"  # Set button background color
button_fg = "black"  # Set button foreground (text) color

# Encryption column buttons
open_file_button = tk.Button(root, text="Open File", font=(
    "Calibiri", 10, "bold"), command=open_file, bg=button_bg, fg=button_fg)
open_file_button.grid(row=6, column=0, padx=10, pady=5)

encrypt_file_button = tk.Button(root, text="Encrypt File", font=(
    "Calibiri", 10, "bold"), command=encrypt_file, bg=button_bg, fg=button_fg)
encrypt_file_button.grid(row=7, column=0, padx=10, pady=5)

view_encrypted_button = tk.Button(root, text="View Encrypted File", font=(
    "Calibiri", 10, "bold"), command=view_encrypted_file, bg=button_bg, fg=button_fg)
view_encrypted_button.grid(row=8, column=0, padx=10, pady=5)

# Decryption column buttons
decrypt_file_button = tk.Button(root, text="Decrypt File", font=(
    "Calibiri", 10, "bold"), command=decrypt_file, bg=button_bg, fg=button_fg)
decrypt_file_button.grid(row=6, column=1, padx=10, pady=5)

view_decrypted_button = tk.Button(root, text="View Decrypted File", font=(
    "Calibiri", 10, "bold"), command=view_decrypted_file, bg=button_bg, fg=button_fg)
view_decrypted_button.grid(row=7, column=1, padx=10, pady=5)

# Steganography column buttons
hide_text_button = tk.Button(root, text="Hide Text in PDF", font=(
    "Calibiri", 10, "bold"), command=hide_text_in_pdf, bg=button_bg, fg=button_fg)
hide_text_button.grid(row=6, column=2, padx=10, pady=5)

# Steganalysis column buttons
extract_text_button = tk.Button(root, text="Extract Text from PDF", font=(
    "Calibiri", 10, "bold"), command=extract_text_from_pdf, bg=button_bg, fg=button_fg)
extract_text_button.grid(row=7, column=2, padx=10, pady=5)

view_extracted_button = tk.Button(root, text="View Extracted File", font=(
    "Calibiri", 10, "bold"), command=view_extracted_file, bg=button_bg, fg=button_fg)
view_extracted_button.grid(row=8, column=2, padx=10, pady=5)

# Success Label
success_label = tk.Label(root, text="", font=(
    "Arial", 12, "bold"), fg="green", bg="bisque")
success_label.grid(row=9, column=0, columnspan=4, pady=20)

root.mainloop()
