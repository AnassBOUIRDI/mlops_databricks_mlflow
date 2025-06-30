FROM python:3.9-slim

WORKDIR /app

COPY train.py /app/train.py

RUN pip install --no-cache-dir mlflow scikit-learn pandas

CMD ["python", "train.py"]

