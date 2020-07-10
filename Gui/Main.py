from tkinter import *
from tkinter.ttk import Notebook
import Gui.Tab1
import Gui.Tab2
import Gui.Tab3
import Gui.Tab4

import Logic.Buckling
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


class Main:
    def __init__(self, master):
        tab_parent = Notebook(master)

        tab1 = Frame(tab_parent)
        tab2 = Frame(tab_parent)
        tab3 = Frame(tab_parent)
        tab4 = Frame(tab_parent)

        tab_parent.add(tab1, text="Naprezenia")
        tab_parent.add(tab2, text="Skrecanie")
        tab_parent.add(tab3, text="Zginanie ukosne")
        tab_parent.add(tab4, text="Wyboczenie")

        tab_parent.pack(expand=1, fill='both')

        Gui.Tab1.tab1(tab1)
        Gui.Tab2.tab2(tab2)
        Gui.Tab3.tab3(tab3)
        Gui.Tab4.tab4(tab4)


window = Tk()
window.title("Wytrzymalosc materialow")
Main(window)
window.geometry("700x500")
window.mainloop()
