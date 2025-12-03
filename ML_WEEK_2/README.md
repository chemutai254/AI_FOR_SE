# Sleep Disorder Prediction

## Description
This project aims to predict the presence of sleep disorders (such as Insomnia and Sleep Apnea) based on an individual's lifestyle and health metrics. It addresses issues aligned with UN SDG 3 (Good Health and Well-being).

## Key Objectives
- Analyze the relationship between lifestyle habits (e.g., steps, physical activity) and sleep health.
- Train and compare multiple machine learning models to predict sleep disorders.

## Dataset
- **Name**: Sleep Health and Lifestyle Dataset.
- **Source**: [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset).
- **Features**: Gender, Age, Occupation, Sleep Duration, Quality of Sleep, Physical Activity Level, Stress Level, BMI Category, Blood Pressure, Heart Rate, Daily Steps.
- **Target**: Sleep Disorder (None, Insomnia, Sleep Apnea).

## Key Findings
- Strong correlation between **Quality of Sleep** and **Sleep Duration**.
- Strong correlation between **Daily Steps** and **Physical Activity Level**.
- Strong correlation between **Stress Level** and **Heart Rate**.

## Tech Stack
- **Language**: Python.
- **Libraries**: Scikit-learn, Pandas, Matplotlib, Seaborn.
- **Models**: Support Vector Machine (SVM), Decision Tree, Random Forest.

## Project Structure
- `sleep_disorder_prediction.ipynb`: Main notebook for EDA and model training.
- `sleep_disorder_app.py`: Python script for the application logic.
- `Sleep_health_and_lifestyle_dataset.csv`: Dataset file.
- `*.pkl`: Serialized model files (Random Forest, SVM, Decision Tree).
- `images/`: Directory containing visualization plots.

## How to Run
1.  **Analysis**: Open `sleep_disorder_prediction.ipynb` to view the exploratory data analysis and model training.
2.  **Application**: Run `python sleep_disorder_app.py` to launch the prediction application (if applicable/configured).