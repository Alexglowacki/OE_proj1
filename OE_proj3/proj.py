from random import randint
from deap import base
from deap import creator
from deap import tools
import random
import matplotlib.pyplot as plt

import math

def f_rana(individual):
    ind = decodeInd(individual)
    point = ind
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

# dlugosc 40
def invidual(icls):
    genome = list()
    for x in range(0, 40):
        genome.append(randint(0, 1))

    return icls(genome)

def decodeInd(invidual):
    half_ind = int(len(invidual)/2)
    # print(half_ind)
    var1 = int(''.join(map(str, invidual[:half_ind])), 2)
    var2 = int("".join(map(str, invidual[half_ind:])), 2)
    return var1, var2

def fitnessFunction(individual):
    # print(individual)
    # print(len(individual))
    ind = decodeInd(individual)
    result = (ind[0] + 2 * ind[1] - 7) ** 2 + (2 * ind[0] + ind[1] - 5) ** 2
    return result,

def real_individual(icls):
    genome = list()
    genome.append(random.uniform(-10,10))
    genome.append(random.uniform(-10,10))
    return icls(genome)

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

    # toolbox.register("mate", tools.cxUniform)

    toolbox.register("mate", tools.cxTwoPoint)

    # mutation
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.3)

    # toolbox.register("mutate", tools.mutFlipBit, indpb=0.3)

    sizePopulation = 100
    probabilityMutation = 0.2
    probabilityCrossover = 0.2
    numberIteration = 100
    g = 0

    pop = toolbox.population(n=sizePopulation)
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # best = list()
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
    #     best_ind = tools.selBest(pop, 1)[0]
    #     best.append(best_ind.fitness.values[0])
    #     print("Best individual is %s, %s" % (best_ind,
    #                                          best_ind.fitness.values))
    #     #
    #     print("-- End of (successful) evolution --")
    # print(best)
    
    # plt.plot(range(numberIteration), best)
    # plt.grid()
    # plt.title("Best values of each evolution")
    # plt.title
    # plt.show()

    best = list()
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
        best_ind = tools.selBest(pop, 1)[0]
        best.append(best_ind.fitness.values[0])
        print("Best individual is %s, %s" % (best_ind,
                                             best_ind.fitness.values))
        #
        print("-- End of (successful) evolution --")

    plt.plot(range(numberIteration), best)
    plt.grid()
    plt.title("Best values of each evolution")
    plt.title
    plt.show()


        

