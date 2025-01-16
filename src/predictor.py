import os
import base64
import pickle
from cryptography.fernet import Fernet


def load_encrypted_model():
    key_encoded = "4wah6uXgU3VvULQGPxUx15t0w5U1Dfvn3BGT48HE3j4="
    # Get current folder path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta al archivo del modelo encriptado
    model_path = os.path.join(current_dir, 'model_encrypted.pkl')

    # Load and uncrypt the model
    with open(model_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    fernet = Fernet(key_encoded)
    decrypted_data = fernet.decrypt(encrypted_data)

    # load model from decrypted file
    model = pickle.loads(decrypted_data)
    return model


def predict_price(model, features):
    prediction = model.predict([features])
    return prediction[0]


def main():
    print('House pricing prediction app')
    print("Introduse your house features:")

    feature_names = [
        'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
        'Population', 'AveOccup', 'Latitude', 'Longitude'
    ]

    features = []
    for name in feature_names:
        value = float(input(f"{name}: "))
        features.append(value)

    # Load encrypted model
    model = load_encrypted_model()

    # Make prediction
    price = predict_price(model, features)
    print(f"Predicted price: ${price * 100000:.2f}")
        
    input("Press any key to exit: ")


if __name__ == "__main__":
    main()
