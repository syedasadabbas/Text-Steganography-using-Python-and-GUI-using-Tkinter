import tkinter as tk
from tkinter import filedialog

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


# Example usage
encrypted_file = "encrypted.txt"

# Open file dialog to select the PDF file
root = tk.Tk()
root.withdraw()
pdf_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

output_file = "hidden_message.pdf"

hide_file(encrypted_file, pdf_file, output_file)
