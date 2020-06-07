import numpy as np


def normal_stress(iy, my, z, n, a):
    return n / a + my / iy * z


def shear_stress(tz, sy, b, iy):
    return np.abs(tz * sy / (b * iy))


def alpha_angle_main(sigma_z, sigma_x, tau_xz):
    double_angle = 2 * tau_xz / (sigma_z - sigma_x)
    return np.arctan(double_angle / 2)


def main_stress_func(sigma_z, sigma_x, alpha_main, tau_xz):
    sigma_z_main = (sigma_z + sigma_x) / 2 + (sigma_z - sigma_x) / 2 * np.cos(2 * alpha_main) + tau_xz * np.sin(
        2 * alpha_main)
    sigma_x_main = (sigma_z + sigma_x) / 2 - (sigma_z - sigma_x) / 2 * np.cos(2 * alpha_main) - tau_xz * np.sin(
        2 * alpha_main)
    return sigma_z_main, sigma_x_main


def alpha_angle_shear(sigma_z, sigma_x, tau_xz):
    double_angle = -(sigma_z - sigma_x) / (2 * tau_xz)
    return np.arctan(double_angle / 2)


def main_shear_func(sigma_z, sigma_x, alpha_main, tau_xz):
    tau_max = -(sigma_z - sigma_x) / 2 * np.sin(alpha_main) + tau_xz * np.cos(2 * alpha_main)
    sigma_z_t, sigma_x_t = main_stress_func(sigma_z, sigma_x, alpha_main, tau_xz)
    return tau_max, sigma_z_t, sigma_x_t
