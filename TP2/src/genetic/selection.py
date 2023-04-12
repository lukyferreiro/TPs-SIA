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

def selector (population, N, method):
    match method:
        case "ELITE":
            return select_elite(population, N)
        case "ROULETTE":
            return select_roulette(population, N)
        case "UNIVERSAL":
            return select_universal(population,N)
        case "TOURNAMENT":
            return select_tournament(population, N)


def select_elite(population, K):
    sorted_subjects = sorted(population, key=lambda x: x.fitness, reverse=True)
    return sorted_subjects[:K]