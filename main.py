def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar Cipher.
    
    :param text: The input string to be encrypted or decrypted.
    :param shift: The number of positions each character in the text is shifted.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The encrypted or decrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            char_code = ord(char) + shift_amount

            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26

            result += chr(char_code)
        else:
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
shift = 3

encrypted = caesar_cipher(plaintext, shift)
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
