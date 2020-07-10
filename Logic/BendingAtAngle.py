import numpy as np


def bending_moments(alpha_func, m_max):
    m_y = m_max * np.cos(alpha_func*np.pi/180)
    m_z = m_max * np.sin(alpha_func*np.pi/180)
    return m_y, m_z


def neutral_axis(m_y_func, m_z_func, j_y_func, j_z_func, y_neutral):
    z_neutral = m_z_func * j_y_func / (m_y_func * j_z_func) * y_neutral
    return z_neutral
