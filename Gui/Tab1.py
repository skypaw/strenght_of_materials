from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import Logic.MomentFunctions
import Logic.StressFunctions


def test(master):
    desc_1 = Label(master, text="L", padx=10)
    desc_2 = Label(master, text="q", padx=10)

    desc_1.grid(row=1)
    desc_2.grid(row=2)

    units_1 = Label(master, text="[m]", padx=10)
    units_2 = Label(master, text="[kN/m]", padx=10)

    units_1.grid(row=1, column=3)
    units_2.grid(row=2, column=3)

    data_1 = Entry(master)
    data_2 = Entry(master)

    data_1.grid(row=1, column=2)
    data_2.grid(row=2, column=2)

    test = Frame(master)
    test.grid(row=1, rowspan=30, column=6)

    figure3 = plt.Figure(figsize=(3, 2))

    moment_table = []
    length_table = []

    def onclick():
        l = float(data_1.get().replace(',', '.'))
        q = float(data_2.get().replace(',', '.'))

        if len(moment_table) != 0:
            moment_table.clear()
            length_table.clear()

        interval = Logic.MomentFunctions.interval_func(l)
        moment, length = Logic.MomentFunctions.uniformly_distributed_load_beam(l, q, interval)

        moment_table.extend(moment)
        length_table.extend(length)

        figure3.clf()
        ax3 = figure3.add_subplot(111)
        ax3.scatter(length_table, moment_table)
        scatter3.draw()

    scatter3 = FigureCanvasTkAgg(figure3, test)

    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button5 = Button(master, text="Calculate", command=onclick)
    button5.grid(row=10, columnspan=3, pady=10)

    normal_stress = []

    def onclick2():
        h = 30
        normal = 20
        if len(normal_stress) != 0:
            normal_stress.clear()

        for i in moment_table:
            normal_s = Logic.StressFunctions.normal_stress(400, i, h, normal, 30)
            normal_stress.append(normal_s)
        print(normal_stress)

    button6 = Button(master, text="testowo", command=onclick2)
    button6.grid(row=11)
