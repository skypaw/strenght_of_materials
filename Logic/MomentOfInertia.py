def z_centre_of_gravity(t_f1, b_f1, tw, hw, t_f2, b_f2):
    z_c = (t_f1 * b_f1 * (t_f1 / 2 + hw + t_f2) + tw * hw * (hw / 2 + t_f2) + t_f2 * b_f2 * (t_f2 / 2)) / (
            t_f1 * b_f1 + tw * hw + t_f2 * b_f2)
    return z_c


def i_beam(t_f1, b_f1, tw, hw, t_f2, b_f2):
    z_c = z_centre_of_gravity(t_f1, b_f1, tw, hw, t_f2, b_f2)
    i_y = (b_f1 * t_f1 ** 3 / 12 + b_f1 * t_f1 * (t_f1 / 2 + hw + t_f2 - z_c) ** 2) + (
            tw * hw ** 3 / 12 + tw * hw * (hw / 2 + t_f2 - z_c) ** 2) + (
                  b_f2 * t_f2 ** 3 / 12 + b_f2 * t_f2 * (t_f2 / 2 - z_c) ** 2)

    return i_y

# print(i_beam(1.6, 25, 1.2, 76, 1.8, 28))
