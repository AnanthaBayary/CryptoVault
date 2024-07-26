import os
import argparse
from cryptography.fernet import Fernet

class FolderEncryptorCLI:
    def __init__(self, folder_path, key, action):
        self.folder_path = folder_path
        self.key = key
        self.action = action

    def get_cipher(self):
        return Fernet(self.key.encode())

    def encrypt_file(self, file_path, cipher):
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encrypted_data = cipher.encrypt(file_data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path, cipher):
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)

    def process_folder(self):
        try:
            cipher = self.get_cipher()
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.action == 'encrypt':
                        self.encrypt_file(file_path, cipher)
                    elif self.action == 'decrypt':
                        self.decrypt_file(file_path, cipher)
            print(f"{self.action.capitalize()}ion completed successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Folder Encryptor/Decryptor CLI')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform: encrypt or decrypt')
    parser.add_argument('folder_path', help='Path to the folder to process')
    parser.add_argument('key', help='Encryption/Decryption key')
    return parser.parse_args()


def main():
    args = parse_arguments()
    encryptor = FolderEncryptorCLI(args.folder_path, args.key, args.action)
    encryptor.process_folder()


if __name__ == "__main__":
    main()
