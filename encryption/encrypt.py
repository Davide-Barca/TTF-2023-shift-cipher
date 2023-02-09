from dotenv import load_dotenv
import os
import string


def encrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """

    if type(key) is not int or key < 0:
        raise ValueError("Key must be >= 0")

    testo = text.lower()
    output = ""

    for char in testo:
        if char.isalpha():
            ascii_code = ord(char) - ord('a')
            new_code = (ascii_code + int(key)) % 26
            new_char = chr(new_code + ord('a'))
            output += new_char
        else:
            output += char
    return output


def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    k = os.getenv("KEY")
    # read from encrypt_input.txt
    text = open("./encryption/encrypt_input.txt")
    testo = text.read()
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txt
    with open("./encryption/encrypt_output.txt", "w") as output:
        output.write(encrypt(testo, k))

   


if __name__ == "__main__":
    _main()
