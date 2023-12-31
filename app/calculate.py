import tkinter as tk
from tkinter import *
from tkinter.ttk import * 
from tkinter import filedialog
from datetime import datetime
import pandas as pd
import numpy as np
import csv

from app.algorithms.elite import Elite
from app.algorithms.function import f_rana
from app.algorithms.population import Population
from app.algorithms.selection import Selection
from app.algorithms.crossover import Crossover
from app.algorithms.mutation import Mutation
from app.algorithms.inversion import Inversion


# add more parameters to the definitioin
class Calculations:
    algorithm_time = 0
    data2export = []
    result_coords = {"y": [], "x1": [], "x2": []}
    roulette_status_val = "0"
    selection_method = ''

    def run_calculations(range_start: int, 
                         range_end: int,
                         epoch: int,
                         population_size: int,
                         precision: float,
                         elite_strategy: int,
                         variable_number: int, 
                         cross_probability: int,
                         mutation_probability: int,
                         inversion_probability: int, 
                         selection_method: str,
                         percent: float,
                         tournament: int,
                         cross_method: str,
                         mutation_method: str,
                         roulette_status: str,
                         real: str) -> None:
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
        Calculations.roulette_status_val = roulette_status
        print("Running calculations...")
        Calculations.selection_method = selection_method.lower()
        cross_method = cross_method.lower()
        mutation_method = mutation_method.lower()

        # debug - to be deleted 
        print(f"Range start: {range_start}")
        print(f"Range end: {range_end}")
        print(f"Epoch: {epoch}")
        print(f"Population size: {population_size}")
        print(f"Precision: {precision}")
        print(f"Elite strategy: {elite_strategy}")
        print(f"Variable number: {variable_number}")
        print(f"Cross probability: {cross_probability}")
        print(f"Mutation probability: {mutation_probability}")
        print(f"Inversion probability: {inversion_probability}")
        print(f"Picked selection_method: {selection_method}")
        print(f"Percent to next: {percent}")
        print(f"Tournaments: {tournament}")
        print(f"Picked cross_method: {cross_method}")
        print(f"Picked mutation_method: {mutation_method}")
        print(f"Picked is min/max {roulette_status}")
        print(f"Is real: {real}")

        alpha_cross = 0.2
        beta_cross = 0.3

        select_best_param = percent

        start_time = datetime.now()

        # Generate and evaluate population
        pop = Population(population_size, variable_number, range_start, range_end, precision)

        # p - binarna
        p = pop.generate_population()
        p2 = pop.generate_population()

        # evaluated - dziesietna
        evaluated = pop.evaluate_population(p)
        evaluated = np.reshape(evaluated, (population_size, 1))
        evaluated2 = pop.evaluate_population(p2)
        evaluated2 = np.reshape(evaluated2, (population_size, 1))
        evaluated = np.concatenate((evaluated, evaluated2), axis=1)
        # print(evaluated)

        if real == "1":
            for _ in range(epoch):

                selected, not_selected = Calculations.run_elitism(elite_strategy, evaluated)

                evaluated = not_selected

                if Calculations.selection_method == "select best":
                    Calculations.data2export = Calculations.run_select_best(select_best_param, p, evaluated)
                elif Calculations.selection_method == "roulette":
                    if roulette_status == 1:
                        Calculations.data2export = Calculations.run_roulette(True, p, evaluated, percent)
                    else:
                        Calculations.data2export = Calculations.run_roulette(False, p, evaluated, percent)
                elif Calculations.selection_method == "tournament":
                    Calculations.data2export = Calculations.run_tournament(p, evaluated, percent, tournament)

                if cross_method == "one-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 1)
                elif cross_method == "two-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 2)
                elif cross_method == "three-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 3)
                elif cross_method == "uniform":
                    Calculations.data2export = Calculations.run_uniform(cross_probability, evaluated)
                elif cross_method == "arithmetic":
                    Calculations.data2export = Calculations.run_arithmetic(cross_probability, evaluated)
                elif cross_method == 'linear':
                    Calculations.data2export = Calculations.run_linear(cross_probability, evaluated)
                elif cross_method == 'blend_crossover_alpha':
                    Calculations.data2export = Calculations.run_blend_crossover_alpha(cross_probability, evaluated, alpha_cross)
                elif cross_method == 'blend_crossover_alpha_beta':
                    Calculations.data2export = Calculations.run_blend_crossover_alpha_beta(cross_probability, evaluated, alpha_cross, beta_cross)
                elif cross_method == 'average_crossover':
                    Calculations.data2export = Calculations.run_average_crossover(cross_probability, evaluated)

                if mutation_method == "one point":
                    Calculations.data2export = Calculations.run_one_point(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "two point":
                    Calculations.data2export = Calculations.run_two_point(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "edge":
                    Calculations.data2export = Calculations.run_edge(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "uniform":
                    Calculations.data2export = Calculations.run_uniform_mut(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "gaussian":
                    Calculations.data2export = Calculations.run_gaussian(mutation_probability, evaluated, real, range_start, range_end)

                Calculations.data2export = Calculations.run_inversion(inversion_probability, evaluated)
                evaluated = np.concatenate((selected, evaluated))
                Calculations.data2export = evaluated
        else:
            for _ in range(epoch):

                selected, not_selected = Calculations.run_elitism_bin(elite_strategy, p)
                evaluated = not_selected

                if Calculations.selection_method == "select best":
                    Calculations.data2export = Calculations.run_select_best(select_best_param, p, evaluated)
                elif Calculations.selection_method == "roulette":
                    if roulette_status == "1":
                        Calculations.data2export = Calculations.run_roulette(True, p, evaluated, percent)
                    else:
                        Calculations.data2export = Calculations.run_roulette(False, p, evaluated, percent)
                elif Calculations.selection_method == "tournament":
                    Calculations.data2export = Calculations.run_tournament(p, evaluated, percent, tournament)

                if cross_method == "one-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 1)
                elif cross_method == "two-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 2)
                elif cross_method == "three-point":
                    Calculations.data2export = Calculations.run_k_point(cross_probability, evaluated, 3)
                elif cross_method == "uniform":
                    Calculations.data2export = Calculations.run_uniform(cross_probability, evaluated)

                if mutation_method == "one point":
                    Calculations.data2export = Calculations.run_one_point(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "two point":
                    Calculations.data2export = Calculations.run_two_point(mutation_probability, evaluated, real, range_start, range_end)
                elif mutation_method == "edge":
                    Calculations.data2export = Calculations.run_edge(mutation_probability, evaluated, real, range_start, range_end)

                Calculations.data2export = Calculations.run_inversion(inversion_probability, evaluated)
                print(selected.shape)
                print(evaluated.shape)
                print(f"selected: {selected}")
                print(f"evaluated: {evaluated}")
                evaluated = np.concatenate((selected, evaluated))
                Calculations.data2export = evaluated


        end_time = datetime.now()
        
        Calculations.algorithm_time = end_time - start_time
        Calculations.export_to_csv(real, population_size, variable_number, range_start, range_end, precision)

        print(Calculations.algorithm_time)

    def run_select_best(percent_best, p, evaluated):
        pop_best = Selection('best', percent_best).select(p, evaluated)
        return pop_best

    def run_roulette(is_min: bool, p, evaluated, percent):
        # the zero in tournament size here is a magic number
        pop_roulette = Selection('roulette_wheel', percent, 0).select(p, evaluated)
        return pop_roulette

    def run_tournament(p, evaluated, percent, tournament_size):
        pop_tournament = Selection('tournament', percent, tournament_size).select(p, evaluated)
        return pop_tournament

    def run_k_point(prob, pop, k):
        cross_k = Crossover('k-point', prob).select(pop, k, prob, 0.1, 0.1)
        return cross_k

    def run_uniform(prob, pop):
        cross_uniform = Crossover('uniform', prob).select(pop, 1, prob, 0.1, 0.1)
        return cross_uniform
    
    def run_arithmetic(prob, pop):
        cross_arithmetic = Crossover('arithmetic', prob).select(pop, 1, prob, 0.1, 0.1)
        return cross_arithmetic

    def run_linear(prob, pop):
        cross_linear = Crossover('linear', prob).select(pop, 1, prob, 0.1, 0.1)
        return cross_linear

    def run_blend_crossover_alpha(prob, pop, alpha):
        cross_alpha = Crossover('blend_crossover_alpha', prob).select(pop, 1, prob, alpha, 0.1)
        return cross_alpha

    def run_blend_crossover_alpha_beta(prob, pop, alpha, beta):
        cross_alpha_beta = Crossover('blend_crossover_alpha_beta', prob).select(pop, 1, prob, alpha, beta)
        return cross_alpha_beta

    def run_average_crossover(prob, pop):
        cross_average = Crossover('average_crossover', prob).select(pop, 1, prob, 0.1, 0.1)
        return cross_average

    
    def run_one_point(probability, pop, real, range_start, range_end):
        mutation_one_point = Mutation('one point', probability, real, range_start, range_end).select(pop, probability)
        return mutation_one_point
    
    def run_two_point(probability, pop, real, range_start, range_end):
        mutation_two_point = Mutation('two point', probability, real, range_start, range_end).select(pop, probability)
        return mutation_two_point
    
    def run_edge(probability, pop, real, range_start, range_end):
        mutation_edge = Mutation('edge', probability, real, range_start, range_end).select(pop, probability)
        return mutation_edge

    def run_uniform_mut(probability, pop, range_start, range_end):
        mutation_uniform = Mutation('uniform', probability, range_start, range_end).select(pop, probability)
        return mutation_uniform

    def run_gaussian(probability, pop, range_start, range_end):
        mutation_gaussian = Mutation('gaussian', probability, range_start, range_end).select(pop, probability)
        return mutation_gaussian

    def run_inversion(probablity, pop):
        inversion_result = Inversion(probablity).inversion(pop, probablity)
        return inversion_result

    def run_elitism(elite_strategy, pop):
        elite_result = Elite(elite_strategy).elitism(pop, elite_strategy)
        return elite_result

    def run_elitism_bin(elite_strategy, pop):
        elite_result = Elite(elite_strategy).elitism_bin(pop, elite_strategy)
        return elite_result

    def export_to_csv(real, population_size, variable_number, range_start, range_end, precision):
        print("Exporting...")
        file_path = filedialog.askopenfilename(defaultextension="csv")

        #header = ["Val1", "Avg", "Dev"]
        header = ["Val1", "Avg", "Dev", 'x1', 'x2', 'Res']

        # calculations results
        data = np.array(Calculations.data2export)
        if real == "1":
            print("real")

            f = Calculations.find_x1_x2_res(data)
            x1 = f[0]
            x2 = f[1]
            results = f[2]

            data = np.reshape(data, (data.shape[0], 2))
            numbers_series = pd.Series(data[:, 0])

            data = data[:, 0]

            data = np.reshape(data, (data.shape[0], 1))

            data_avg = numbers_series.rolling(2).mean()
            data_avg = data_avg.to_numpy()
            data_avg = np.reshape(data_avg, (data.shape[0], 1))

            data_std = numbers_series.rolling(2).std()
            data_std = data_std.to_numpy()
            data_std = np.reshape(data_std, (data.shape[0], 1))

            #data = np.concatenate((data, data_avg), axis=1)
            #data = np.concatenate((data, data_std), axis=1)

            data = np.concatenate((data, data_avg, data_std, x1, x2, results), axis=1)

            # export to csv
            with open(file_path, 'w') as exportfile:
                csvwriter = csv.writer(exportfile)
                csvwriter.writerow(header)
                csvwriter.writerows(data)

                print("Exported")
        else:
            print("binary")

            pop = Population(population_size, variable_number, range_start, range_end, precision)
            data = pop.decode_population(data)

            f = Calculations.find_x1_x2_res(data)
            x1 = f[0]
            x2 = f[1]
            results = f[2]

            # data
            data = np.reshape(data, (data.shape[0], 2))
            numbers_series = pd.Series(data[:, 0])

            data = data[:, 0]

            data = np.reshape(data, (data.shape[0], 1))

            data_avg = numbers_series.rolling(2).mean()
            data_avg = data_avg.to_numpy()
            data_avg = np.reshape(data_avg, (data.shape[0], 1))

            data_std = numbers_series.rolling(2).std()
            data_std = data_std.to_numpy()
            data_std = np.reshape(data_std, (data.shape[0], 1))

            #data = np.concatenate((data, data_avg), axis=1)
            #data = np.concatenate((data, data_std), axis=1)

            data = np.concatenate((data, data_avg, data_std, x1, x2, results), axis=1)

            # export to csv
            with open(file_path, 'w') as exportfile:
                csvwriter = csv.writer(exportfile)
                csvwriter.writerow(header)
                csvwriter.writerows(data)

                print("Exported")


    def find_x1_x2_res(data):
        # Finding the value of f(x1, x2)
        r = data.reshape(-1)
        results = []
        for i in range(0, len(r), 2):
            if i + 1 < len(r):
                point_x1 = r[i]
                point_x2 = r[i + 1]
                results.append(f_rana([point_x1, point_x2]))
        x1 = data[:, 0]
        x2 = data[:, 1]
        x1 = np.reshape(x1, (x1.shape[0], 1))
        x2 = np.reshape(x2, (x2.shape[0], 1))

        return [x1, x2, results]

