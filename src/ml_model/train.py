import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Set to True to save model locally
RUN_LOCAL = True
LOCAL_MODEL_DIR = "model"
LOCAL_MODEL_PATH = os.path.join(LOCAL_MODEL_DIR, "diabetes_model.pkl")
LOCAL_MLFLOW_MODEL_PATH = os.path.join(LOCAL_MODEL_DIR, "mlflow_diabetes_model")

def main():
    #mlflow.set_experiment("diabetes-linear-regression")
    mlflow.set_experiment("/Users/anass.b.compt@gmail.com/diabetes-linear-regression")

    with mlflow.start_run():
        data = load_diabetes(as_frame=True)
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        mlflow.log_metric("r2_score", score)
        mlflow.sklearn.log_model(model, "model")
        print(f"R\u00b2 on test set: {score:.4f}")

        if RUN_LOCAL:
            os.makedirs(LOCAL_MODEL_DIR, exist_ok=True)
            joblib.dump(model, LOCAL_MODEL_PATH)
            mlflow.sklearn.save_model(model, LOCAL_MLFLOW_MODEL_PATH)
            print(f"Model saved locally at {LOCAL_MODEL_PATH} and {LOCAL_MLFLOW_MODEL_PATH}")

if __name__ == "__main__":
    main()

