import pickle

# Load the PKL file
with open('../crunch1/rawData.pkl', 'rb') as f:
    data = pickle.load(f)

print(data.shape)
