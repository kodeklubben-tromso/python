import string


def caesar_cipher_encrypt():
    encryption_key = int(raw_input("Enter encryption key: ")) % 256
    message = str(raw_input("Enter message: "))

    encrypted = ""

    for letter in message:
        print "Encrypting {0}: {1} + {2} % 256 = {3}".format(letter, ord(letter), encryption_key, ((ord(letter) + encryption_key) % 256))
        encrypted += chr((ord(letter) + encryption_key) % 256)

    print "Cipher text: {0}\n".format(repr(str(encrypted)))
    return encrypted, encryption_key


def caesar_cipher_decrypt(literal, encryption_key):

    decrypted = ""
    for letter in literal:
        decrypted += chr((ord(letter) - encryption_key) % 256)
        print "Decrypting {0}: {1} - {2} % 256 = {3}".format(letter, ord(letter), encryption_key, ((ord(letter) - encryption_key) % 256))

    print "\nDecrypted Message: {0}".format(decrypted)

if __name__ == "__main__":
    cipher_text, key = caesar_cipher_encrypt()
    caesar_cipher_decrypt(cipher_text, key)
