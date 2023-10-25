import random
import numpy as np

class Inversion:
    def __init__(self, percentage):
        self.percentage = percentage

    def inversion(offspring_crossover, percentage):

        if Inversion.check_percentage(percentage):
            inversion_offspring = []

            for gene in offspring_crossover:
                random_idx_in_bin_start = random.randint(0, len(gene) - 1)
                random_idx_in_bin_end = random.randint(0, len(gene) - 1)

                gene = list(gene)

                if random_idx_in_bin_start > random_idx_in_bin_end:
                    temp = random_idx_in_bin_end
                    random_idx_in_bin_end = random_idx_in_bin_start
                    random_idx_in_bin_start = temp

                strip = gene[random_idx_in_bin_start:random_idx_in_bin_end]

                reversed_strip = strip[::-1]

                gene[random_idx_in_bin_start:random_idx_in_bin_end] = reversed_strip
                gene = ''.join(gene)
                inversion_offspring.append(gene)

            offspring_crossover = np.array(inversion_offspring)

        return offspring_crossover
    
    def check_percentage(percentage):
        rng = random.random()
        if 0 < rng < (percentage/100):
            return True
        else:
            return False

if __name__ == "__main__":

    bin_repr_inv = ["10110011111111111111", "01010100100000000000"]
    offspring_crossover = np.array(bin_repr_inv)

    inversion_result = Inversion.inversion(offspring_crossover, 20)
    print(f"inversion_result = {inversion_result}")