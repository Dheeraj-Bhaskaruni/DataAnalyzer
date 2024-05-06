import numpy as np
from scipy.interpolate import RegularGridInterpolator
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
with open('../crunch1/rawData.pkl', 'rb') as f:
    data = pickle.load(f)

# Assuming data['graph'] is your feature array and data['labels'] contains binary labels
current_data = data['graph']
labels = data['labels']

# Create an interpolation function from the original data
x = np.linspace(0, 1, current_data.shape[0])
y = np.linspace(0, 1, current_data.shape[1])
interpolator = RegularGridInterpolator((x, y), current_data, method='linear')

# Define the new grid
new_x = np.linspace(0, 1, 6)
new_y = np.linspace(0, 1, 2048)
new_grid = np.meshgrid(new_x, new_y, indexing='ij')

# Interpolate data
points = np.vstack([new_grid[0].ravel(), new_grid[1].ravel()]).T
interpolated_data = interpolator(points).reshape(6, 2048)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(interpolated_data, labels, test_size=0.2, random_state=42)

# Initialize and train the classifier
classifier = LogisticRegression(max_iter=1000)
classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
