import mlflow
import mlflow.sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    mlflow.set_experiment("diabetes-linear-regression")
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
        print(f"R² on test set: {score:.4f}")

if __name__ == "__main__":
    main()

