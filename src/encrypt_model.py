from cryptography.fernet import Fernet
import pickle

def encrypt_model():
    # Key generation
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

    # Load model
    model_data = pickle.load(open('model.pkl', 'rb'))

    # Encrypt model
    fernet = Fernet(key)
    with open("model_encrypted.pkl", 'wb') as f:
        f.write(fernet.encrypt(pickle.dumps(model_data)))

    print("Model encrypted and saved into 'model_encrypted.pkl'.")

if __name__ == "__main__":
    encrypt_model()
