from numpy import genfromtxt
import numpy as np
from initial_values import RUN_NUM
import matplotlib.pyplot as plt
import os

BASEDIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(BASEDIR, 'datapoints.csv')


def plot_data():
    x = []
    y = []
    with open(DATADIR) as f:
        data = genfromtxt(f, delimiter=',')
        for i in data:
            # print(i)
            x.append(i[0])
            y.append(i[1] * RUN_NUM / 43)
        # print(a)
        # print(y)

    error_bar = lambda a: np.sqrt(a)
    for i, j in zip(x, y):
        plt.errorbar(i, j, fmt="ok", yerr=error_bar(j * RUN_NUM / 43))
