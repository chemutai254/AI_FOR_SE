# import libraries
import joblib
import streamlit as st


# Define functions and variables
with open("random_forest_model.pkl", "rb") as f:
    classifier = joblib.load(f)

def predict_sleep_disorder(Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP, Diastolic):
    global classifier
    prediction = classifier.predict([[Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP, Diastolic]])
    
    if prediction == 1:
        return "No Sleep Disorder"
    elif prediction == 2:
        return "Insomnia"
    else:
        return "Sleep Apnea"
    
# Sleep Disorder Prediction App
def main():
    
    # st.set_page_config(page_title="Sleep Disorder Predictor")
    
    st.markdown("""
    <style>
        /* Main page background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(to bottom right, #e3f2fd, #bbdefb);
        }

        /* Sidebar background */
        [data-testid="stSidebar"] {
            background: linear-gradient(to bottom, #90caf9, #64b5f6);
        }


        /* Title style */
        .title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 700;
            color: #0d47a1;
            margin-bottom: 20px;
        }

        /* Input labels */
        label, .stSelectbox label, .stNumberInput label {
            color: #1b263b !important;
            font-weight: 600 !important;
        }

        /* Buttons */
        div.stButton > button {
            background-color: #1976d2;
            color: white;
            border-radius: 10px;
            height: 45px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #0d47a1;
            transform: scale(1.02);
        }

        /* Success message */
        .stSuccess {
            color: #004d40 !important;
            background-color: #a5d6a7 !important;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Floating content card
    st.markdown('<div class="floating-card">', unsafe_allow_html=True)

    st.markdown('<div class="title">🩺 Sleep Disorder Prediction App</div>', unsafe_allow_html=True)

    # st.title("Sleep Disorder Prediction App")
    
    # Body
    st.write("Enter the following details to predict sleep disorder:")
    Gender = st.selectbox("Gender: Male, Female", [1, 2])
    Age = st.number_input("Age", min_value=20, max_value=60, value=30)
    Occupation = st.selectbox("Occupation: Software Engineer, Doctor, Sales Representative, Teacher, Nurse, Engineer, Accountant, Scientist, Lawyer, Salesperson, Manager", [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
    Sleep_Duration = st.selectbox("Sleep Duration (hours)", [6.1, 6.2, 5.9, 6.3, 7.8, 6.0, 6.5, 7.6, 7.7, 7.9, 6.4, 7.5, 7.2,
       5.8, 6.7, 7.3, 7.4, 7.1, 6.6, 6.9, 8. , 6.8, 8.1, 8.3, 8.5, 8.4, 8.2])
    Quality_of_Sleep = st.selectbox("Quality of Sleep", [6, 4, 7, 5, 8, 9])
    Physical_Activity_Level = st.selectbox("Physical Activity Level", [42, 60, 30, 40, 75, 35, 45, 50, 32, 70, 80, 55, 90, 47, 65, 85])
    Stress_Level = st.selectbox("Stress Level", [3, 4, 5, 6, 7, 8])
    BMI_Category = st.selectbox("BMI Category: Underweight, Normal, Overweight,  Obese", [1, 2, 3, 4])
    Heart_Rate = st.number_input("Heart Rate", min_value=0, max_value=120, value=70)
    Daily_Steps = st.number_input("Daily Steps", min_value=0, max_value=20000, value=10000)
    Systolic_BP = st.number_input("Systolic Blood Pressure", min_value=90, max_value=180, value=120)
    Diastolic_BP = st.number_input("Diastolic Blood Pressure", min_value=60, max_value=120, value=80)

    # Predict
    if st.button("Predict"):
        result = predict_sleep_disorder(Gender, Age, Occupation, Sleep_Duration, Quality_of_Sleep, Physical_Activity_Level, Stress_Level, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP, Diastolic_BP)
        st.success(f"The predicted sleep disorder is: {result}")
        
    # Close floating card
    st.markdown('</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
