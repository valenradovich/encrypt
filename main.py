import config
from src.passphrase import generate_passphrase, save_passphrase, load_passphrase
from src.encrypt import compress_and_encrypt_folder
from src.decrypt import decrypt_and_decompress_folder

def main():
    # generate a passphrase
    passphrase = generate_passphrase()
    save_passphrase(passphrase, 'secure_passphrase.bin')
    print("Passphrase saved.")
    
    # encrypt a folder
    input_raw_files = 'input_files'
    output_encrypted = 'encrypted_files'
    compress_and_encrypt_folder(input_raw_files, output_encrypted, passphrase)
    
    # decrypt a folder
    input_encrypted = 'encrypted_files'
    output_decrypted = 'decrypted_files'
    decrypt_and_decompress_folder(input_encrypted, output_decrypted, load_passphrase('secure_passphrase.bin'))
    
    
if __name__ == '__main__':
    main()