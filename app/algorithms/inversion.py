import random
import numpy as np

class Inversion:
    def __init__(self, percentage):
        self.percentage = percentage

    def inversion(self, offspring_crossover, percentage):

        if Inversion.check_percentage(percentage):
            random_idx_in_bin_start = random.randint(0, len(offspring_crossover) - 1)
            random_idx_in_bin_end = random.randint(0, len(offspring_crossover) - 1)

            if random_idx_in_bin_start > random_idx_in_bin_end:
                temp = random_idx_in_bin_end
                random_idx_in_bin_end = random_idx_in_bin_start
                random_idx_in_bin_start = temp

            strip = offspring_crossover[random_idx_in_bin_start:random_idx_in_bin_end]

            reversed_strip = strip[::-1]

            offspring_crossover[random_idx_in_bin_start:random_idx_in_bin_end] = reversed_strip

        return offspring_crossover
    
    def check_percentage(percentage):
        rng = random.random()
        if 0 < rng < (percentage/100):
            return True
        else:
            return False
