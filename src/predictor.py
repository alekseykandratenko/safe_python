import os
import base64
import pickle
from cryptography.fernet import Fernet


def load_encrypted_model():
    key_encoded = "4wah6uXgU3VvULQGPxUx15t0w5U1Dfvn3BGT48HE3j4="
    # Obtener la ruta del directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Ruta al archivo del modelo encriptado
    model_path = os.path.join(current_dir, 'model_encrypted.pkl')

    # Cargar y desencriptar el modelo
    with open(model_path, 'rb') as enc_file:
        encrypted_data = enc_file.read()

    fernet = Fernet(key_encoded)
    decrypted_data = fernet.decrypt(encrypted_data)

    # Cargar el modelo desde los datos desencriptados
    model = pickle.loads(decrypted_data)
    return model


def predict_price(model, features):
    prediction = model.predict([features])
    return prediction[0]


def main():
    print("Aplicación de Predicción de Precios de Viviendas")
    print("Ingrese las características de la vivienda:")

    feature_names = [
        'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
        'Population', 'AveOccup', 'Latitude', 'Longitude'
    ]

    features = []
    for name in feature_names:
        value = float(input(f"{name}: "))
        features.append(value)

    # Cargar el modelo encriptado
    model = load_encrypted_model()

    # Realizar la predicción
    price = predict_price(model, features)
    print(f"El precio estimado de la vivienda es: ${price * 100000:.2f}")
        
    input("Press any key to exit: ")


if __name__ == "__main__":
    main()
