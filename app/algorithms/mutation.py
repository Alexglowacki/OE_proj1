import random
import numpy as np

class Mutation:
    def __init__(self, decision, percentage, real):
        self.percentage = percentage
        self.decision = decision
        self.real = real

    def select(self, evaluated_pop, percentage):
        if self.real == "1":
            if self.decision == 'one point':
                return self.mutation_one_point(evaluated_pop, percentage)
            if self.decision == 'two point':
                return self.mutation_two_point(evaluated_pop, percentage)
            if self.decision == 'edge':
                return self.mutation_edge(evaluated_pop, percentage)
            else:
                raise NameError("Not a type of mutation")
        else:
            if self.decision == 'one point':
                return self.mutation_one_point_bin(evaluated_pop, percentage)
            if self.decision == 'two point':
                return self.mutation_two_point_bin(evaluated_pop, percentage)
            if self.decision == 'edge':
                return self.mutation_edge_bin(evaluated_pop, percentage)
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
    
    def mutation_one_point_bin(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            mutation_offspring = []

            # Mutation changes a single gene in each offspring randomly.
            for gene in offspring_crossover:

                random_idx_in_1st_point = random.randint(0, len(gene) - 1)

                gene = list(gene)

                if gene[random_idx_in_1st_point] == '0':
                    gene[random_idx_in_1st_point] = '1'
                else:
                    gene[random_idx_in_1st_point] = '0'

                print(gene)

                gene = ''.join(gene)

                mutation_offspring.append(gene)

            offspring_crossover = np.array(mutation_offspring)
        return offspring_crossover

    def mutation_edge_bin(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            mutation_offspring = []

                # Mutation changes a single gene in each offspring randomly.
            for gene in offspring_crossover:
                gene = list(gene)

                if gene[len(gene) - 1] == '0':
                    gene[len(gene) - 1] = '1'
                else:
                    gene[len(gene) - 1] = '0'
                print(gene)
                gene = ''.join(gene)

                mutation_offspring.append(gene)

            offspring_crossover = np.array(mutation_offspring)

        return offspring_crossover

    def mutation_two_point_bin(self, offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            mutation_offspring = []

            # Mutation changes a single gene in each offspring randomly.
            for gene in offspring_crossover:

                random_idx_in_1st_point = random.randint(0, len(gene) - 1)
                random_idx_in_2nd_point = random.randint(0, len(gene) - 1)

                gene = list(gene)

                if gene[random_idx_in_1st_point] == '0':
                    gene[random_idx_in_1st_point] = '1'
                else:
                    gene[random_idx_in_1st_point] = '0'

                if gene[random_idx_in_2nd_point] == '0':
                    gene[random_idx_in_2nd_point] = '1'
                else:
                    gene[random_idx_in_2nd_point] = '0'
                print(gene)
                gene = ''.join(gene)

                mutation_offspring.append(gene)

            offspring_crossover = np.array(mutation_offspring)
        return offspring_crossover
    
    def check_percentage(percentage):
        rng = random.random()
        if 0 < rng < (percentage/100):
            return True
        else:
            return False
