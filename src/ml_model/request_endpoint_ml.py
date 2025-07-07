import requests
import json
from sklearn.datasets import load_diabetes

# Token personnel Databricks (à générer si besoin)
DATABRICKS_TOKEN = "<YOUR_DATABRICKS_TOKEN>"  # 🔐 à remplacer

# URL de ton endpoint (copie depuis l’écran "Use this model for inference")
ENDPOINT_URL = "<YOUR_ENDPOINT_URL>"


# Charger un échantillon comme dans ton run.py
data = load_diabetes(as_frame=True)
X_sample = data.data.sample(1, random_state=42)

# Transformer en format JSON compatible avec le format "split"
payload = {
    "dataframe_split": {
        "columns": list(X_sample.columns),
        "data": X_sample.values.tolist()
    }
}

headers = {
    "Authorization": f"Bearer {DATABRICKS_TOKEN}",
    "Content-Type": "application/json"
}

# Envoyer la requête
response = requests.post(ENDPOINT_URL, headers=headers, data=json.dumps(payload))

# Afficher le résultat
print("Prediction:", response.json())
