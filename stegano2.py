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


# Example usage
hidden_pdf = "hidden_message.pdf"
output_file = "retrieved_encrypted.txt"

extract_hidden_file(hidden_pdf, output_file)
