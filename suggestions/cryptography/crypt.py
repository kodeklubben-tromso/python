import string


def caesar_cipher_encrypt():
    encryption_key = int(raw_input("Enter encryption key: ")) % 256
    message = str(raw_input("Enter message: "))

    encrypted = ""

    for letter in message:
    	if letter == ' ':
	    encrypted += ' '
        encrypted += chr((ord(letter) + encryption_key) % 256)

    print encrypted
    return encrypted, encryption_key


def caesar_cipher_decrypt(literal, encryption_key):


    decrypted = ""
    for letter in literal:
    	if letter == ' ':
	    decrypted += ' '
	elif (ord(letter) - encryption_key) < 0:
	    decrypted += chr(255 + ord(letter) - encryption_key)
	else:
            decrypted += chr((ord(letter) - encryption_key))

    print decrypted

if __name__ == "__main__":
    cipher_text, key = caesar_cipher_encrypt()
    caesar_cipher_decrypt(cipher_text, key)
