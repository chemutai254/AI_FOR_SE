import joblib
import streamlit as st
import numpy as np

# Load the model
with open('iris_model.pkl', 'rb') as f:
    classifier = joblib.load(f)
    
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