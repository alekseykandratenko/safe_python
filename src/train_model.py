import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def train_and_save_model():
    # Load dataset
    data = fetch_california_housing()
    X = data.data
    y = data.target

    # Divide the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    score = model.score(X_test, y_test)
    print(f"Precisión del modelo: {score * 100:.2f}%")

    # Save model
    pickle.dump(model, open('model.pkl', 'wb'))
    print("Modelo guardado en 'model.pkl'.")

if __name__ == "__main__":
    train_and_save_model()
