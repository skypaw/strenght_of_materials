import numpy as np


def circular_stress(j_y_circular, j_z_circular, m_s_func, rho_func):
    j_0 = j_y_circular + j_z_circular
    r = 0
    tau_x_table = []
    rho_table = []
    while r <= rho_func:
        tau_x = np.abs(m_s_func) / j_0 * r

        tau_x_table.append(tau_x)
        rho_table.append(r)

        print(r)
        r = r + rho_func / 100
    return tau_x_table, rho_table
