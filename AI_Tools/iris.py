import sys
import os

try:
    import joblib
except ImportError:
    print("Missing required package 'joblib'. Install with: python3 -m pip install joblib scikit-learn")
    sys.exit(1)

import streamlit as st
import numpy as np

# Load the model (resolve path relative to this file)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')
if not os.path.exists(MODEL_PATH):
    print(f"Model file not found at {MODEL_PATH}. Place iris_model.pkl next to iris.py")
    sys.exit(1)

classifier = joblib.load(MODEL_PATH)
    
def predictor(sepal_length, sepal_width, petal_length, petal_width):
    global classifier
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = classifier.predict(features)
    
    if prediction == 0:
        return "Iris-setosa"
    elif prediction == 1:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"

# Interface
def main():
    st.title("Iris Flower Species Prediction")
    st.write("Enter the features of the iris flower to predict its species.")

    # Input features
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0)

    # Predict button
    if st.button("Predict"):
        species = predictor(sepal_length, sepal_width, petal_length, petal_width)
        st.success(f"The predicted species is: {species}")
        
    st.write("Developed by Nancy Chemutai")
# Run the app with: streamlit run iris.py
if __name__ == "__main__":
    main()