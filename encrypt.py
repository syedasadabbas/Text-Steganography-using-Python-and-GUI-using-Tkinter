def encrypt(message):
    # Null Cipher mapping
    null_cipher_mapping = {
        'A': 'Artificial', 'B': 'bounty', 'C': 'Cat', 'D': 'Dirty', 'E': 'Empower', 'F': 'Fine',
        'G': 'Guts', 'H': 'Hymn', 'I': 'Ink', 'J': 'Jug', 'K': 'Kulfa', 'L': 'Lemon', 'M': 'Manner',
        'N': 'Nice', 'O': 'Octopus', 'P': 'Python', 'Q': 'Quilt', 'R': 'Rent', 'S': 'Such',
        'T': 'Turtle', 'U': 'UNO', 'V': 'Viola', 'W': "Who's", 'X': 'Extreme', 'Y': 'Your', 'Z': 'Zings',
        'a': 'new', 'b': 'sky', 'c': 'noon', 'd': 'dig', 'e': 'like', 'f': 'look',
        'g': 'black', 'h': 'jungle', 'i': 'sag', 'j': 'blue', 'k': 'work', 'l': 'great', 'm': 'high',
        'n': 'while', 'o': 'sea', 'p': 'citation', 'q': 'shine', 'r': 'backup', 's': 'off',
        't': 'hundred', 'u': 'once', 'v': 'coating', 'w': "pluck", 'x': 'yes', 'y': 'goat', 'z': 'now'
    }

    # Apply Null Cipher
    converted_message = ""
    for letter in message:
        if letter in null_cipher_mapping:
            converted_message += null_cipher_mapping[letter]
        else:
            converted_message += letter

    # Apply key = 3
    key = 3
    shifted_message = ""
    for char in converted_message:

        if char.isalpha():
            if char.isupper():
                shifted_char = chr(
                    (ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                shifted_char = chr(
                    (ord(char) - ord('a') + key) % 26 + ord('a'))
            shifted_message += shifted_char
        else:
            shifted_message += char

    # Apply base 85 conversion
    base85_message = shifted_message.encode('ascii').hex()

    # Save encrypted message to file
    with open('encrypted.txt', 'w') as file:
        file.write(base85_message)
    with open('nobase.txt', 'w') as file:
        file.write(shifted_message)
    with open('nocipher.txt', 'w') as file:
        file.write(converted_message)


with open('filetosecure.txt', 'r') as file:
    secret_message = file.read()

encrypt(secret_message)
print("Encryption complete. Encrypted message saved in 'encrypted.txt'.")
