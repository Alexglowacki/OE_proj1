import numpy as np

class Crossover:
    def __init__(self, decision, probability):
        self.probability = probability
        self.decision = decision

    def select(self, evaluated_pop, k, probability):
        if self.decision == "one-point":
            return self.k_point(evaluated_pop, 1, probability)
        elif self.decision == "two-point":
            return self.k_point(evaluated_pop, 2, probability)
        elif self.decision == "three-point":
            return self.k_point(evaluated_pop, 3, probability)
        elif self.decision == "uniform":
            return self.uniform(evaluated_pop, probability)
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

        for i in range(0, pop_size, 2):
            parent1 = pop[i]
            parent2 = pop[i+1]
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

    def create_uniques(points):
        unq, c = np.unique(points, return_counts=1)
        m = np.isin(points, unq[c > 1])
        unique = np.setdiff1d(np.arange(len(points)),points[~m])
        points[m] = unique
        points.sort()

        return points