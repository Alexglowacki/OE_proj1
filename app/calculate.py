import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from tkinter import filedialog
from datetime import datetime
import csv
from app.algorithms.population import Population
from app.algorithms.selection import Selection
from app.algorithms.crossover import Crossover
from app.algorithms.mutation import Mutation
from app.algorithms.inversion import Inversion


# add more parameters to the definitioin
class Calculations:
    algorithm_time = 0
    data2export = []
    dummy = 0 # placeholder for uniform crossover
    def run_calculations(range_start: int, 
                         range_end: int,
                         epoch: int,
                         population_size: int,
                         precision: float,
                         elite_strategy: float,
                         cross_probability: float,
                         mutation_probability: float,
                         inversion_probability: float, 
                         selection_method: str,
                         percent: float,
                         tournament: float,
                         cross_method: str,
                         mutation_method: str,
                         roulette_status: bool) -> None:
        """_summary_

        Args:
            range_start (float): _description_
            range_end (float): _description_
            epoch (int): _description_
            population_size (int): _description_
            precision (int): _description_
            elite_strategy (float): _description_
            cross_probability (float): _description_
            mutation_probability (float): _description_
            inversion_probability (float): _description_
            selection_method (str): _description_
            percent (float): _description_
            tournament (float): _description_
            cross_method (str): _description_
            mutation_method (str): _description_
            roulette_status (bool, optional): _description_. Defaults to False.
        """

        print("Running calculations...")
        selection_method = selection_method.lower()
        cross_method = cross_method.lower()
        mutation_method = mutation_method.lower()

        # debug - to be deleted 
        print(f"Range start: {range_start}")
        print(f"Range end: {range_end}")
        print(f"Epoch: {epoch}")
        print(f"Population size: {population_size}")
        print(f"Precision: {precision}")
        print(f"Elite strategy: {elite_strategy}")
        print(f"Cross probability: {cross_probability}")
        print(f"Mutation probability: {mutation_probability}")
        print(f"Inversion probability: {inversion_probability}")
        print(f"Picked selection_method: {selection_method}")
        print(f"Percent to next: {percent}")
        print(f"Tournaments: {tournament}")
        print(f"Picked cross_method: {cross_method}")
        print(f"Picked mutation_method: {mutation_method}")
        print(f"Picked is min/max {roulette_status}")

        select_best_param = percent

        start_time = datetime.now()

        # Generate and evaluate population
        pop = Population(population_size, 2, range_start, range_end, precision)
        p = pop.generate_population()
        evaluated = pop.evaluate_population(p)

        if selection_method == "select best":
            Calculations.data2export = Calculations.run_select_best(select_best_param, p, evaluated)
        elif selection_method == "roulette":
            if roulette_status:
                Calculations.data2export = Calculations.run_roulette(True, p, evaluated, percent)
            else:
                Calculations.data2export = Calculations.run_roulette(False, p, evaluated, percent)
        elif selection_method == "tournament":
            Calculations.data2export = Calculations.run_tournament(p, evaluated)

        if cross_method == "one-point":
            Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 1)
        elif cross_method == "two-point":
            Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 2)
        elif cross_method == "k-point":
            Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, k)
        elif cross_method == "uniform":
            Calculations.data2export = Calculations.run_uniform(cross_probability, evaluated)

        if mutation_method == "one point":
            Calculations.data2export = Calculations.run_one_point(mutation_probability, evaluated)
        elif mutation_method == "two point":
            Calculations.data2export = Calculations.run_two_point(mutation_probability, evaluated)
        elif mutation_method == "edge":
            Calculations.data2export = Calculations.run_edge(mutation_probability, evaluated)

        Calculations.data2export = Calculations.run_inversion(inversion_probability, evaluated)

        end_time = datetime.now()
        
        Calculations.algorithm_time = end_time - start_time
        Calculations.export_to_csv()

        print(Calculations.algorithm_time)

    def run_select_best(percent_best, p, evaluated):
        pop_best = Selection('best', percent_best).select(p, evaluated)
        return pop_best

    def run_roulette(is_min: bool, p, evaluated, percent):
        pop_roulette = Selection('roulette_wheel', percent).select(p, evaluated)
        return pop_roulette

    def run_tournament(p, evaluated, percent):
        pop_tournament = Selection('tournament', percent).select(p, evaluated)
        return pop_tournament

    def run_k_point(prob, pop, k):
        cross_k = Crossover('k-point', prob).select(pop, k, prob)
        return cross_k

    def run_uniform(prob, pop):
        cross_uniform = Crossover('uniform', prob).select(pop, prob)
        return cross_uniform
    
    def run_one_point(probability, pop):
        mutation_one_point = Mutation('one point').select(pop, probability)
        return mutation_one_point
    
    def run_two_point(probability, pop):
        mutation_two_point = Mutation('two point').select(pop, probability)
        return mutation_two_point
    
    def run_edge(probability, pop):
        mutation_edge = Mutation('edge').select(pop, probability)
        return mutation_edge
    
    def run_inversion(probablity, pop):
        inversion_result = Inversion.inversion(pop, probablity)
        return inversion_result

    def export_to_csv():
        print("Exporting...")
        file_path = filedialog.askopenfilename(defaultextension="csv")
        print(file_path)

        header = ["Val1", "Avg", "Dev"]

        # calculations results
        data = Calculations.data2export

        with open(file_path, 'w') as  exportfile:
            csvwriter = csv.writer(exportfile)
            csvwriter.writerow(header)

            for row in data:
                csvwriter.writerow(row)
                # for iterable like list use .writerows()

            