import uuid
import hashlib
import getpass

def get_message():

    message = str(raw_input("Enter message: "))
    print "\n"
    return message


def get_key():

    encryption_key = 0
    key = raw_input("Enter encryption key: ")
    for letter in key:
        if letter.isdigit():
            encryption_key += int(letter)
        else:
            encryption_key += ord(letter)

    return (encryption_key % 256)


def caesar_cipher_encrypt(message, encryption_key):

    encrypted = ""
    for letter in message:
        print "Encrypting {0}: {1} + {2} % 256 = {3}".format(letter, ord(letter), encryption_key, ((ord(letter) + encryption_key) % 256))
        encrypted += chr((ord(letter) + encryption_key) % 256)

    return encrypted


def caesar_cipher_decrypt(literal, encryption_key):

    decrypted = ""
    for letter in literal:
        decrypted += chr((ord(letter) - encryption_key) % 256)
        print "Decrypting {0}: {1} - {2} % 256 = {3}".format(repr(letter), ord(letter), encryption_key, ((ord(letter) - encryption_key) % 256))

    return decrypted


def run_caesar_cipher():
    key = get_key()
    message = get_message()

    cipher_text = caesar_cipher_encrypt(message, key)
    print "\nCipher text: {0}\n".format(cipher_text)

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