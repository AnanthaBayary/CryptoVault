import os
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox
from cryptography.fernet import Fernet


class FolderEncryptor:
    def __init__(self, master):
        self.master = master
        master.title("Folder Encryptor/Decryptor")
        master.geometry("545x200")

        self.folder_path = StringVar()
        self.key = StringVar()

        self.create_widgets()

    def create_widgets(self):
        Label(self.master, text="Folder Path:").grid(row=0, column=0, padx=5, pady=5)
        Entry(self.master, textvariable=self.folder_path, width=40).grid(row=0, column=1, padx=5, pady=5)
        Button(self.master, text="Browse", command=self.browse_folder).grid(row=0, column=2, padx=5, pady=5)

        Label(self.master, text="Encryption Key:").grid(row=1, column=0, padx=5, pady=5)
        Entry(self.master, textvariable=self.key, width=40, show="*").grid(row=1, column=1, padx=5, pady=5)

        Button(self.master, text="Encrypt", command=lambda: self.process_folder('encrypt'), bg='lightgreen').grid(row=2, column=0, padx=5, pady=5)
        Button(self.master, text="Decrypt", command=lambda: self.process_folder('decrypt'), bg='lightcoral').grid(row=2, column=1, padx=5, pady=5)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def get_cipher(self):
        return Fernet(self.key.get().encode())

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
            for root, dirs, files in os.walk(self.folder_path.get()):
                for file in files:
                    file_path = os.path.join(root, file)
                    if action == 'encrypt':
                        self.encrypt_file(file_path, cipher)
                    elif action == 'decrypt':
                        self.decrypt_file(file_path, cipher)

            messagebox.showinfo("Success", f"{action.capitalize()}ion completed successfully.")
            self.master.quit()  
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = FolderEncryptor(root)
    root.mainloop()
