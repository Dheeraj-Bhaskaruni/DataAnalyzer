import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, file_path):
        self.data = pd.read_pickle(file_path)

    def arr_process(self, arr):
        return np.count_nonzero(arr > -100)

    def check(self, a, b, c):
        if b != 0 and c != 0:
            return 'Checked_out_and_in_bag'
        elif b != 0 and c == 0:
            return 'Checked_out_but_not_in_bag'
        elif b == 0 and c != 0:
            return 'Not_checked_out_but_in_bag'
        elif b == 0 and c == 0:
            return 'Not_checked_out_and_not_in_bag'

    def analyze_data(self):
        # Deleting unused timestamp data
        del self.data['time']

        # Initialize counts
        TP = TN = FP = FN = 0

        for key, values in self.data.items():
            x = self.arr_process(values[3])
            y = self.arr_process(values[4])
            z = self.arr_process(values[5])
            true_label = self.check(x, y, z)

            if true_label == 'Checked_out_and_in_bag':
                TP += 1
            elif true_label == 'Checked_out_but_not_in_bag':
                FP += 1
            elif true_label == 'Not_checked_out_but_in_bag':
                FN += 1
            elif true_label == 'Not_checked_out_and_not_in_bag':
                TN += 1

        cm = [[TN, FP], [FN, TP]]

        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Checked Out', 'Checked Out'], yticklabels=['Not In Bag', 'In Bag'])
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title('Confusion Matrix')
        plt.show()

# Usage:
analyzer = DataAnalyzer('crunch4/rawData.pkl')
analyzer.analyze_data()
