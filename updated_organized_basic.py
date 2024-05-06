import pandas as pd
import numpy as np

def arr_process(arr):
    return np.count_nonzero(arr > -100)

def check(a, b, c):
    if b == 0 and c == 0:
        return 'Not Checked out and not in cart'
    elif b != 0 and c == 0:
        return 'Checked out but not in bag'
    elif b != 0 and c != 0:
        return 'Checked out and in cart'
    elif b == 0 and c != 0:
        return 'Not checked out but in cart'

def main():
    # Load the .pkl file
    data = pd.read_pickle('crunch1/rawData.pkl')

    # Deleting unused timestamp data
    del data['time']

    for key, values in data.items():
        x = arr_process(values[3])
        y = arr_process(values[4])
        z = arr_process(values[5])
        print(check(x, y, z))

if __name__ == "__main__":
    main()
