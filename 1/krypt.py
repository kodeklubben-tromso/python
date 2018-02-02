import string


def caesar_cipher_encrypt():
    encryption_key = int(raw_input("Enter encryption key: "))
    message = raw_input("Enter message: ")

    encrypted = ""

    for letter in message:
        encrypted += chr((ord(letter) + encryption_key) % 256)

    print repr(encrypted)
    return repr(encrypted)


def caesar_cipher_decrypt(literal):

    encryption_key = 4545

    decrypted = ""
    for letter in repr(literal):
        decrypted += chr((ord(letter) + encryption_key) % 256)

    print decrypted

if __name__ == "__main__":
    # caesar_cipher_encrypt()
    caesar_cipher_decrypt(literal='\t&*\xed\xe1%&55&\xe1&3\xe1&/\xe1)&..&-*(\xe1.&-%*/(\xe140.\xe1%6\xe1,"/\xe1%&,0%&\xe1)7*4\xe1%6\xe1)"3\xe13*,5*(\xe1/\x84y,,&-')