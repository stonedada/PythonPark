import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer, load_iris

# Load the breast cancer dataset
breast_cancer = load_breast_cancer()

# Split the data into features (X) and target variable (y)
X = breast_cancer.data
y = breast_cancer.target

# -----------also can load your own data ------------------
# df = pd.read_csv('path/to/your/data.csv')
# X = df.drop(['target_variable_column_name'], axis=1)
# y = df['target_variable_column_name']

# Create a logistic regression classifier
clf = LogisticRegression(random_state=0)

# Perform 5-fold cross-validation
scores = cross_val_score(clf, X, y, cv=5)

# Print the cross-validation scores
print("Cross-validation scores: {}".format(scores))
