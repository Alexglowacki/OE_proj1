
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

import tkinter as Tk
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import csv
from tkinter import filedialog

import pandas as pd
# for black background
# plt.style.use('dark_background')
class Graphing:
    def graph_results() -> None:
        """_summary_

        Args:
            method (str): _description_
        """

        file_path = filedialog.askopenfilename(defaultextension="csv")
        print(file_path)

        x_vals = []

        data = pd.read_csv(file_path, delimiter=",")
        x_vals = np.linspace(start=0, stop=len(data['Val1']), num=len(data['Val1']))

        #y1_vals = data['Val1']
        y1_vals = data['Res']
        y2_vals = data['Avg']
        y3_vals = data['Dev']

        # creating 3 subplots - wartosc funkcji od kolejnej iteracji,
        # sredniej wartosci funkcji i odchylenia
        f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey = True)

        ax1.set_title('Function value')
        ax1.plot(x_vals, y1_vals)

        ax2.set_title('Avg. value')
        ax2.plot(x_vals, y2_vals)

        ax3.set_title('Std. deviation')
        ax3.plot(x_vals, y3_vals)

        ax2.set_xlabel("Iterations")

        ax1.set_ylabel("Value of a function")
        ax2.set_ylabel("Rolling average of the function")
        ax3.set_ylabel("Rolling standard deviation of the function")

        ax1.grid(color='gray', linestyle='--', linewidth=0.5)
        ax2.grid(color='gray', linestyle='--', linewidth=0.5)
        ax3.grid(color='gray', linestyle='--', linewidth=0.5)

        plt.show()


    def get_data() -> None:
        file_path = filedialog.askopenfilename(defaultextension="csv")
        print(file_path)

        x_vals = []

        data = pd.read_csv(file_path, delimiter=",", header=None, names=['Val1', 'Avg', 'Dev'])
        x_vals = np.linspace(0, len(data['Val1']))

        y1_vals = data['Val1']
        y2_vals = data['Avg']
        y3_vals = data['Dev']

    def Function_value_plot() -> None:

        ax.set_title('Function value')
        ax.plot(x_vals, y1_vals)
        ax.set_xlabel("Iterations")

        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.show()

    def Average_value_plot() -> None:

        ax.set_title('Avg. value')
        ax.plot(x_vals, y2_vals)
        ax.set_xlabel("Iterations")

        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.show()

    def Standard_deviation_plot() -> None:

        ax.set_title('Std. deviation')
        ax.plot(x_vals, y3_vals)
        ax.set_xlabel("Iterations")

        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.show()