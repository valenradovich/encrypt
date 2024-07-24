import os
import subprocess
import tarfile

def decrypt_and_decompress_folder(input_folder, output_folder, passphrase):
    os.makedirs(output_folder, exist_ok=True)
    
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path) and file_path.endswith('.gpg'):
            decrypted_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0])
            
            # decrypt
            command_gpg = [
                'gpg', '--batch', '--yes', '--decrypt', '--passphrase', passphrase,
                '--output', decrypted_file_path, file_path
            ]
            result_gpg = subprocess.run(command_gpg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result_gpg.stdout.decode())
            if result_gpg.returncode != 0:
                print(f"Failed to decrypt {file_path}: {result_gpg.stderr.decode()}")
                continue

            # decompress the file
            with tarfile.open(decrypted_file_path, 'r:gz') as tar:
                tar.extractall(output_folder)
            os.remove(decrypted_file_path)
            print(f"Decrypted and decompressed {file_path} to {output_folder}")
