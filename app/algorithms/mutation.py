import random
import numpy as np

class Mutation:
    def __init__(self, decision, percentage):
        self.percentage = percentage
        self.decision = decision

    def select(self, evaluated_pop):
        if self.decision == 'one point':
            return self.mutation_one_point(evaluated_pop)
        if self.decision == 'two point':
            return self.mutation_two_point(evaluated_pop)
        if self.decision == 'edge':
            return self.mutation_edge(evaluated_pop)
        else:
            raise NameError("Not a type of selection")

    def mutation_one_point(offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            mutation_offspring = []

            # Mutation changes a single gene in each offspring randomly.
            for gene in offspring_crossover:

                random_idx_in_bin = random.randint(0, len(gene) - 1)
                gene = list(gene)

                if gene[random_idx_in_bin] == '0':
                    gene[random_idx_in_bin] = '1'
                else:
                    gene[random_idx_in_bin] = '0'
                gene = ''.join(gene)
            
                mutation_offspring.append(gene)

            offspring_crossover = np.array(mutation_offspring)
        
        return offspring_crossover

    def mutation_edge(offspring_crossover, percentage):

        if Mutation.check_percentage(percentage):

            mutation_offspring = []

            # Mutation changes a single gene in each offspring randomly.
            for gene in offspring_crossover:
                gene = list(gene)

                if gene[len(gene) - 1] == '0':
                    gene[len(gene) - 1] = '1'
                else:
                    gene[len(gene) - 1] = '0'
                gene = ''.join(gene)
            
                mutation_offspring.append(gene)

            offspring_crossover = np.array(mutation_offspring)

        return offspring_crossover

    def mutation_two_point(offspring_crossover, percentage):

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

if __name__ == "__main__":
    bin_repr = ["11111111111111111111", "00000000000000000000"]
    offspring_crossover = np.array(bin_repr)

    mutation_result = Mutation.mutation_edge(offspring_crossover, 20)
    print(f"edge = {mutation_result}")

    mutation_result = Mutation.mutation_one_point(offspring_crossover, 20)
    print(f"mutation one point = {mutation_result}")

    mutation_result = Mutation.mutation_two_point(offspring_crossover, 20)
    print(f"mutation two point = {mutation_result}")
