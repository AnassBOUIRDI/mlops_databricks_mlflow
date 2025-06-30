# deploy_databricks.sh
#!/bin/bash

if [ -z "$DATABRICKS_INSTANCE" ] || [ -z "$DATABRICKS_TOKEN" ]; then
  echo "Erreur : DATABRICKS_INSTANCE et/ou DATABRICKS_TOKEN ne sont pas définis."
  exit 1
fi

curl -X POST https://${DATABRICKS_INSTANCE}/api/2.1/jobs/create \
  -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @job_config.json

databricks fs cp train.py dbfs:/FileStore/train.py

