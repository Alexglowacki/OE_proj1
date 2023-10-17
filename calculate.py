import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from tkinter import filedialog

from datetime import datetime
import csv

# add more parameters to the definitioin
def run_calculations(method: str) -> None:
    """_summary_

    Args:
        method (str): _description_
    """

    print("Running calculations...")
    method = method.lower()
    print(f"Picked method: {method}")

    # test value 10% best
    select_best_param = 10

    start_time = datetime.now()

    if method == "select best":
        run_select_best(select_best_param)
    elif method == "roulette":
        run_roulette()
    elif method == "tournament":
        run_tournament()

    end_time = datetime.now()
    algorithm_time = end_time - start_time
    export_to_csv()

    print(algorithm_time)

def run_select_best(percent_best):
    for i in range(10):
        print('Best')

def run_roulette():
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

        