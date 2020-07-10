from tkinter import *
import Logic.TwistingMoment
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)


def tab2(master):
    desc_1 = Label(master, text="m_s", padx=10)
    desc_2 = Label(master, text="j_y", padx=10)
    desc_3 = Label(master, text="r", padx=10)

    desc_1.grid(row=1)
    desc_2.grid(row=2)
    desc_3.grid(row=3)

    units_1 = Label(master, text="[kNcm]", padx=10)
    units_2 = Label(master, text="[cm^4]", padx=10)
    units_3 = Label(master, text="[cm]", padx=10)

    units_1.grid(row=1, column=3)
    units_2.grid(row=2, column=3)
    units_3.grid(row=3, column=3)

    data_1 = Entry(master)
    data_2 = Entry(master)
    data_3 = Entry(master)

    data_1.grid(row=1, column=2)
    data_2.grid(row=2, column=2)
    data_3.grid(row=3, column=2)

    graph = Frame(master)
    graph.grid(row=1, rowspan=30, column=6)

    figure3 = plt.Figure(figsize=(4, 4))

    def onclick():
        m_s_func = float(data_1.get().replace(',', '.'))
        j_y_circular = j_z_circular = float(data_2.get().replace(',', '.'))
        rho_func = float(data_3.get().replace(',', '.'))

        tau_x, rho_table = Logic.TwistingMoment.circular_stress(j_y_circular, j_z_circular, m_s_func, rho_func)

        figure3.clf()
        ax3 = figure3.add_subplot(111)
        ax3.scatter(tau_x, rho_table)
        scatter3.draw()

        results_2.config(text=f'tau = {round(max(tau_x), 4)} [-]')

    scatter3 = FigureCanvasTkAgg(figure3, graph)
    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button5 = Button(master, text="Calculate", command=onclick)
    button5.grid(row=10, columnspan=3, pady=10)

    results_1 = Label(master, text="Wyniki:")
    results_2 = Label(master, text="Lambda = 0")

    results_1.grid(row=11, columnspan=3, pady=10)
    results_2.grid(row=12, columnspan=3)
