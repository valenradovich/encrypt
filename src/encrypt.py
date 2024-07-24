# sudo apt-get install gnupg in linux env
import os
import subprocess
from passphrase import load_passphrase

def compress_and_encrypt_folder(input_folder, output_folder, passphrase):
    os.makedirs(output_folder, exist_ok=True)
    
    # compress folder
    tar_file = os.path.join(output_folder, 'compressed_folder.tar.gz')
    command_tar = ['tar', '-czf', tar_file, '-C', input_folder, '.']
    subprocess.run(command_tar, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # encrypt compressed folder
    encrypted_file = tar_file + '.gpg'
    command_gpg = [
        'gpg', '--batch', '--yes', '--symmetric', '--cipher-algo', 'AES256',
        '--passphrase', passphrase, '--output', encrypted_file, tar_file
    ]
    subprocess.run(command_gpg, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Compressed and encrypted {input_folder} to {encrypted_file}")
