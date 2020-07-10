from tkinter import *
import Logic.BendingAtAngle
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)


def tab3(master):
    desc_1 = Label(master, text="m_max", padx=10)
    desc_2 = Label(master, text="kat alpha", padx=10)
    desc_3 = Label(master, text="j_y", padx=10)
    desc_4 = Label(master, text="j_z", padx=10)
    desc_5 = Label(master, text="y", padx=10)

    desc_1.grid(row=1)
    desc_2.grid(row=2)
    desc_3.grid(row=3)
    desc_4.grid(row=4)
    desc_5.grid(row=5)

    units_1 = Label(master, text="[kNcm]", padx=10)
    units_2 = Label(master, text="[*]", padx=10)
    units_3 = Label(master, text="[cm^4]", padx=10)
    units_4 = Label(master, text="[cm^4]", padx=10)
    units_5 = Label(master, text="[cm]", padx=10)

    units_1.grid(row=1, column=3)
    units_2.grid(row=2, column=3)
    units_3.grid(row=3, column=3)
    units_4.grid(row=4, column=3)
    units_5.grid(row=5, column=3)

    data_1 = Entry(master)
    data_2 = Entry(master)
    data_3 = Entry(master)
    data_4 = Entry(master)
    data_5 = Entry(master)

    data_1.grid(row=1, column=2)
    data_2.grid(row=2, column=2)
    data_3.grid(row=3, column=2)
    data_4.grid(row=4, column=2)
    data_5.grid(row=5, column=2)

    graph = Frame(master)
    graph.grid(row=1, rowspan=30, column=6)

    def onclick():
        m_max = float(data_1.get().replace(',', '.'))
        alpha = float(data_2.get().replace(',', '.'))
        j_y = float(data_3.get().replace(',', '.'))
        j_z = float(data_4.get().replace(',', '.'))
        y = float(data_5.get().replace(',', '.'))

        m_y, m_z = Logic.BendingAtAngle.bending_moments(alpha, m_max)
        z_neutral = Logic.BendingAtAngle.neutral_axis(m_y, m_z, j_y, j_z, y)

        results_2.config(text=f'm_y = {round(m_y, 4)} [-]')
        results_3.config(text=f'm_z = {round(m_z, 4)} [-]')
        results_4.config(text=f'z_neutral = {round(z_neutral, 4)} [cm]')

    # scatter3 = FigureCanvasTkAgg(figure3, graph)
    # scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button5 = Button(master, text="Calculate", command=onclick)
    button5.grid(row=10, columnspan=3, pady=10)

    results_1 = Label(master, text="Wyniki:")
    results_2 = Label(master, text="m_y = 0 [-]")
    results_3 = Label(master, text="m_z = 0 [-]")
    results_4 = Label(master, text="z_neutral = 0 [cm]")

    results_1.grid(row=11, columnspan=3, pady=10)
    results_2.grid(row=12, columnspan=3)
    results_3.grid(row=13, columnspan=3)
    results_4.grid(row=14, columnspan=3)
