from numpy import genfromtxt
import numpy as np
from initial_values import RUN_NUM
import matplotlib.pyplot as plt
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(BASEDIR, 'datapoints.csv')
DATASET_NUM = 43


def plot_data():
    x = []
    y = []
    with open(DATADIR) as f:
        data = genfromtxt(f, delimiter=',')
        for i in data:
            # print(i)
            x.append(i[0])
            y.append(i[1])
        # print(a)
        # print(y)

    def error_bar(a):
        return np.sqrt(a)

    for i, j in zip(x, y):
        # plt.errorbar(i, j, fmt="ok", yerr=error_bar(j))
        plt.errorbar(i, j * RUN_NUM / DATASET_NUM, fmt="ok", yerr=error_bar(j) * (RUN_NUM / DATASET_NUM))


if __name__ == '__main__':
    plot_data()
    plt.xlabel('Number of Sparks')
    # plt.ylabel(fr'Number of Muon Decays $x{int(1)}$')
    plt.ylabel(fr'Number of Muon Decays $x{int(RUN_NUM/DATASET_NUM)}$')
    plt.tight_layout()
    plt.show()
