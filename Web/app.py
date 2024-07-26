from flask import Flask, render_template, request, redirect, flash, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class FolderEncryptor:
    def __init__(self):
        self.folder_path = None
        self.key = None

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

    def process_folder(self, action):
        try:
            cipher = self.get_cipher()
            for root, dirs, files in os.walk(self.folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if action == 'encrypt':
                        self.encrypt_file(file_path, cipher)
                    elif action == 'decrypt':
                        self.decrypt_file(file_path, cipher)

            return True, f"{action.capitalize()}ion completed successfully."
        except Exception as e:
            return False, f"{str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder_path = request.form.get('folder')
        encryption_key = request.form.get('key')
        action = request.form.get('action')

        encryptor = FolderEncryptor()
        encryptor.folder_path = folder_path
        encryptor.key = encryption_key

        if not os.path.exists(folder_path):
            flash(f"Folder '{folder_path}' does not exist.", 'error')
            return redirect('/')

        success, message = encryptor.process_folder(action)

        if success:
            flash(message, 'success')
        else:
            flash(message, 'error')

        return redirect('/')
    
    return render_template('index.html')

@app.route('/process_file', methods=['POST'])
def process_file():
    try:
        folder_path = request.form.get('folder')
        encryption_key = request.form.get('key')
        action = request.form.get('action')

        encryptor = FolderEncryptor()
        encryptor.folder_path = folder_path
        encryptor.key = encryption_key

        if not os.path.exists(folder_path):
            return jsonify({'error': f"Folder '{folder_path}' does not exist."}), 404

        success, message = encryptor.process_folder(action)

        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
