import numpy as np


def lambda_section(a_data, j_data, coefficient_data, l_data):
    i = np.sqrt(j_data / a_data)
    lw = coefficient_data * l_data
    lambda_data = lw / i
    return i, lw, lambda_data


def lambda_critical(e_data, sigma_h):
    lambda_gr = np.pi * np.sqrt(e_data / sigma_h)
    return lambda_gr


def sigma_critical(lambda_data, lambda_critical_data, e_data, sigma_p_data, sigma_h_data):
    if lambda_data > lambda_critical_data:
        sigma_kr = np.pi ** 2 * e_data / lambda_data ** 2
    else:
        sigma_kr = sigma_p_data - (sigma_p_data - sigma_h_data) / lambda_critical_data * lambda_data
    return sigma_kr


def critical_force(sigma_kr_data, a_data):
    p_kr = sigma_kr_data * a_data
    return p_kr


def graph_data(sigma_h_data, e_data, sigma_p_data, a_data, j_data, coefficient_data, l_data):
    lambda_cross = 0
    lambda_critical_data = lambda_critical(e_data, sigma_h_data)

    lambda_rel = lambda_section(a_data, j_data, coefficient_data, l_data)[2]

    lambda_table = []
    sigma_table = []

    while lambda_cross < lambda_rel + 0.1 * lambda_rel:
        sigma = sigma_critical(lambda_cross, lambda_critical_data, e_data, sigma_p_data, sigma_h_data)
        sigma_table.append(sigma)
        lambda_table.append(lambda_cross)
        lambda_cross = lambda_cross + 0.1

    sigma_crit_rel = sigma_critical(lambda_rel, lambda_critical_data, e_data, sigma_p_data, sigma_h_data)

    print(lambda_rel)
    print(sigma_crit_rel)
    p_kr = critical_force(sigma_crit_rel * 0.1, a_data * 10 ** 4)
    print(p_kr)
    return lambda_table, sigma_table, lambda_rel, sigma_crit_rel, p_kr


graph_data(215, 209e3, 235, 6.91 * 10 ** -4, 9.43 * 10 ** -8, 2, 4)
