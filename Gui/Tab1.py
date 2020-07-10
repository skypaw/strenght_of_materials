from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import Logic.MomentFunctions
import Logic.StressFunctions
import Logic.MomentOfInertia


def tab1(master):
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

    graph_frame = Frame(master)
    graph_frame.grid(row=1, rowspan=16, column=6)

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

    scatter3 = FigureCanvasTkAgg(figure3, graph_frame)

    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button1 = Button(master, text="Calculate Moment", command=onclick)
    button1.grid(row=10, columnspan=3, pady=10)

    # PART FOR NORMAL STRESS

    normal_stress = []

    desc_3 = Label(master, text="b_f1", padx=10)
    desc_4 = Label(master, text="t_f1", padx=10)
    desc_5 = Label(master, text="h_w", padx=10)
    desc_6 = Label(master, text="t_w", padx=10)
    desc_7 = Label(master, text="b_f2", padx=10)
    desc_8 = Label(master, text="t_f2", padx=10)
    desc_9 = Label(master, text="N", padx=10)

    desc_3.grid(row=11)
    desc_4.grid(row=12)
    desc_5.grid(row=13)
    desc_6.grid(row=14)
    desc_7.grid(row=15)
    desc_8.grid(row=16)
    desc_9.grid(row=17)

    units_3 = Label(master, text="[cm]", padx=10)
    units_4 = Label(master, text="[cm]", padx=10)
    units_5 = Label(master, text="[cm]", padx=10)
    units_6 = Label(master, text="[cm]", padx=10)
    units_7 = Label(master, text="[cm]", padx=10)
    units_8 = Label(master, text="[cm]", padx=10)
    units_9 = Label(master, text="[kN]", padx=10)

    units_3.grid(row=11, column=3)
    units_4.grid(row=12, column=3)
    units_5.grid(row=13, column=3)
    units_6.grid(row=14, column=3)
    units_7.grid(row=15, column=3)
    units_8.grid(row=16, column=3)
    units_9.grid(row=17, column=3)

    data_3 = Entry(master)
    data_4 = Entry(master)
    data_5 = Entry(master)
    data_6 = Entry(master)
    data_7 = Entry(master)
    data_8 = Entry(master)
    data_9 = Entry(master)

    data_3.grid(row=11, column=2)
    data_4.grid(row=12, column=2)
    data_5.grid(row=13, column=2)
    data_6.grid(row=14, column=2)
    data_7.grid(row=15, column=2)
    data_8.grid(row=16, column=2)
    data_9.grid(row=17, column=2)

    graph_frame2 = Frame(master)
    graph_frame2.grid(row=16, rowspan=8, column=6)

    figure4 = plt.Figure(figsize=(3, 2))

    def onclick2():
        bf1 = float(data_3.get().replace(',', '.'))
        tf1 = float(data_4.get().replace(',', '.'))
        hw = float(data_5.get().replace(',', '.'))
        tw = float(data_6.get().replace(',', '.'))
        bf2 = float(data_7.get().replace(',', '.'))
        tf2 = float(data_8.get().replace(',', '.'))
        normal_force = float(data_9.get().replace(',', '.'))

        i_y = Logic.MomentOfInertia.i_beam(tf1, bf1, tw, hw, tf2, bf2)
        a_cross_section = Logic.MomentOfInertia.i_beam_cross(tf1, bf1, tw, hw, tf2, bf2)

        print(i_y)
        print(a_cross_section)

        h = tf1 + tw + tf2

        if len(normal_stress) != 0:
            normal_stress.clear()

        for i in moment_table:
            normal_s = Logic.StressFunctions.normal_stress(i_y, i * 100, h, normal_force, a_cross_section)
            normal_stress.append(normal_s)
        print(normal_stress)

        max_stress = round(max(normal_stress), 2)
        results_1.config(text=f'Maksymalne naprężenie = {max_stress} [kN/cm^2]')
        results_2.config(text=f'Moment bezwladnosci = {i_y} [cm^4]')
        results_3.config(text=f'Pole przekroju = {a_cross_section} [cm^2]')

        figure4.clf()
        ax4 = figure4.add_subplot(111)
        ax4.scatter(length_table, normal_stress)
        scatter4.draw()

    scatter4 = FigureCanvasTkAgg(figure4, graph_frame2)
    scatter4.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button2 = Button(master, text="Calculate Stress", command=onclick2)
    button2.grid(row=18, columnspan=3)

    results_1 = Label(master, text="Maksymalne naprezenie = 0 [kN/cm^2] ")
    results_2 = Label(master, text="Moment bezwladnosci = 0 [cm^4]")
    results_3 = Label(master, text="Pole przekroju = 0 [cm^2]")
    results_1.grid(row=19, column=2)
    results_2.grid(row=20, column=2)
    results_3.grid(row=21, column=2)
