# deploy_databricks.sh
#!/bin/bash

curl -X POST https://${DATABRICKS_INSTANCE}/api/2.1/jobs/create \
  -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d @job_config.json

