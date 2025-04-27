import streamlit as st
from encryptor import generate_key, encrypt_message, decrypt_message

def main():
    st.title("🔒 Secure Data Encryption App")

    menu = ["Generate Key", "Encrypt Message", "Decrypt Message"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Generate Key":
        st.subheader("🔑 Generate a New Key")
        if st.button("Generate"):
            key = generate_key()
            st.success("Key generated successfully!")
            st.code(key.decode(), language='text')

    elif choice == "Encrypt Message":
        st.subheader("🔐 Encrypt your message")
        key = st.text_input("Enter your secret key")
        message = st.text_area("Enter the message to encrypt")

        if st.button("Encrypt"):
            try:
                encrypted = encrypt_message(key.encode(), message)
                st.success("Encrypted successfully!")
                st.code(encrypted.decode(), language='text')
            except Exception as e:
                st.error(f"Error: {e}")

    elif choice == "Decrypt Message":
        st.subheader("🔓 Decrypt your message")
        key = st.text_input("Enter your secret key")
        encrypted_message = st.text_area("Enter the encrypted message")

        if st.button("Decrypt"):
            try:
                decrypted = decrypt_message(key.encode(), encrypted_message.encode())
                st.success("Decrypted successfully!")
                st.code(decrypted, language='text')
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == '__main__':
    main()
