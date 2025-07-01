# deploy_databricks.sh
#!/bin/bash

# Vérifier que le Databricks CLI est installé, sinon l'installer
if ! command -v databricks &> /dev/null; then
  echo "Databricks CLI non trouvé, installation..."
  pip install --user databricks-cli
  export PATH="$HOME/.local/bin:$PATH"
fi

# S'assurer que DATABRICKS_INSTANCE commence par https://
if [[ "$DATABRICKS_INSTANCE" != https://* ]]; then
  export DATABRICKS_INSTANCE="https://${DATABRICKS_INSTANCE}"
fi

if [ -z "$DATABRICKS_INSTANCE" ] || [ -z "$DATABRICKS_TOKEN" ]; then
  echo "Erreur : DATABRICKS_INSTANCE et/ou DATABRICKS_TOKEN ne sont pas définis."
  exit 1
fi

curl -X POST ${DATABRICKS_INSTANCE}/api/2.1/jobs/create \
  -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @job_config.json

databricks fs cp train.py dbfs:/FileStore/train.py

