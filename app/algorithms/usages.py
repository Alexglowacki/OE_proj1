from app.algorithms.selection import *
from app.algorithms.population import *
from app.algorithms.function import *
from app.algorithms.crossover import *
from app.algorithms.mutation import *
from app.algorithms.inversion import *


if __name__ == '__main__':
    # function
    point = [20, 10]
    print(f"f(20, 10) = {f_rana(point)}")
    # population
    population_size = 10
    num_of_variables = 2
    range_min = -512.0
    range_max = 512.0
    precision = 6
    pop = Population(population_size, num_of_variables, range_min, range_max, precision)
    p = pop.generate_population()
    print(f"Generated population:\n{p}")
    evaluated = pop.evaluate_population(p)
    print(f"\nEvaluated population:\n{evaluated}")
    decoded = pop.decode_population(p)
    print(f"\nDecoded population:\n{decoded}")
    print(f"\n")
    #Selection
    pop_best = Selection('best', 0.2).select(p, evaluated)
    print(f"20% from best selection:\n{pop.decode_population(pop_best[0])}")
    pop_roulette = Selection('roulette_wheel', 0.2).select(p, evaluated)
    print(f"\n\nRoulette selection:\n{pop.decode_population(pop_roulette[0])}")
    pop_tournament = Selection('tournament', 0.2).select(p, evaluated)
    print(f"\n\n20% from tournament selection:\n{pop.decode_population(pop_tournament[0])}")
    #Crossover
    cross_k = Crossover('k-point', 0.2).select(p, 2, 0.2)
    print(f"\n\nK-point crossover:\n{pop.decode_population(cross_k)}")
    cross_one = Crossover('one-point', 0.2).select(p, 2, 0.2)
    print(f"\n\nOne-point crossover:\n{pop.decode_population(cross_one)}")
    cross_two = Crossover('two-point', 0.2).select(p, 2, 0.2)
    print(f"\n\nTwo-point crossover:\n{pop.decode_population(cross_two)}")
    cross_uniform = Crossover('uniform', 0.2).select(p, 2, 0.2)
    print(f"\n\nUniform crossover:\n{pop.decode_population(cross_uniform)}")
    #Mutation
    mut_one = Mutation('one point', 0.2).select(p, 0.2)
    print(f"\n\nOne-point mutation:\n{pop.decode_population(mut_one)}")
    mut_two = Mutation('two point', 0.2).select(p, 0.2)
    print(f"\n\nTwo-point mutation:\n{pop.decode_population(mut_two)}")
    mut_edge = Mutation('edge', 0.2).select(p, 0.2)
    print(f"\n\nEdge mutation:\n{pop.decode_population(mut_edge)}")
    #Inversion
    inv = Inversion(0.2).select(p, 0.2)
    print(f"\n\nInversion:\n{pop.decode_population(inv)}")