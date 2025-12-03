# Automatic Diagnosis of Breast Cancer

## Description
This project utilizes machine learning to assist in the diagnosis of breast cancer. By analyzing features computed from digitized images of a fine needle aspirate (FNA) of a breast mass, the model classifies tumors as either Malignant or Benign.

## Key Objectives
- **Data Preprocessing**: Cleaning, label encoding, and scaling the dataset.
- **Model Training**: Implementing a Random Forest Classifier to predict diagnosis.
- **Evaluation**: Assessing model performance using accuracy, F1-score, and confusion matrix.

## Dataset
- **Name**: Breast Cancer Wisconsin (Diagnostic) Data Set.
- **Source**: `data.csv` (included in directory).
- **Target**: Diagnosis (M = Malignant, B = Benign).

## Tech Stack
- **Language**: Python.
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.

## Project Structure
- `breast_diagnosis.ipynb`: The main Jupyter Notebook containing the complete workflow from data loading to evaluation.
- `data.csv`: The dataset used for training and testing.

## How to Run
1.  Ensure you have the required libraries installed (`pip install pandas numpy scikit-learn matplotlib seaborn`).
2.  Open `breast_diagnosis.ipynb` in Jupyter Notebook or Google Colab.
3.  Run the cells sequentially to reproduce the analysis and model results.