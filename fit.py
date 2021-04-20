from data_handler import DATADIR, DATASET_NUM
from numpy import genfromtxt
import matplotlib.pyplot as plt
from initial_values import RUN_NUM, START, STOP, INTERVAL
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


def total_error():
    error = []
    for i in data()[1]:
        error.append(np.sqrt(i * RUN_NUM / DATASET_NUM))
    total = sum(error) ** 2
    return total


print('errorbar:', total_error())


def plot_residual(m):
    d = {}
    for i, j in zip(data()[0], data()[1]):
        d[int(i)] = int(j)
    s = simulate(m)
    # print(d)
    # print(s)
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
    # print(rx)
    # print(ry)
    # print(sum_r)
    return sum_r


DATA_POINTS = int((STOP - START) / INTERVAL + 1)


def draw():
    print('total points:', DATA_POINTS)
    m = np.linspace(START, STOP, DATA_POINTS)
    r = []
    current_point = 0
    for i in m:
        r.append(plot_residual(i))
        current_point += 1
        print('\rcurrent point:', current_point, end='')
    print('\nminimum mu_c2:', m[r.index(min(r))])
    plt.errorbar(m, r, fmt='-ok', lw=1, yerr=0)
    # plt.errorbar(m, r, fmt='-ok', lw=1, yerr=total_error())
    plt.xlabel(r'$m_μc^2(MeV)$')
    plt.ylabel('Sum of Squared Residuals')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    draw()
