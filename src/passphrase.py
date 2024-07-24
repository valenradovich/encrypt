import os
import secrets
import string

def generate_passphrase(length=32):
    characters = string.ascii_letters + string.digits + string.punctuation
    passphrase = ''.join(secrets.choice(characters) for _ in range(length))
    return passphrase.encode('utf-8')

def save_passphrase(passphrase, filename):
    with open(filename, 'wb') as f:
        f.write(passphrase)
    # restrict permissions to owner only 
    # (this could be handled with a group as well to add more than 1 user)
    os.chmod(filename, 0o600)
    
def load_passphrase(filename):
    with open(filename, 'r') as f:
        return f.read().strip()
    
        
    

