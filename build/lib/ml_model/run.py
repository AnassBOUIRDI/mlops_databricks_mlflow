import mlflow
import pandas as pd
from sklearn.datasets import load_diabetes

def main():
    # Charger les données d'exemple
    data = load_diabetes(as_frame=True)
    X = data.data

    # Prendre un échantillon pour la prédiction
    X_sample = X.sample(1, random_state=42)

    # URI du modèle enregistré dans le run (non enregistré dans le registry)
    model_uri = "runs:/4ee8d3060ca6429a82f54333d92d9cd9/model"

    # Charger le modèle en tant que PyFuncModel
    model = mlflow.pyfunc.load_model(model_uri)

    # Faire la prédiction
    prediction = model.predict(X_sample)

    # Afficher les résultats
    print("=== Input sample ===")
    print(X_sample)
    print("\n=== Prediction ===")
    print(prediction)

if __name__ == "__main__":
    main()
