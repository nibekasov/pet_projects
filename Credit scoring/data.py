from sklearn.datasets import make_classification
import pandas as pd

# Generate synthetic data with 1000 samples, 5 features, and 2 classes
X, y = make_classification(n_samples=1000, n_features=5, n_classes=2, random_state=42)

# Convert the numpy arrays to a pandas dataframe
data = pd.DataFrame(X, columns=['age', 'income', 'debt', 'savings', 'credit_history'])
data['approved'] = y

# Save the data to a CSV file
data.to_csv('credit_data.csv', index=False)
