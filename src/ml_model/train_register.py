import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    mlflow.set_experiment("/Users/anass.b.compt@gmail.com/diabetes-linear-regression")

    with mlflow.start_run() as run:
        data = load_diabetes(as_frame=True)
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )
        model = LinearRegression()
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)

        mlflow.log_metric("r2_score", score)

        # Enregistrement dans le Model Registry
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name="model_name_1"  # <-- Ce nom sera utilisé dans run.py
        )

        print(f"R² on test set: {score:.4f}")
        print(f"Run ID: {run.info.run_id}")

if __name__ == "__main__":
    main()
