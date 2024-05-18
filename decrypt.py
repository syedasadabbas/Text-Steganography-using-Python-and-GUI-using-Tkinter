def decrypt():
    # Read encrypted message from file
    with open('encrypted.txt', 'r') as file:
        base85_message = file.read()

    # Reverse base 85 conversion
    shifted_message = bytes.fromhex(base85_message).decode('ascii')

    # Reverse key = 3
    key = 3
    decrypted_message = ""
    for char in shifted_message:

        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(
                    (ord(char) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted_char = chr(
                    (ord(char) - ord('a') - key) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char

    # Null Cipher reverse mapping
    null_cipher_mapping = {
        'Artificial': 'A', 'bounty': 'B', 'Cat': 'C', 'Dirty': 'D', 'Empower': 'E', 'Fine': 'F',
        'Guts': 'G', 'Hymn': 'H', 'Ink': 'I', 'Jug': 'J', 'Kulfa': 'K', 'Lemon': 'L', 'Manner': 'M',
        'Nice': 'N', 'Octopus': 'O', 'Python': 'P', 'Quilt': 'Q', 'Rent': 'R', 'Such': 'S',
        'Turtle': 'T', 'UNO': 'U', 'Viola': 'V', "Who's": 'W', 'Extreme': 'X', 'Your': 'Y', 'Zings': 'Z',
        'new': 'a', 'sky': 'b', 'noon': 'c', 'dig': 'd', 'like': 'e', 'look': 'f',
        'black': 'g', 'jungle': 'h', 'sag': 'i', 'blue': 'j', 'work': 'k', 'great': 'l', 'high': 'm',
        'while': 'n', 'sea': 'o', 'citation': 'p', 'shine': 'q', 'backup': 'r', 'off': 's',
        'hundred': 't', 'once': 'u', 'coating': 'v', "pluck": 'w', 'yes': 'x', 'goat': 'y', 'now': 'z'
    }

    # Apply Null Cipher reverse substitution
    for word, replacement in null_cipher_mapping.items():
        decrypted_message = decrypted_message.replace(word, replacement)

    # Save decrypted message to file
    with open('decrypted.txt', 'w') as file:
        file.write(decrypted_message)


decrypt()
print("Decryption complete. Decrypted message saved in 'decrypted.txt'.")
