import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from tkinter import filedialog

from datetime import datetime
import csv

# add more parameters to the definitioin
class Calculations():
    algorithm_time = 0
    def run_calculations(selection_method: str) -> None:

        print("Running calculations...")
        selection_method = selection_method.lower()
        print(f"Picked selection_method: {selection_method}")

        # test value 10% best
        select_best_param = 10

        roulette_status = 1

        start_time = datetime.now()

        if selection_method == "select best":
            Calculations.run_select_best(select_best_param)
        elif selection_method == "roulette":
            if roulette_status == 1:
                Calculations.run_roulette(True)
            else:
                Calculations.run_roulette(False)
        elif selection_method == "tournament":
            Calculations.run_tournament()

        end_time = datetime.now()
        
        Calculations.algorithm_time = end_time - start_time
        Calculations.export_to_csv()

        print(Calculations.algorithm_time)

    def run_select_best(percent_best):
        for i in range(10):
            print('Best')

    def run_roulette(is_min: bool):
        for i in range(10):
            print('Roulette')

    def run_tournament():
        for i in range(10):
            print('Tournament')

    def export_to_csv():
        print("Exporting...")
        file_path = filedialog.askopenfilename(defaultextension="csv")
        print(file_path)

        # header - always the same?
        header = ["#", "Val1", "Val2", "Val3", "Val4"]

        # calculations results
        data = [1, 0.1, 0.1, 0.1, 0.1]

        with open(file_path, 'w') as  exportfile:
            csvwriter = csv.writer(exportfile)
            csvwriter.writerow(header)

            for i in range(10):
                csvwriter.writerow(data)

            # for iterable like list use .writerows()

            