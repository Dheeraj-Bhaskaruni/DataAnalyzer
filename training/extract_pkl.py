import pickle
import numpy as np

with open('../crunch1/rawData.pkl', 'rb') as f:
    data = pickle.load(f)

print(data.keys())