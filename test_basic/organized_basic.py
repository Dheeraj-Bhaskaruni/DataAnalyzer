import pandas as pd
import numpy as np

# Load the .pkl file
data = pd.read_pickle('../crunch1/rawData.pkl')


def arr_process(arr):
    arr_high = np.where(arr > -100)[0]
    return len(arr_high)

def check(a,b,c):
    if b == 0 and c == 0:
        print('Not Checked out and not in cart')
    elif b != 0 and c == 0:
        print('Checked out but not in bag')
    elif b != 0 and c != 0:
        print('Checked out and in cart')
    elif b == 0 and c != 0:
        print('Not checked out but in cart')

#deleting unused timestamp data
del data['time']
keys = data.keys()
for key in keys:
    x = arr_process(data[key][3])
    y = arr_process(data[key][4])
    z = arr_process(data[key][5])
    check(x,y,z)
