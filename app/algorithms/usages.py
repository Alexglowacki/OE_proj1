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
    # Crossover
    print(f"\nReshape decoded population:\n{decoded.reshape(-1)}")
    print(f"\nSize of decoded population:\n{decoded.reshape(-1).size}")
    cross_alpha = Crossover('blend_crossover_alpha', 0.5).select(decoded.reshape(-1),
                                                                 0, 0.3, 0.25, 0.11)
    print(f"\nBlend crossover alpha:\n{cross_alpha}")
    cross_alpha_beta = Crossover('blend_crossover_alpha_beta', 0.5).select(decoded.reshape(-1),
                                                                 0, 0.3, 0.25, 0.11)
    print(f"\nBlend crossover alpha beta:\n{cross_alpha_beta}")
    cross_average = Crossover('average_crossover', 0.5).select(decoded.reshape(-1),
                                                                           0, 0.3, 0.25, 0.11)
    print(f"\nAverage crossover:\n{cross_average}")
    cross_flat = Crossover('flat_crossover', 0.5).select(decoded.reshape(-1),
                                                               0, 0.3, 0.25, 0.11)
    print(f"\nFlat crossover:\n{cross_flat}")
    print()
    #Selection
    pop_best = Selection('best', 0.2, 0).select(p, evaluated)
    print(f"20% from best selection:\n{pop.decode_population(pop_best[0])}")
    pop_roulette = Selection('roulette_wheel', 0.2, 0).select(p, evaluated)
    print(f"\n\nRoulette selection:\n{pop.decode_population(pop_roulette[0])}")
    pop_tournament = Selection('tournament', 0.2, 8).select(p, evaluated)
    print(f"\n\n20% from tournament selection:\n{pop.decode_population(pop_tournament[0])}")
    #Crossover
    cross_k = Crossover('k-point', 0.2).select(p, 2, 0.2, 0.25, 0.11)
    print(f"\n\nK-point crossover:\n{pop.decode_population(cross_k)}")
    cross_one = Crossover('one-point', 0.2).select(p, 2, 0.2, 0.25, 0.11)
    print(f"\n\nOne-point crossover:\n{pop.decode_population(cross_one)}")
    cross_two = Crossover('two-point', 0.2).select(p, 2, 0.2, 0.25, 0.11)
    print(f"\n\nTwo-point crossover:\n{pop.decode_population(cross_two)}")
    cross_uniform = Crossover('uniform', 0.2).select(p, 2, 0.2, 0.25, 0.11)
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