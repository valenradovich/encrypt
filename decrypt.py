import config
from src.passphrase import load_passphrase
from src.decrypt import decrypt_and_decompress_folder

def main():
    # decrypt a folder
    input_encrypted = 'encrypted_files'
    output_decrypted = 'decrypted_files'
    decrypt_and_decompress_folder(input_encrypted, output_decrypted, load_passphrase('secure_passphrase.bin'))
    
if __name__ == '__main__':
    main()