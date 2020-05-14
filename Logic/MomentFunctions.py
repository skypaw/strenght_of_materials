def uniformly_distributed_load_beam(l_data, q_data, interval):
    x = 0
    while x <= l_data:
        support_l = q_data * l_data / 2
        moment = support_l * x - q_data * x ** 2 / 2

        x = x + interval

        print(x, " ", moment)
    return moment


def uniformly_distributed_load_hanger(l_data, q_data, interval):
    x = 0
    while x <= l_data:
        support_l = q_data * l_data
        moment_l = -q_data * l_data ** 2 / 2

        moment = moment_l + support_l * x - q_data * x ** 2 / 2

        x = x + interval

        print(x, " ", moment)
    return moment


def point_load_beam(l_data, p_data, interval, x_data):
    x = 0
    while x <= l_data:
        support_l = q_data * l_data / 2
        moment = support_l * x - q_data * x ** 2 / 2

        x = x + interval

        print(x, " ", moment)
    return moment


uniformly_distributed_load_hanger(500, 30, 1)
