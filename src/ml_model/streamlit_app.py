import streamlit as st
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_diabetes

# Editable local model path (update as needed)
MODEL_PATH = "model/mlflow_diabetes_model"

# Load diabetes feature names
feature_names = load_diabetes().feature_names

def main():
    st.title("Diabetes Prediction App")
    st.write("Input patient data to predict diabetes progression.")

    # User input for each feature
    user_input = {}
    for feature in feature_names:
        user_input[feature] = st.number_input(f"{feature}", value=0.0, format="%.4f")

    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    if st.button("Predict"):
        with st.spinner("Loading model and predicting..."):
            try:
                model = mlflow.sklearn.load_model(MODEL_PATH)
                prediction = model.predict(input_df)
                st.success(f"Predicted diabetes progression: {prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main() 