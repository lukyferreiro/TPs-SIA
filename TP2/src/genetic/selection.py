import numpy as np

"""
Implementar:
    --Elite
    --Por ruleta
    --Universal
    --Torneos
    --Por ranking
    --Boltzmann
"""


def selector(population, N, method):
    match method:
        case "ELITE":
            return select_elite(population, N)
        case "ROULETTE":
            return select_roulette(population, N)
        case "UNIVERSAL":
            return select_universal(population, N)
        case "TOURNAMENT":
            return select_tournament(population, N)


def select_elite(population, K):
    sorted_subjects = sorted(population, key=lambda x: x.fitness, reverse=True)
    return sorted_subjects[:K]


def select_roulette(population, K):
    sorted_subjects = sorted(population, key=lambda x: x.get_fitness(), reverse=True)
    fitness = np.array([subject.get_fitness() for subject in sorted_subjects])
    sum_fitness = np.sum(fitness)

    ps = fitness / sum_fitness
    qs = np.cumsum(ps)
    rs = np.random.uniform(0., 1., size=(K,))

    selection = []
    for ri in rs:
        for i in range(len(qs)):
            if qs[i - 1] < ri <= qs[i]:
                selection.append(sorted_subjects[i])

    return np.array(selection)


def select_universal(population, N):
    pass  #TODO


def select_tournament(population, K):
    selection = []
    for i in range(K):
        # Seleccionar dos individuos al azar de la población
        idx = np.random.choice(len(population), size=2, replace=False)
        competitors = population[idx]

        # Seleccionar al ganador como el individuo con la mayor aptitud
        winner = max(competitors, key=lambda subject: subject.get_fitness())
        selection.append(winner)

    return np.array(selection)
