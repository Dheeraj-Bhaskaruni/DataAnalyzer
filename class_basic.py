import pandas as pd
import numpy as np


class DataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_pickle(file_path)

    def arr_process(self, arr):
        return np.count_nonzero(arr > -100)

    def check(self, a, b, c):
        if b == 0 and c == 0:
            return 'Not Checked out and not in cart'
        elif b != 0 and c == 0:
            return 'Checked out but not in bag'
        elif b != 0 and c != 0:
            return 'Checked out and in cart'
        elif b == 0 and c != 0:
            return 'Not checked out but in cart'

    def analyze_data(self):
        # Deleting unused timestamp data
        del self.data['time']

        for key, values in self.data.items():
            x = self.arr_process(values[3])
            y = self.arr_process(values[4])
            z = self.arr_process(values[5])
            print(self.check(x, y, z))


# Usage:
analyzer = DataAnalyzer('crunch1/rawData.pkl')
analyzer.analyze_data()
