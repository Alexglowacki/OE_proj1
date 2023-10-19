import numpy as np
import function as f


class Population:
    def __init__(self, population_size, num_of_variables, range_min, range_max, precision):
        self.population_size = population_size
        self.num_of_variables = num_of_variables
        self.range_min = range_min
        self.range_max = range_max
        self.precision = precision
        self.num_of_bits = self.binary_length()

    def np_to_dec(self, n):  #returns decimal represntation for numpy array
        n = ''.join(str(int(i)) for i in n)
        return int(n, 2)

    def binary_length(self):
        a = self.range_min
        b = self.range_max
        d = self.precision
        return int(np.ceil(np.log2(float((b - a) * (10 ** d))) + np.log2(1)))

    def generate_population(self):
        return np.random.randint(2, size=(self.population_size, self.num_of_variables, self.num_of_bits))

    def decode_population(self, population):
        a = self.range_min
        b = self.range_max
        m = self.num_of_bits
        decoded = []
        for i in range(0, len(population)):
            x1_bin_part = self.np_to_dec(population[i][0])
            x1 = a + x1_bin_part * (b - a) / (2 ** m - 1)
            x2_bin_part = self.np_to_dec(population[i][1])
            x2 = a + x2_bin_part * (b - a) / (2 ** m - 1)
            decoded.append([x1, x2])
        return np.array(decoded)

    def evaluate_population(self, population):
        population = self.decode_population(population)
        return np.array([f.evaluate(r) for r in population])



if __name__ == '__main__':
    population_size = 5
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
