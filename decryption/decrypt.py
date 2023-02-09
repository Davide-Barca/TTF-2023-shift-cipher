from dotenv import load_dotenv
import os
import string


def decrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """
    testo = text.read()
    testo = testo.lower()
    output = ""

    for char in testo:
        if char.isalpha():
            ascii_code = ord(char) - ord('a')
            new_code = (ascii_code - int(key)) % 26
            new_char = chr(new_code + ord('a'))
            output += new_char
        else:
            output += char 
    return str(output)


def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    k = os.getenv("KEY")
    # read from encrypt_input.txt
    text = open("./decryption/decrypt_input.txt")
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txt
    with open("./decryption/decrypt_output.txt", "w") as output:
        output.write(decrypt(text, k))

   


if __name__ == "__main__":
    _main()
