from app.algorithms.population import *


def new_pop_from_indexes(pop, indexes):
    return np.array([pop[i] for i in indexes])


class Selection:
    def __init__(self, decision, percentage, tournament_size):
        self.percentage = percentage
        self.decision = decision
        self.tournament_size = tournament_size

    def select(self, pop, evaluated_pop):
        if self.decision == 'best':
            return self.best(pop, evaluated_pop)
        if self.decision == 'roulette_wheel':
            return self.roulette_wheel(pop, evaluated_pop)
        if self.decision == 'tournament':
            return self.tournament(pop, evaluated_pop)
        else:
            raise NameError("Not a type of selection")

    def best(self, pop, evaluated_pop):
        pop_size = pop.shape[0]
        not_selected_indexes = [i for i in range(pop_size)]

        n_selected = int(evaluated_pop.size * self.percentage)
        selected_indexes = evaluated_pop.argsort()[:n_selected]

        selected = new_pop_from_indexes(pop, selected_indexes)
        not_selected_indexes = [i for i in not_selected_indexes if i not in selected_indexes]
        not_selected = new_pop_from_indexes(pop, not_selected_indexes)

        return selected, not_selected

    def roulette_wheel(self, pop, evaluated_pop):
        evaluated_pop = 1 / (evaluated_pop + 1)
        total = np.sum(evaluated_pop)
        scores = np.array([x / total for x in evaluated_pop])  # probability 1/Sum

        # sum of two probabilities one by one. Example, p [1, 2, 3, 4] then distr [1, 3, 6, 10]
        distribuer = np.concatenate(([0], np.cumsum(scores)))

        rng = np.random.default_rng()

        indexes = []
        for _ in range(pop.shape[0]):
            rng_num = rng.random()  # number drawn

            for index in range(1, distribuer.shape[0]):
                if rng_num > distribuer[index - 1] and rng_num < distribuer[index]:
                    indexes.append(index - 1)
                    break

        new_pop = pop[indexes]

        return new_pop, []

    def tournament(self, pop, evaluated_pop):
        pop_size = pop.shape[0]
        # k = pop_size // (int(self.percentage * pop_size))
        k = self.tournament_size
        not_selected_indexes = [i for i in range(pop_size)]

        selected_indexes = np.array([i for i in range(len(evaluated_pop))])
        np.random.shuffle(selected_indexes)
        selected_indexes = np.array_split(selected_indexes, int(len(evaluated_pop) / k))

        selected_indexes = list(map(lambda x: min(x, key=lambda y: evaluated_pop[y]), selected_indexes))
        selected = new_pop_from_indexes(pop, selected_indexes)

        not_selected_indexes = [i for i in not_selected_indexes if i not in selected_indexes]
        not_selected = new_pop_from_indexes(pop, not_selected_indexes)

        return selected, not_selected

