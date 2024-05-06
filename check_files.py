import pandas as pd
import numpy as np

# Load the .pkl file
data = pd.read_pickle('crunch1/rawData.pkl')

# Now you can work with 'data' as a pandas DataFrame

# Access and print values of a specific key from the dictionary
key_to_check = 'ABBC00000000000000000002'
values = data[key_to_check]
print(len(values[1]))
# index starting of being greater than 0
# index_greater_than_neg100 = np.argmax(values[5] > -100)
# print(index_greater_than_neg100)
# list of indexes where it is being greater than 0
print('list for array 5')
array_5_high = np.where(values[4] > -80)[0]
print(array_5_high)
print('list for array 6')
indices_greater_than_zero = np.where(values[5] > -80)[0]
print(indices_greater_than_zero)

# for j in range(len(values)):
#     count = 0
#     for i in range(len(values[j])):
#         if values[j][i] > -100:
#             count = count + 1
#     print(count)
