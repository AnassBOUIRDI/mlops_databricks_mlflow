# mlops_databricks_mlflow

## Présentation
Ce projet montre comment entraîner un modèle ML avec MLflow et le déployer sur Databricks via un job Dockerisé.

## Prérequis
- Docker
- Un compte Databricks avec droits de création de jobs et accès à l'API
- Un token d'accès Databricks (`DATABRICKS_TOKEN`)
- L'URL de ton workspace Databricks (`DATABRICKS_INSTANCE`)

## 1. Builder et pousser l'image Docker

```bash
docker build -t abouirdi/mlops-databricks-demo:latest .
docker push abouirdi/mlops-databricks-demo:latest
```

> Remplace `abouirdi` par ton nom Docker Hub si besoin.

## 2. Configurer les variables d'environnement

```bash
export DATABRICKS_INSTANCE="<ton-instance>.cloud.databricks.com"
export DATABRICKS_TOKEN="<ton-token>"
```

## 3. Déployer le job sur Databricks

```bash
bash deploy_databricks.sh
```

## 4. Vérifier le job dans l'interface Databricks

Le job s'appelle **ML MLOps Docker Job**.

---

## Dépannage
- Vérifie que l'image Docker est bien publique et accessible.
- Vérifie que les variables d'environnement sont bien définies.
- Le token doit avoir les droits nécessaires.
