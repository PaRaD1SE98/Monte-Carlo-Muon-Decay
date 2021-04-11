from data_handler import DATADIR, DATASET_NUM
from numpy import genfromtxt
import matplotlib.pyplot as plt
from initial_values import RUN_NUM
from simulate import simulate
import numpy as np


def data():
    x = []
    y = []
    with open(DATADIR) as f:
        d = genfromtxt(f, delimiter=',')
        for i in d:
            x.append(i[0])
            y.append(i[1] * RUN_NUM / DATASET_NUM)
    return x, y


def plot_residual(m):
    d = {}
    for i, j in zip(data()[0], data()[1]):
        d[int(i)] = int(j)
    s = simulate(m)
    print(d)
    print(s)
    rx = []
    ry = []
    for i in d:
        rx.append(i)
    for j in s:
        if j in rx:
            ry.append((s[j] - d[j]) ** 2)
        # else:
        #     ry.append(0)
    for k in d:
        if k not in s:
            ry.append(0)
    count = ry.count(0)
    # print(count)
    for i in range(count):
        # print(i)
        ry[-(i + 1)] = (d[len(d) + 2 - i]) ** 2
    sum_r = sum(ry)
    print(rx)
    print(ry)
    print(sum_r)
    return sum_r


def draw():
    m = np.linspace(60, 140, 17)
    r = []
    for i in m:
        r.append(plot_residual(i))
    plt.plot(m, r, '-ok')
    plt.xlabel(r'$m_μc^2(MeV)$')
    plt.ylabel('Sum of Squared Residuals')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    draw()
