# mlops_databricks_mlflow

## Présentation
Ce projet montre comment entraîner un modèle ML avec MLflow et le déployer sur Databricks via un job serverless ou en utilisant Docker.

## Prérequis
- Python 3.9+
- Docker (optionnel)
- Un compte Databricks avec droits de création de jobs et accès à l'API
- Un token d'accès Databricks (`DATABRICKS_TOKEN`)
- L'URL de ton workspace Databricks (`DATABRICKS_INSTANCE`)  -

---

## 1. Exécution locale

### a) Installation des dépendances

Active ton environnement virtuel (optionnel mais recommandé) puis installe les dépendances :

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### b) Lancer le script

```bash
python train.py
```

---

## 2. Exécution avec Docker

### a) Builder l'image Docker

```bash
docker build -t abouirdi/mlops-databricks-demo:latest .
```

### b) Exécuter le conteneur

```bash
docker run --rm abouirdi/mlops-databricks-demo:latest
```

---

## 3. Déploiement sur Databricks (mode serverless)

### a) Déploiement via Databricks Bundle (recommandé)

1. **Mettre à jour la configuration Databricks CLI**

Assure-toi que le fichier `~/.databrickscfg` est bien configuré avec l'URL de ton workspace et un token valide :

```ini
[DEFAULT]
host = https://<ton-instance>.cloud.databricks.com
token = dapiXXXXXXXXXXXXXXXXXXXXXXXX
```

Pour configurer :
```bash
databricks configure --token
```

2. **Déployer et exécuter le job avec le bundle**

```bash
pip install --upgrade databricks-cli

databricks bundle deploy

databricks bundle run train-job
```

Le script `train.py` sera automatiquement uploadé sur DBFS et le job sera lancé sur un cluster serverless minimal.

---

## Dépannage
- Vérifie que le script est bien uploadé sur DBFS (automatique avec le bundle).
- Vérifie que les variables d'environnement ou le fichier `.databrickscfg` sont bien définis.
- Le token doit avoir les droits nécessaires.
- Pour Docker, remplace `abouirdi` par ton nom Docker Hub si besoin.
