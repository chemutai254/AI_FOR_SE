from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')

X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)
joblib.dump(clf, MODEL_PATH)
print(f"Saved model to {MODEL_PATH}")
