import string


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

def caesar_cipher_encrypt(message, encryption_key):
    
    encrypted = ""
    
    # Encrypt each letter of the message
    for letter in message:
        # Print the formula for encrypting each letter
        print "Encrypting {0}: {1} + {2} % 256 = {3}".format(letter, ord(letter), encryption_key, ((ord(letter) + encryption_key) % 256))
        encrypted += chr((ord(letter) + encryption_key) % 256)

    return encrypted

if __name__ == "__main__":

    key = get_key()
    message = get_message()

    cipher_text = caesar_cipher_encrypt(message, key)
    print "\nCipher text: {0}\n".format(repr(str(cipher_text)))
