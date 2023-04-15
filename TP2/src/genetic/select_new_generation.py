import numpy as np

def select_new_generation(mutated_children, parents, N, K, select_new_generation_type):
    switcher = {
        "USE_ALL": select_use_all(mutated_children, parents, N),
        "NEW_OVER_ACTUAL": select_new_over_actual(mutated_children, parents, N, K),
    }

    return switcher.get(select_new_generation_type, "Metodo de seleccion de nueva generacion invalido")

"""
Generando K hijos de N padres. La nueva generación se formará seleccionando
N individuos del conjunto de [N + K]
"""
def select_use_all(mutated_children, parents, N):
    all_subjects = np.concatenate((mutated_children, parents), axis=0)
    count_all_subjects = len(all_subjects)
    # Seleccionar N individuos del conjunto [N+K]
    idx = np.random.default_rng().choice(range(count_all_subjects), size=N, replace=True)
    return [all_subjects[i] for i in idx]

"""
Generando K hijos de N padres.
- K > N : La nueva generación se genera seleccionando N de los K hijos únicamente.
- K <= N: La nueva generación se conformará por los K hijos generados + (N-K) individuos
     seleccionados de la generación actual.
"""
def select_new_over_actual(mutated_children, parents, N, K):
    if(K > N):
        return mutated_children[:K]
    else: 
        new_generation = mutated_children[:K]
        return np.concatenate((new_generation, parents[:N-K]), axis=0)