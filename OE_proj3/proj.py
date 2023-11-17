from random import randint
from deap import base
from deap import creator
from deap import tools
import random
import matplotlib.pyplot as plt
import benchmark_functions as bf

import numpy as np

import math

# Idealny wynik dla f_rana: y = -511.73288188661934 dla x1 = -488.632577 i x2 = 512.0
range_max = 512.0
range_min = -512.0

def f_rana(invidual):
    # ind = decodeInd(invidual)
    # point = ind

    point = invidual

    s = 0.0
    array = []
    for i in range(len(point) - 1):
        p1 = point[i] * math.cos(math.sqrt(abs(point[i + 1] + point[i] + 1.0)))
        p2 = math.sin(math.sqrt(abs(point[i + 1] - point[i] + 1.0)))
        p3 = (1.0 + point[i + 1]) * math.sin(math.sqrt(abs(point[i + 1] + point[i] + 1.0)))
        p4 = math.cos(math.sqrt(abs(point[i + 1] - point[i] + 1.0)))
        s += p1 * p2 + p3 * p4
        array.append(s)
    return array

# def invidual(icls):
#     genome = list()
#     for _ in range(0, 40):
#         genome.append(randint(0, 1))

#     return icls(genome)

# def decodeInd(invidual):
#     half_ind = int(len(invidual)/2)
#     # print(half_ind)
#     # dekodowanie z pierwszego projektu
#     var1 = range_min + int(''.join(map(str, invidual[:half_ind])), 2) * (range_max - range_min)/(2**half_ind - 1)
#     var2 = range_min + int("".join(map(str, invidual[half_ind:])), 2) * (range_max - range_min)/(2**half_ind - 1)

#     return var1, var2

def fitnessFunction(individual):
    # print(individual)
    # print(len(individual))
    # ind = decodeInd(individual)
    result = (ind[0] + 2 * ind[1] - 7) ** 2 + (2 * ind[0] + ind[1] - 5) ** 2
    return result,

def invidual(icls):
    genome = list()
    genome.append(random.uniform(-512.0, 512.0))
    genome.append(random.uniform(-512.0, 512.0))
    return icls(genome)

def pick_cross(method: str):
    if method == 'arithmetic':
        cross_arithmetic()
    elif method == 'linear':
        cross_linear()
    elif method == 'alfa':
        cross_alfa()
    elif method == 'alfabeta':
        cross_alfabeta()
    elif method == 'avg':
        cross_avg()

def cross_arithmetic(pop, probability):
    pop_size = pop.shape[0]
    new_pop = []

    for i in range(0, pop_size, 2):
        k = random.random()
        parent1 = pop[i] #1
        parent2 = pop[i+1] #2
        if k < probability:

            size = len(parent1)
            child1 = np.zeros_like(parent1)
            child2 = np.zeros_like(parent2)

            for j in range(size):
                child1[j] =  k * parent1[j] + (1 - k) * parent2[j]
                child2[j] =  (1 - k) * parent1[j] + k * parent2[j]
            
            new_pop.append(child1)
            new_pop.append(child2)
        else:
            new_pop.append(parent1)
            new_pop.append(parent2)

    return np.array(new_pop)

def evaluate(n_dimensions, point):
    func = bf.Rana(n_dimensions=n_dimensions)
    return func(point)

def cross_linear(pop, probability):
    pop_size = pop.shape[0]
    new_pop = []

    for i in range(0, pop_size, 2):
        rand_value = np.random.rand()
        parent1 = pop[i]
        parent2 = pop[i + 1]

        if rand_value > probability:
            new_pop.append(parent1)
            new_pop.append(parent2)
        else:
            parent_size = len(parent1)
            z = np.zeros(parent_size)
            v = np.zeros(parent_size)
            w = np.zeros(parent_size)

            for j in range(parent_size):
                z[j] = (1 / 2 * parent1[j] + 1 / 2 * parent2[j])
                v[j] = (3 / 2 * parent1[j] - 1 / 2 * parent2[j])
                w[j] = (-1 / 2 * parent1[j] + 3 / 2 * parent2[j])

            vectors = [z, v, w]
            evaluate = [evaluate(parent_size, r) for r in vectors]
            sorted_pairs = sorted(zip(vectors, evaluate), key=lambda x: x[1])
            offsprings = [pair[0] for pair in sorted_pairs]

            new_pop.append(offsprings[-2])
            new_pop.append(offsprings[-1])

    return np.array(new_pop)

def cross_alfa(pop, alpha):
    new_pop = []

    for i in range(0, len(pop), 4):
        if i + 3 < len(pop):
            parent1_x1 = pop[i]  # x1
            parent2_y1 = pop[i + 1]  # y1
            parent3_x2 = pop[i + 2]  # x2
            parent4_y2 = pop[i + 3]  # y2

            di_x = abs(parent1_x1 - parent3_x2)
            di_y = abs(parent2_y1 - parent4_y2)

            min_x = np.minimum(parent1_x1, parent3_x2)
            max_x = np.maximum(parent1_x1, parent3_x2)
            min_y = np.minimum(parent2_y1, parent4_y2)
            max_y = np.maximum(parent2_y1, parent4_y2)

            x1_new = random.uniform(min_x - alpha * di_x, max_x + alpha * di_x)
            y1_new = random.uniform(min_y - alpha * di_y, max_y + alpha * di_y)
            x2_new = random.uniform(min_x - alpha * di_x, max_x + alpha * di_x)
            y2_new = random.uniform(min_y - alpha * di_y, max_y + alpha * di_y)

            new_pop.extend([x1_new, y1_new, x2_new, y2_new])

    return np.array(new_pop)

def cross_alfabeta(pop, alpha, beta):
    new_pop = []

    for i in range(0, len(pop), 4):
        if i + 3 < len(pop):
            parent1_x1 = pop[i]  # x1
            parent2_y1 = pop[i + 1]  # y1
            parent3_x2 = pop[i + 2]  # x2
            parent4_y2 = pop[i + 3]  # y2

            di_x = abs(parent1_x1 - parent3_x2)
            di_y = abs(parent2_y1 - parent4_y2)

            min_x = np.minimum(parent1_x1, parent3_x2)
            max_x = np.maximum(parent1_x1, parent3_x2)
            min_y = np.minimum(parent2_y1, parent4_y2)
            max_y = np.maximum(parent2_y1, parent4_y2)

            x1_new = random.uniform(min_x - alpha * di_x, max_x + beta * di_x)
            y1_new = random.uniform(min_y - alpha * di_y, max_y + beta * di_y)
            x2_new = random.uniform(min_x - alpha * di_x, max_x + beta * di_x)
            y2_new = random.uniform(min_y - alpha * di_y, max_y + beta * di_y)

            new_pop.extend([x1_new, y1_new, x2_new, y2_new])

    return np.array(new_pop)

def cross_avg(pop, probability):
    new_pop = []
    for i in range(0, len(pop), 4):
        k = random.random()
        if k < probability and i + 3 < len(pop):
            parent1_x1 = pop[i]  # x1
            parent2_y1 = pop[i + 1]  # y1
            parent3_x2 = pop[i + 2]  # x2
            parent4_y2 = pop[i + 3]  # y2

            x1_new = (parent1_x1 + parent3_x2)/2
            y1_new = (parent2_y1 + parent4_y2)/2

            new_pop.extend([x1_new, y1_new])

    return np.array(new_pop)

if __name__ == "__main__":

    # problem minimalizacji
    creator.create("FitnessMin", base.Fitness, weights=(-1.0, ))

    # problem maksymalizacji
    creator.create("FitnessMax", base.Fitness, weights=(1.0, ))

    # creator.create("Individual", list, fitness=creator.FitnessMax)
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    toolbox.register("individual", invidual, creator.Individual)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # toolbox.register("evaluate", fitnessFunction)
    toolbox.register("evaluate", f_rana)

    # selection
    # toolbox.register("select", tools.selTournament, tournsize=3)

    # toolbox.register("select", tools.selRandom)

    toolbox.register("select", tools.selBest)

    # toolbox.register("select", tools.selWorst)

    # toolbox.register("select", tools.selRoulette)

    # crossover
    # toolbox.register("mate", tools.cxOnePoint)

    # toolbox.register("mate", tools.cxUniform, indpb=0.3)

    toolbox.register("mate", tools.cxTwoPoint)

    # crossover own implementation

    # pick_cross('arithmetic')

    # pick_cross('linear')

    # pick_cross('alfa')

    # pick_cross('alfabeta')

    # pick_cross('avg')


    # mutation
    # toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3)

    # toolbox.register("mutate", tools.mutFlipBit, indpb=0.001)

    # TYLKO DLA RECZYWISTYCH
    # toolbox.register("mutate", tools.mutGaussian, mu=3, sigma=6, indpb=0.001)

    toolbox.register("mutate", tools.mutUniformInt, low=-512.0, up=512.0, indpb=0.001) 

    sizePopulation = 1000
    probabilityMutation = 0.3
    probabilityCrossover = 0.6
    numberIteration = 500
    g = 0

    pop = toolbox.population(n=sizePopulation)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # min_vals = list()
    # max_vals = list()
    # avg_vals = list()
    # std_vals = list()
    # best_vals = list()

    # while g < numberIteration:
    #     g = g + 1
    #     print("-- Generation %i --" % g)
    #     # Select the next generation individuals
    #     offspring = toolbox.select(pop, len(pop))
    #     # Clone the selected individuals
    #     offspring = list(map(toolbox.clone, offspring))
    #     # Apply crossover and mutation on the offspring
    #     for child1, child2 in zip(offspring[::2], offspring[1::2]):
    #         # cross two individuals with probability CXPB
    #         if random.random() < probabilityCrossover:
    #             toolbox.mate(child1, child2)
    #         # fitness values of the children
    #         # must be recalculated later
    #         del child1.fitness.values
    #         del child2.fitness.values
    #     for mutant in offspring:
    #         # mutate an individual with probability MUTPB
    #         if random.random() < probabilityMutation:
    #             toolbox.mutate(mutant)
    #             del mutant.fitness.values
    #     # Evaluate the individuals with an invalid fitness
    #     invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    #     fitnesses = map(toolbox.evaluate, invalid_ind)
    #     for ind, fit in zip(invalid_ind, fitnesses):
    #         ind.fitness.values = fit
    #     print(" Evaluated %i individuals" % len(invalid_ind))
    #     pop[:] = offspring
    #     # Gather all the fitnesses in one list and print the stats
    #     fits = [ind.fitness.values[0] for ind in pop]
    #     length = len(pop)
    #     mean = sum(fits) / length
    #     sum2 = sum(x * x for x in fits)
    #     std = abs(sum2 / length - mean ** 2) ** 0.5
    #     print(" Min %s" % min(fits))
    #     print(" Max %s" % max(fits))
    #     print(" Avg %s" % mean)
    #     print(" Std %s" % std)
    #     min_vals.append(min(fits))
    #     max_vals.append(max(fits))
    #     avg_vals.append(mean)
    #     std_vals.append(std)
    #     best_ind = tools.selBest(pop, 1)[0]
    #     best_vals.append(best_ind.fitness.values[0])
    #     print("Best individual is %s, %s" % (best_ind,
    #                                          best_ind.fitness.values))
    #     #
    #     print("-- End of (successful) evolution --")
    
    # plt.subplot(2, 3, 1)
    # plt.grid()
    # plt.title("Best values of each evolution")
    # plt.plot(range(numberIteration), best_vals)

    # plt.subplot(2, 3, 2)
    # plt.grid()
    # plt.title("Min values of each evolution")
    # plt.plot(range(numberIteration), min_vals)

    # plt.subplot(2, 3, 3)
    # plt.grid()
    # plt.title("Max values of each evolution")
    # plt.plot(range(numberIteration), max_vals)

    # plt.subplot(2, 3, 4)
    # plt.grid()
    # plt.title("Average values of each evolution")
    # plt.plot(range(numberIteration), avg_vals)

    # plt.subplot(2, 3, 5)
    # plt.grid()
    # plt.title("Std. deviation values of each evolution")
    # plt.plot(range(numberIteration), std_vals)

    # plt.rcParams["figure.figsize"] = (40, 10)
    # plt.show()


    # ========================================
    # Elityzm
    # ========================================

    min_vals = list()
    max_vals = list()
    avg_vals = list()
    std_vals = list()
    best_vals = list()

    g = 0
    numberElitism = 1
    while g < numberIteration:
        g = g + 1
        print("-- Generation %i --" % g)
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        listElitism = []
        for x in range(0, numberElitism):
            listElitism.append(tools.selBest(pop, 1)[0])
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            # cross two individuals with probability CXPB
            if random.random() < probabilityCrossover:
                toolbox.mate(child1, child2)
            # fitness values of the children
            # must be recalculated later
            del child1.fitness.values
            del child2.fitness.values
        for mutant in offspring:
            # mutate an individual with probability MUTPB
            if random.random() < probabilityMutation:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print(" Evaluated %i individuals" % len(invalid_ind))
        pop[:] = offspring + listElitism
        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5
        print(" Min %s" % min(fits))
        print(" Max %s" % max(fits))
        print(" Avg %s" % mean)
        print(" Std %s" % std)

        min_vals.append(min(fits))
        max_vals.append(max(fits))
        avg_vals.append(mean)
        std_vals.append(std)

        best_ind = tools.selBest(pop, 1)[0]
        best_vals.append(best_ind.fitness.values[0])
        print("Best individual is %s, %s" % (best_ind,
                                             best_ind.fitness.values))
        #
        print("-- End of (successful) evolution --")

    plt.subplot(2, 3, 1)
    plt.grid()
    plt.title("Best values of each evolution")
    plt.plot(range(numberIteration), best_vals)

    plt.subplot(2, 3, 2)
    plt.grid()
    plt.title("Min values of each evolution")
    plt.plot(range(numberIteration), min_vals)

    plt.subplot(2, 3, 3)
    plt.grid()
    plt.title("Max values of each evolution")
    plt.plot(range(numberIteration), max_vals)

    plt.subplot(2, 3, 4)
    plt.grid()
    plt.title("Average values of each evolution")
    plt.plot(range(numberIteration), avg_vals)

    plt.subplot(2, 3, 5)
    plt.grid()
    plt.title("Std. deviation values of each evolution")
    plt.plot(range(numberIteration), std_vals)

    plt.rcParams["figure.figsize"] = (40, 10)
    plt.show()

    # W INTERPRETACJI RZECZYWISTEJ
    # najlepsze wyniki wychodza dla:
    # elityzm = 1
    # toolbox.register("mutate", tools.mutUniformInt, low=-512.0, up=512.0, indpb=0.001) 
    # toolbox.register("select", tools.selBest)
    # toolbox.register("mate", tools.cxOnePoint)

    # sizePopulation = 100
    # probabilityMutation = 0.6
    # probabilityCrossover = 0.8
    # numberIteration = 500


