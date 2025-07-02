FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ml_model/ /app/src/ml_model/
WORKDIR /app/src/ml_model

CMD ["python", "train.py"]

