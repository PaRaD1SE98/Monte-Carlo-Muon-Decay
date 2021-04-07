import random
from initial_values import *
from scipy.integrate import quad


def max_p():
    li = []
    li_value = []
    n = 5000
    for i in range(1, n + 1):
        li.append(i / (n / 50))
        li_value.append(P_E_e(i / (n / 50)))
    # print(max(li_value))
    return max(li_value)


def generate_valid_E_e(mu_c2):
    E_e = float(random.randrange(0, mu_c2 / 2 * 10000)) / 10000
    random_seed = random.uniform(0, 0.04)
    while random_seed > P_E_e(E_e):
        # print(E_e, random_seed, P_E_e(E_e))
        E_e = float(random.randrange(0, mu_c2 / 2 * 10000)) / 10000
        random_seed = random.uniform(0, 0.04)
    return E_e


def P_E_e(E_e):
    Ee = E_e

    def P_E_e_initial(E_e=Ee):
        return (mu_c2 * E_e) ** 2 * (3 - 4 * E_e / mu_c2)

    i = quad(P_E_e_initial, 0, mu_c2 / 2)[0]
    c = 1 / i
    return c * P_E_e_initial(E_e=Ee)


class MuonDecay:
    def __init__(self, mu_c2, theta_max, E_e=None, r=None, phi=None, theta=None, z_0=None):
        """
        Generate a MUON.

        :param mu_c2: Rest mass of the MUON (MeV)
        :param theta_max: the max value of position theta (degree)
        """
        self.mu_c2 = mu_c2
        self.theta_max = theta_max

        if E_e is None:
            # E_e = float(random.randrange(0, self.mu_c2 / 2 * 10000)) / 10000
            E_e = generate_valid_E_e(self.mu_c2)
        if r is None:
            r = float(random.randrange(0, R / 2 * 10000)) / 10000
        if phi is None:
            phi = float(random.randrange(0, 360 * 10000)) / 10000
        if theta is None:  # get_l_esc ZeroDivisionError
            theta = float(random.randrange(1, self.theta_max * 10000)) / 10000
        if z_0 is None:
            z_0 = float(random.randrange(0, t_plate * 10000)) / 10000
        self.E_e = E_e
        self.r = r
        self.phi = phi
        self.theta = theta
        self.z_0 = z_0
