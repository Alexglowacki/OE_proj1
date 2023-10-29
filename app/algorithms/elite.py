import numpy as np

class Elite:
    def __init__(self, amount):
        self.amount = amount

    def elitism(self, pop, amount):
        amount = amount/100
        pop_size = pop.shape[0]
        # not_selected_indexes = [i for i in range(pop_size)]

        n_selected = int(pop_size * amount)
        # selected_indexes = np.argsort(pop)[:n_selected]

        # selected = np.array([pop[i] for i in selected_indexes])
        # not_selected_indexes = [i for i in not_selected_indexes if i not in selected_indexes]
        # not_selected = np.array([pop[i] for i in not_selected_indexes])

        selected = np.argsort(pop)
        selected = selected[:n_selected]
        not_selected = pop[n_selected:]

        return selected, not_selected