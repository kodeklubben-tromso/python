import hashlib
import getpass

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
        print "Access Granted"

if __name__ == "__main__":
    run_login()