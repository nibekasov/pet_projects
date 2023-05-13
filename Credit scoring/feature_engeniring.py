import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('credit_data.csv')

# Explore and visualize the data
print(df.describe())
sns.pairplot(df)

# Feature engineering
df['debt_to_income_ratio'] = df['debt'] / df['income']
df['credit_to_income_ratio'] = df['savings'] / df['income']
df['credit_history_squared'] = df['credit_history'] ** 2

# Feature selection
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
relevant_features = corr.index[abs(corr['approved']) >= 0.2]
df = df[relevant_features]

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X = df.drop('approved', axis=1)
y = df['approved']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Evaluate the model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
y_pred = clf.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1 score:', f1_score(y_test, y_pred))
print('Confusion matrix:', confusion_matrix(y_test, y_pred))
