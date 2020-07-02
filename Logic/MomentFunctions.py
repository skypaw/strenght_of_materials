def interval_func(l_data):
    return l_data / 100


def uniformly_distributed_load_beam(l_data, q_data, interval):
    moment_func_uniformly = []
    x_uniformly_table = []
    x_uniformly = 0
    while x_uniformly <= l_data:
        support_l = q_data * l_data / 2
        moment_interval = support_l * x_uniformly - q_data * x_uniformly ** 2 / 2
        moment_func_uniformly.append(moment_interval)
        x_uniformly_table.append(x_uniformly)

        x_uniformly = x_uniformly + interval

        print(x_uniformly, " ", moment_interval)
    return moment_func_uniformly, x_uniformly_table


def uniformly_distributed_load_hanger(l_data, q_data, interval):
    moment_func_hanger = 0
    x_hanger = 0
    while x_hanger <= l_data:
        support_l = q_data * l_data
        moment_l = -q_data * l_data ** 2 / 2

        moment_func_hanger = moment_l + support_l * x_hanger - q_data * x_hanger ** 2 / 2

        x_hanger = x_hanger + interval

        print(x_hanger, " ", moment_func_hanger)
    return moment_func_hanger


def point_load_beam(l_data, q_data, interval):
    moment_func_point = 0
    x_point = 0
    while x_point <= l_data:
        support_l = q_data * l_data / 2
        moment_func_point = support_l * x_point - q_data * x_point ** 2 / 2

        x_point = x_point + interval

        print(x_point, " ", moment_func_point)
    return moment_func_point


#uniformly_distributed_load_hanger(500, 30, 1)
