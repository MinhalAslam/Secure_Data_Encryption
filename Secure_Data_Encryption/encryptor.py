from cryptography.fernet import Fernet

def generate_key():
    """Generates and returns a secure encryption key."""
    return Fernet.generate_key()

def encrypt_message(key, message):
    """Encrypts a message using the given key."""
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted

def decrypt_message(key, encrypted_message):
    """Decrypts a message using the given key."""
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message).decode()
    return decrypted
