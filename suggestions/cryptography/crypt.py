import uuid
import hashlib
import getpass

def get_message():
    
    # Get a message to encrypt
    message = str(raw_input("Enter message: "))
    return message


def get_key():

    # Get an encryption key
    encryption_key = 0
    key = raw_input("Enter encryption key: ")
    
    # Convert non-digit characters to numbers
    for letter in key:
        if letter.isdigit():
            encryption_key += int(letter)
        else:
            # If the input contains a letter, use its ascii-value instead
            encryption_key += ord(letter)

    # Limit the key to max 255
    return (encryption_key % 256)

<<<<<<< HEAD

def caesar_cipher_encrypt(message, encryption_key):

    encrypted = ""
=======
def caesar_cipher_encrypt(message, encryption_key):
    
    encrypted = ""
    
    # Encrypt each letter of the message
>>>>>>> 369417c6ead09a4462fbf6852e9c4a53741e4c1b
    for letter in message:
        # Print the formula for encrypting each letter
        print "Encrypting {0}: {1} + {2} % 256 = {3}".format(letter, ord(letter), encryption_key, ((ord(letter) + encryption_key) % 256))
        encrypted += chr((ord(letter) + encryption_key) % 256)

    return encrypted

def caesar_cipher_decrypt(cipher_text, encryption_key):

    decrypted = ""
    for letter in cipher_text:
        decrypted += chr((ord(letter) - encryption_key) % 256)
        print "Decrypting {0}: {1} - {2} % 256 = {3}".format(repr(letter), ord(letter), encryption_key, ((ord(letter) - encryption_key) % 256))

    return decrypted

<<<<<<< HEAD

def run_caesar_cipher():
=======
if __name__ == "__main__":

>>>>>>> 369417c6ead09a4462fbf6852e9c4a53741e4c1b
    key = get_key()
    message = get_message()

    cipher_text = caesar_cipher_encrypt(message, key)
    print "\nCipher text: {0}\n".format(cipher_text)

<<<<<<< HEAD
    decrypted_text = caesar_cipher_decrypt(cipher_text, key)
    print "\nDecrypted Message: {0}".format(decrypted_text)


def hash_password(pw):

    hashobj = hashlib.sha256(pw)
    return hashobj.hexdigest()


def set_password():

    hashed = hash_password(getpass.getpass(prompt="Set Password: "))
    return hashed

def run_login():
    
    password_hash = set_password()
    pw = getpass.getpass(prompt="Password: ")

    if password_hash != hash_password(pw):
        print "Access denied"
    else:
        run_caesar_cipher()

if __name__ == "__main__":

    run_login()
=======
    message = caesar_cipher_decrypt(cipher_text, key)
    print "\nCipher text: {0}\n".format(repr(str(message)))
>>>>>>> 369417c6ead09a4462fbf6852e9c4a53741e4c1b
