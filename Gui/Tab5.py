from tkinter import *
import Logic.Buckling
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)


def test(master):
    desc_1 = Label(master, text="E", padx=10)

    desc_1.grid(row=1)

    units_1 = Label(master, text="[GPa]", padx=10)

    units_1.grid(row=1, column=3)

    data_1 = Entry(master)

    data_1.grid(row=1, column=2)

    test = Frame(master)
    test.grid(row=1, rowspan=30, column=6)

    figure3 = plt.Figure(figsize=(5, 4))
    ax3 = figure3.add_subplot(111)

    def onclick():
        e = float(data_1.get().replace(',', '.')) * 10 ** 3

        lambda_graph = [2, 3, 1, 3, 1, 3, 2]
        sigma_graph = [2, 3, 1, 3, 1, 3, 2]

        ax3.scatter(lambda_graph, sigma_graph)

        scatter3.draw()

    scatter3 = FigureCanvasTkAgg(figure3, test)

    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)

    button5 = Button(master, text="Calculate", command=onclick)
    button5.grid(row=10, columnspan=3, pady=10)
