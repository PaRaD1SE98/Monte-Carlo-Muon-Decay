from numpy import genfromtxt
import numpy as np
from initial_values import RUN_NUM
import matplotlib.pyplot as plt


def plot_data():
    x = []
    y = []
    with open('/home/parad1se/PycharmProjects/MonteCarloMuonMass/datapoints.csv') as f:
        data = genfromtxt(f, delimiter=',')
        for i in data:
            # print(i)
            x.append(i[0])
            y.append(i[1] * RUN_NUM / 43)
        # print(x)
        # print(y)

    errorbar = lambda x: np.sqrt(x)
    for i, j in zip(x, y):
        plt.errorbar(i, j, fmt="ok", yerr=errorbar(j * RUN_NUM / 43))
