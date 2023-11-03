import random
import numpy as np
import benchmark_functions as bf

from app.algorithms.function import f_rana


class Crossover:
    def __init__(self, decision, probability):
        self.probability = probability
        self.decision = decision

    def select(self, evaluated_pop, k, probability, alpha, beta):
        if self.decision == "one-point":
            return self.k_point(evaluated_pop, 1, probability)
        elif self.decision == "two-point":
            return self.k_point(evaluated_pop, 2, probability)
        elif self.decision == "three-point":
            return self.k_point(evaluated_pop, 3, probability)
        elif self.decision == "uniform":
            return self.uniform(evaluated_pop, probability)
        elif self.decision == "arithmetic":
            return self.arithmetic_crossover(evaluated_pop, probability)
        elif self.decision == 'linear':
            return self.linear_crossover(evaluated_pop, probability)
        elif self.decision == 'blend_crossover_alpha':
            return self.blend_crossover_alpha(evaluated_pop, alpha)
        elif self.decision == 'blend_crossover_alpha_beta':
            return self.blend_crossover_alpha_beta(evaluated_pop, alpha, beta)
        elif self.decision == 'average_crossover':
            return self.average_crossover(evaluated_pop, probability)
        elif self.decision == 'flat_crossover':
            return self.flat_crossover(evaluated_pop, probability)
        else:
            raise NameError("Not a type of crossover")

    def k_point(self, pop, k, probability):
        pop_size = pop.shape[0]
        new_pop = []

        # Selecting random crossover points
        points = np.random.randint(0, pop_size, size = k)
        points.sort()
        points = self.create_uniques(points)

        for i in range(0, pop_size, 2):
            parent1 = pop[i]
            parent2 = pop[i+1]
            child1 = np.zeros_like(parent1)
            child2 = np.zeros_like(parent2)
            for i in range(0, len(points), 1):
                if np.random.rand() < probability:
                    child1 = np.concatenate([parent1[:points[i]], parent2[points[i]:points[i+1]], parent1[points[i+1]:]])
                    child2 = np.concatenate([parent2[:points[i]], parent1[points[i]:points[i+1]], parent2[points[i+1]:]])
                    new_pop.append(child1)
                    new_pop.append(child2)
                else:
                    new_pop.append(parent1)
                    new_pop.append(parent2)

        return np.array(new_pop)

    def uniform(self, pop, probability):
        pop_size = pop.shape[0]
        new_pop = []
        parent1 = []
        parent2 = []

        for i in range(0, pop_size, 4):
            parent1 = pop[i], pop[i+1]
            parent2 = pop[i+1], pop[i+2]
            child1 = np.zeros_like(parent1)
            child2 = np.zeros_like(parent2)
            for j in range(len(parent1)):
                if np.random.rand() < probability:
                    child1[j] = parent2[j]
                    child2[j] = parent1[j]
                else:
                    child1[j] = parent1[j]
                    child2[j] = parent2[j]
            new_pop.append(child1)
            new_pop.append(child2)
        return np.array(new_pop)
    
    def arithmetic_crossover(self, pop, probability):
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

    def linear_crossover(self, pop, probability):
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
                evaluate = [self.evaluate(parent_size, r) for r in vectors]
                sorted_pairs = sorted(zip(vectors, evaluate), key=lambda x: x[1])
                offsprings = [pair[0] for pair in sorted_pairs]

                new_pop.append(offsprings[-2])
                new_pop.append(offsprings[-1])

        return np.array(new_pop)

    def evaluate(self, n_dimensions, point):
        func = bf.Rana(n_dimensions=n_dimensions)
        return func(point)

    def blend_crossover_alpha(self, pop, alpha):
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

    def blend_crossover_alpha_beta(self, pop, alpha, beta):
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

    def average_crossover(self, pop, probability):
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

    def flat_crossover(self, pop, probability):
        new_pop=[]
        for i in range(0, len(pop), 4):
            k = random.random()
            if k < probability and i + 3 < len(pop):
                parent1_x1 = pop[i]  # x1
                parent2_y1 = pop[i + 1]  # y1
                parent3_x2 = pop[i + 2]  # x2
                parent4_y2 = pop[i + 3]  # y2

                x1_new = random.uniform(parent1_x1, parent3_x2)
                y1_new = random.uniform(parent2_y1, parent4_y2)

                new_pop.extend([x1_new, y1_new])

        return np.array(new_pop)




    def create_uniques(points):
        unq, c = np.unique(points, return_counts=1)
        m = np.isin(points, unq[c > 1])
        unique = np.setdiff1d(np.arange(len(points)),points[~m])
        points[m] = unique
        points.sort()

        return points