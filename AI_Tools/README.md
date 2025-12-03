# AI Tools: Iris Flower Classification

## Description
A fundamental machine learning project that demonstrates how to build, train, and save a model to classify Iris flowers into their respective species based on physical measurements.

## Key Objectives
- Load and explore the Iris dataset.
- Train a machine learning model (e.g., Logistic Regression or Decision Tree).
- Save the trained model for future use.

## Dataset
- **Name**: Iris Dataset.
- **Source**: `Iris.csv` (included in directory).
- **Features**: Sepal Length, Sepal Width, Petal Length, Petal Width.
- **Target**: Species (Setosa, Versicolor, Virginica).

## Tech Stack
- **Language**: Python.
- **Libraries**: Scikit-learn, Pandas, Joblib/Pickle.

## Project Structure
- `iris.ipynb`: Jupyter Notebook containing data analysis and model training steps.
- `iris.py`: Python script version of the model training logic.
- `train_iris_model.py`: Script to train and save the model.
- `iris_model.pkl`: Serialized trained model file.
- `requirements.txt`: List of dependencies.

## How to Run
1.  Install dependencies: `pip install -r requirements.txt` (if available) or `pip install pandas scikit-learn`.
2.  Run the notebook: Open `iris.ipynb` in Jupyter and execute cells.
3.  Run the script: `python iris.py` or `python train_iris_model.py`.
