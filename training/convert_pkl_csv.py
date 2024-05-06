import pickle

# Load the data from the pickle file
with open('../crunch1/rawData.pkl', 'rb') as f:
    data = pickle.load(f)

# Accessing the first element of each array for each key
first_row = {key: data[key][0] for key in data.keys()}

# Printing the first row
for key, value in first_row.items():
    print(f"First row of '{key}': {value}")
