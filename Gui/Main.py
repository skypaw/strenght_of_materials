from tkinter import *
from tkinter.ttk import Notebook
import Logic.Buckling
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

window = Tk()
window.title("Wytrzymalosc materialow")
window.geometry("700x500")

tab_parent = Notebook(window)

tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)
tab3 = Frame(tab_parent)
tab4 = Frame(tab_parent)

tab_parent.add(tab1, text="Naprezenia")
tab_parent.add(tab2, text="Momenty bezwladnosci")
tab_parent.add(tab3, text="Zginanie ukosne")
tab_parent.add(tab4, text="Wyboczenie")

tab_parent.pack(expand=1, fill='both')

#
# Tab 5
#

desc_1 = Label(tab4, text="E", padx=10)
desc_2 = Label(tab4, text="A", padx=10)
desc_3 = Label(tab4, text="J", padx=10)
desc_4 = Label(tab4, text="Mu", padx=10)
desc_5 = Label(tab4, text="l", padx=10)
desc_6 = Label(tab4, text="sigma_h", padx=10)
desc_7 = Label(tab4, text="sigma_p", padx=10)

desc_1.grid(row=1)
desc_2.grid(row=2)
desc_3.grid(row=3)
desc_4.grid(row=4)
desc_5.grid(row=5)
desc_6.grid(row=6)
desc_7.grid(row=7)

units_1 = Label(tab4, text="[GPa]", padx=10)
units_2 = Label(tab4, text="[cm^2]", padx=10)
units_3 = Label(tab4, text="[cm^4]", padx=10)
units_4 = Label(tab4, text="[-]", padx=10)
units_5 = Label(tab4, text="[m]", padx=10)
units_6 = Label(tab4, text="[MPa]", padx=10)
units_7 = Label(tab4, text="[MPa]", padx=10)

units_1.grid(row=1, column=3)
units_2.grid(row=2, column=3)
units_3.grid(row=3, column=3)
units_4.grid(row=4, column=3)
units_5.grid(row=5, column=3)
units_6.grid(row=6, column=3)
units_7.grid(row=7, column=3)

data_1 = Entry(tab4)
data_2 = Entry(tab4)
data_3 = Entry(tab4)
data_4 = Entry(tab4)
data_5 = Entry(tab4)
data_6 = Entry(tab4)
data_7 = Entry(tab4)

data_1.grid(row=1, column=2)
data_2.grid(row=2, column=2)
data_3.grid(row=3, column=2)
data_4.grid(row=4, column=2)
data_5.grid(row=5, column=2)
data_6.grid(row=6, column=2)
data_7.grid(row=7, column=2)

lambda_graph = 0
sigma_graph = 0
lambda_rel = 0
sigma_crit = 0

test = Frame(tab4)
test.grid(row=1, rowspan=30, column=6)

figure3 = plt.Figure(figsize=(5, 4))
ax3 = figure3.add_subplot(111)

results_1 = Label(tab4, text="i = ")
results_2 = Label(tab4, text="P_kr = ")
results_1.grid(row=11)
results_2.grid(row=12)


def onclick():
    e = float(data_1.get().replace(',', '.')) * 10 ** 3
    a = float(data_2.get().replace(',', '.')) * 10 ** -4
    j = float(data_3.get().replace(',', '.')) * 10 ** -8
    mu = float(data_4.get().replace(',', '.'))
    l = float(data_5.get().replace(',', '.'))
    sigma_h = float(data_6.get().replace(',', '.'))
    sigma_p = float(data_7.get().replace(',', '.'))

    lambda_graph, sigma_graph, lambda_rel, sigma_crit, p_kr = Logic.Buckling.graph_data(sigma_h, e, sigma_p, a, j, mu,
                                                                                        l)
    results_1.config(text=round(p_kr,3))
    ax3.scatter(lambda_graph, sigma_graph)
    ax3.scatter(lambda_rel, sigma_crit)
    scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)


scatter3 = FigureCanvasTkAgg(figure3, test)
ax3.set_xlabel('Lambda [-]')
ax3.set_ylabel('Sigma [MPa]')

button5 = Button(tab4, text="Calculate", command=onclick)
button5.grid(row=10, columnspan=3, pady=10)

window.mainloop()
