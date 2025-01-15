from cryptography.fernet import Fernet
import pickle

def encrypt_model():
    # Generar una clave
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

    # Cargar el modelo
    model_data = pickle.load(open('model.pkl', 'rb'))

    # Encriptar el modelo
    fernet = Fernet(key)
    with open("model_encrypted.pkl", 'wb') as f:
        f.write(fernet.encrypt(pickle.dumps(model_data)))

    print("Modelo encriptado y guardado en 'model_encrypted.pkl'.")

if __name__ == "__main__":
    encrypt_model()
