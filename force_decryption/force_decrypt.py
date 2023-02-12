from dotenv import load_dotenv
import os
import string


def decrypt(text: str, key: int) -> str:
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
            new_code = (ascii_code - int(key)) % 26
            new_char = chr(new_code + ord('a'))
            output += new_char
        else:
            output += char

    output = output + "\n\n"
    return output


def _main():
    load_dotenv()
    # read your secret encryption key from the .env file
    # k = os.getenv("KEY")
    key_limit = 10 
    count = 0
    # read from encrypt_input.txt
    text = open("./force_decryption/force_decrypt_input.txt")
    testo = text.read()
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txt
    with open("./force_decryption/force_decrypt_output.txt", "w") as output:
        message = ""
        while(count < key_limit):
            message += "key used: " + str(count) + "\n" + decrypt(testo, count)
            count += 1
        output.write(str(message))

   


if __name__ == "__main__":
    _main()
