from models import P_E_e
from matplotlib import pyplot as plt
from models import MuonDecay
from initial_values import *


def P_E_e_initial(E_e):
    return (mu_c2 * E_e) ** 2 * (3 - 4 * E_e / mu_c2)


li = []
li_value = []
n = int(mu_c2 / 2)
for i in range(1, n + 1):
    li.append(i)
    li_value.append(P_E_e(i))
MAX = max(li_value)

ax1 = plt.subplot(211)
ax2 = plt.subplot(212, sharex=ax1)
print(max(li_value))
ax1.plot(li, li_value, "k")
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel(r'P$(E_e)$')


MUON_E_e = []
for i in range(100000):
    MUON = MuonDecay(
        mu_c2=mu_c2,
        theta_max=theta_max
    )
    MUON_E_e.append(MUON.E_e)

ax2.hist(MUON_E_e, bins=100)
ax2.set_ylabel(r'Quantity of $E_e$')
ax2.set_xlabel(r'$E_e$')
plt.tight_layout()
plt.show()
