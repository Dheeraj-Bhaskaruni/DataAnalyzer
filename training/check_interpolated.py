import numpy as np
from scipy.interpolate import RegularGridInterpolator
import pickle

with open('../crunch1/rawData.pkl', 'rb') as f:
    data = pickle.load(f)

# Assuming data['graph'] is your 2D array from the pickle file
current_data = data['graph']

# Create an original grid based on the current shape
x = np.linspace(0, 1, current_data.shape[0])
y = np.linspace(0, 1, current_data.shape[1])

# Function to interpolate
interpolator = RegularGridInterpolator((x, y), current_data, method='linear')

# New grid dimensions
new_x = np.linspace(0, 1, 6)  # new dimension 1
new_y = np.linspace(0, 1, 2048)  # new dimension 2
new_grid = np.meshgrid(new_x, new_y, indexing='ij')

# Flatten the new grid for the interpolator and then reshape the results
points = np.vstack([new_grid[0].ravel(), new_grid[1].ravel()]).T
new_data = interpolator(points).reshape(6, 2048)

# Check first and last values
first_value_matches = current_data[0, 0] == new_data[0, 0]
last_value_matches = current_data[-1, -1] == new_data[-1, -1]

print("First values match:", first_value_matches)
print("Last values match:", last_value_matches)
print(new_data.shape)  # This should print (6, 2048)
