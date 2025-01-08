from cryptography.fernet import Fernet

class FileEncryptor:
    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    @staticmethod
    def encrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            data = file.read()
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    @staticmethod
    def decrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)