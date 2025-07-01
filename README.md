# mlops_databricks_mlflow

## Présentation
Ce projet montre comment entraîner un modèle ML avec MLflow et le déployer sur Databricks via un job serverless ou en utilisant Docker.

## Prérequis
- Python 3.9+
- Docker (optionnel)
- Un compte Databricks avec droits de création de jobs et accès à l'API
- Un token d'accès Databricks (`DATABRICKS_TOKEN`)
- L'URL de ton workspace Databricks (`DATABRICKS_INSTANCE`)

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

### a) Uploader le script sur DBFS

Assure-toi d'avoir le Databricks CLI installé et configuré :

```bash
pip install databricks-cli
# Configure avec : databricks configure --token

databricks fs cp train.py dbfs:/FileStore/train.py --overwrite
```

### b) Adapter la configuration du job

Vérifie que `job_config.json` est au format serverless (voir exemple dans ce repo).

### c) Déployer le job

```bash
bash deploy_databricks.sh
```

Le job s'appelle **ML MLOps Serverless Job** et apparaîtra dans l'interface Databricks.

---

## Dépannage
- Vérifie que le script est bien uploadé sur DBFS.
- Vérifie que les variables d'environnement sont bien définies.
- Le token doit avoir les droits nécessaires.
- Pour Docker, remplace `abouirdi` par ton nom Docker Hub si besoin.
