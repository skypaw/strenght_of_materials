import numpy as np


def circular_stress(j_y_circular, j_z_circular, m_s_func, rho_func):
    j_0 = j_y_circular + j_z_circular
    tau_x = np.abs(m_s_func) / j_0 * rho_func
    return tau_x
