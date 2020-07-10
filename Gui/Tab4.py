from tkinter import *
import Logic.Buckling
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)


def tab4(master):
    desc_1 = Label(master, text="E", padx=10)
    desc_2 = Label(master, text="sigma_h", padx=10)
    desc_3 = Label(master, text="sigma_p", padx=10)
    desc_4 = Label(master, text="Pole przekroju", padx=10)
    desc_5 = Label(master, text="Moment bezwladnosci", padx=10)
    desc_6 = Label(master, text="Wspolczynnik wyboczenia", padx=10)
    desc_7 = Label(master, text="Dlugosc preta", padx=10)

    desc_1.grid(row=1)
    desc_2.grid(row=2)
    desc_3.grid(row=3)
    desc_4.grid(row=4)
    desc_5.grid(row=5)
    desc_6.grid(row=6)
    desc_7.grid(row=7)

    units_1 = Label(master, text="[GPa]", padx=10)
    units_2 = Label(master, text="[MPa]", padx=10)
    units_3 = Label(master, text="[MPa]", padx=10)
    units_4 = Label(master, text="[cm^2]", padx=10)
    units_5 = Label(master, text="[cm^4]", padx=10)
    units_6 = Label(master, text="[-]", padx=10)
    units_7 = Label(master, text="[m]", padx=10)

    units_1.grid(row=1, column=3)
    units_2.grid(row=2, column=3)
    units_3.grid(row=3, column=3)
    units_4.grid(row=4, column=3)
    units_5.grid(row=5, column=3)
    units_6.grid(row=6, column=3)
    units_7.grid(row=7, column=3)

    data_1 = Entry(master)
    data_2 = Entry(master)
    data_3 = Entry(master)
    data_4 = Entry(master)
    data_5 = Entry(master)
    data_6 = Entry(master)
    data_7 = Entry(master)

    data_1.grid(row=1, column=2)
    data_2.grid(row=2, column=2)
    data_3.grid(row=3, column=2)
    data_4.grid(row=4, column=2)
    data_5.grid(row=5, column=2)
    data_6.grid(row=6, column=2)
    data_7.grid(row=7, column=2)

    graph = Frame(master)
    graph.grid(row=1, rowspan=30, column=6)

    figure3 = plt.Figure(figsize=(4, 4))

    def onclick():
        e = float(data_1.get().replace(',', '.')) * 10 ** 3  # Conversion from MPa to GPa
        sigma_h = float(data_2.get().replace(',', '.'))
        sigma_p = float(data_3.get().replace(',', '.'))
        a = float(data_4.get().replace(',', '.')) * 10 ** -4  # Conversion from m^2, to cm^2
        j = float(data_5.get().replace(',', '.')) * 10 ** -8  # Conversion from m^4, to cm^4
        coefficient = float(data_6.get().replace(',', '.'))
        l = float(data_7.get().replace(',', '.'))

        lambda_table, sigma_table, lambda_rel, sigma_crit_rel, p_kr = Logic.Buckling.graph_data(sigma_h, e, sigma_p, a,
                                                                                                j, coefficient, l)

        figure3.clf()
        ax3 = figure3.add_subplot(111)
        ax3.scatter(lambda_table, sigma_table)
        ax3.scatter(lambda_rel, sigma_crit_rel)
        scatter3.draw()

        results_2.config(text=f'Lambda = {round(lambda_rel, 2)} [-]')
        results_3.config(text=f'Sigma krytyczna = {round(sigma_crit_rel, 4)} [MPa]')
        results_4.config(text=f'Sila krytyczna = {round(p_kr, 2)} [kN]')

    scatter3 = FigureCanvasTkAgg(figure3, graph)
    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button5 = Button(master, text="Calculate", command=onclick)
    button5.grid(row=10, columnspan=3, pady=10)

    results_1 = Label(master, text="Wyniki:")
    results_2 = Label(master, text="Lambda = 0")
    results_3 = Label(master, text="Sigma krytyczna = 0")
    results_4 = Label(master, text="Maksymalna siła = 0")

    results_1.grid(row=11, columnspan=3, pady=10)
    results_2.grid(row=12, columnspan=3)
    results_3.grid(row=13, columnspan=3)
    results_4.grid(row=14, columnspan=3)
