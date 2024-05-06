import pickle

# Load the data from the pickle file
with open('rawData.pkl', 'rb') as f:
    data = pickle.load(f)

# Printing keys
for key in data.keys():
    print(key)
