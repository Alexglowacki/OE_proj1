import random
import numpy as np

class Mutation:
    def __init__(self, decision, percentage):
        self.percentage = percentage
        self.decision = decision

    def select(self, evaluated_pop, percentage):
        if self.decision == 'one point':
            return self.mutation_one_point(evaluated_pop, percentage)
        if self.decision == 'two point':
            return self.mutation_two_point(evaluated_pop, percentage)
        if self.decision == 'edge':
            return self.mutation_edge(evaluated_pop, percentage)
        else:
            raise NameError("Not a type of mutation")

    def mutation_one_point(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            random_idx_in_bin = random.randint(0, len(offspring_crossover) - 1)

            offspring_crossover[random_idx_in_bin] = offspring_crossover[random_idx_in_bin] + 1

        return offspring_crossover

    def mutation_edge(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            offspring_crossover[len(offspring_crossover) - 1] = offspring_crossover[len(offspring_crossover) - 1] + 1

        return offspring_crossover

    def mutation_two_point(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            random_idx_in_1st_point = random.randint(0, len(offspring_crossover) - 1)
            random_idx_in_2nd_point = random.randint(0, len(offspring_crossover) - 1)

            offspring_crossover[random_idx_in_1st_point] = offspring_crossover[random_idx_in_1st_point] + 1
            offspring_crossover[random_idx_in_2nd_point] = offspring_crossover[random_idx_in_2nd_point] + 1
        return offspring_crossover
    
    def check_percentage(percentage):
        rng = random.random()
        if 0 < rng < (percentage/100):
            return True
        else:
            return False
