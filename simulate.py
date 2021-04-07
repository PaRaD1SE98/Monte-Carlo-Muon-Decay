from models import MuonDecay
from initial_values import *
import matplotlib.pyplot as plt
import numpy as np
import math
from data_handler import plot_data


def get_l():
    l = X0 * np.log(1 + MUON.E_e / E_crit)
    if l > get_l_esc():
        return get_l_esc()
    else:
        return l


def get_l_esc():
    r = MUON.r
    phi = MUON.phi
    cos_phi = math.cos(math.radians(phi))
    sin_theta = math.sin(math.radians(MUON.theta))
    sqrt = math.sqrt
    tp = t_plate
    tg = t_gap
    l_esc = ((-r * math.cos(phi) + sqrt(r ** 2 * cos_phi ** 2 + (R ** 2 - r ** 2))) / sin_theta) * (tp / (tp + tg))
    return l_esc


def get_n_s():
    n_s = 1 + math.floor((get_l() * math.cos(math.radians(MUON.theta)) - MUON.z_0) / t_plate)
    return n_s


MUON_DATA_R = []
MUON_DATA_PHI = []
MUON_DATA_THETA = []
MUON_DATA_L = []
MUON_DATA_L_ESC = []
MUON_DATA_Z_0 = []
MUON_DATA_N_S = []
MUON_DATA_E_e = []
for i in range(RUN_NUM):
    MUON = MuonDecay(
        mu_c2=mu_c2,
        theta_max=theta_max
    )
    MUON_DATA_R.append(MUON.r)
    MUON_DATA_PHI.append(MUON.phi)
    MUON_DATA_THETA.append(MUON.theta)
    MUON_DATA_Z_0.append(MUON.z_0)
    MUON_DATA_L.append(get_l())
    MUON_DATA_L_ESC.append(get_l_esc())
    MUON_DATA_N_S.append(get_n_s())
    MUON_DATA_E_e.append(MUON.E_e)

BAR_NUM = []
BAR_QUAN = []
for i in MUON_DATA_N_S:
    if i not in BAR_NUM:
        BAR_NUM.append(i)

for i in BAR_NUM:
    q = MUON_DATA_N_S.count(i)
    BAR_QUAN.append(q)

try:
    o = BAR_NUM.index(0)
    BAR_NUM.remove(0)
    del BAR_QUAN[o]
    N_SIM_N_S = len(MUON_DATA_N_S) - MUON_DATA_N_S.count(0)
except ValueError:
    N_SIM_N_S = len(MUON_DATA_N_S) - MUON_DATA_N_S.count(0)

DATA_DICT = {}
for i, j in zip(BAR_NUM, BAR_QUAN):
    DATA_DICT[i] = j

sorted_data = {}
for i in sorted(DATA_DICT):
    sorted_data[i] = DATA_DICT[i]

if __name__ == '__main__':
    print('\033[32mthe number of times it decayed:\033[0m{}'.format(N_SIM_N_S))
    print('\033[32mthe number of times it didn`t decay:\033[0m{}'.format(MUON_DATA_N_S.count(0)))
    print('\033[32mthe number of times for each event:\033[0m{}'.format(sorted_data))
    plot = plt.bar(BAR_NUM, BAR_QUAN, 1)
    plt.bar_label(plot)
    plt.xlabel('Number of Sparks')
    plt.ylabel('Number of Muon Decays')
    plot_data()
    plt.show()
