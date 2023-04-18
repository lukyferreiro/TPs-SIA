import numpy as np

def mutator(children, mutation_method, mutation_pm):
    switcher = {
        "ONE_GEN": mutate_one_gen(children, mutation_pm),
        "MULTIGEN_LIMITED": mutate_multigen_limited(children, mutation_pm),
        "MULTIGEN_UNIFORM": mutate_multigen_uniform(children, mutation_pm),
        "COMPLETE": mutate_complete(children, mutation_pm)
    }

    return switcher.get(mutation_method, "Metodo de mutacion invalido")

# Función que realmente modifica el valor del gen pedido
def mutate_gen(gen):
    u = gen * 0.5  
    delta = np.random.default_rng().uniform(-u, u)

    return gen + delta if gen + delta < 1 else 1 

"""
Se altera un solo gen con una probabilidad Pm
"""
def mutate_one_gen(children, mutation_pm):
    children_len = len(children)
    gen_length = len(children[0].get_color_proportions())

    for i in range(children_len):
        # Selecciono idx de gen a modificar (puede cambiarse a choice)
        idx = np.random.default_rng().integers(0, gen_length-1)
        mutate = np.random.default_rng().uniform(0, 1)
        if (mutate < mutation_pm):
            children[i].get_color_proportions()[idx] = mutate_gen(children[i].get_color_proportions()[idx])

    return children

"""
Se selecciona una cantidad [1,M] de genes para mutar, con probabilidad Pm.
"""
def mutate_multigen_limited(children, mutation_pm):
    children_len = len(children)
    gen_length = len(children[0].get_color_proportions())
    M = np.random.default_rng().integers(1, gen_length)

    for i in range(children_len):
        color_props = children[i].get_color_proportions()
        #Seleccciono los M a mutar 
        for j in range(M):
            mutate = np.random.default_rng().uniform(0, 1)
            #change to choice
            if (mutate < mutation_pm):
                color_props[j] = mutate_gen(color_props[j])

    return children

"""
Cada gen tiene una probabilidad Pm de ser mutado.
"""
def mutate_multigen_uniform(children, mutation_pm):
    children_len = len(children)
    gen_length = len(children[0].get_color_proportions())

    for i in range(children_len):
        color_props = children[i].get_color_proportions()

        # Muto todos con posibilidad Pm
        for j in range(gen_length):
            mutate = np.random.default_rng().uniform(0, 1)
            if (mutate < mutation_pm):
                color_props[j] = mutate_gen(color_props[j])

    return children

"""
Con una probabilidad Pm se mutan todos los genes del individuo.
"""
def mutate_complete(children, mutation_pm):
    children_len = len(children)
    gen_length = len(children[0].get_color_proportions())

    for i in range(children_len):
        color_props = children[i].get_color_proportions()
        mutate = np.random.default_rng().uniform(0, 1)

        if (mutate < mutation_pm):
            for j in range(gen_length):
                    color_props[j] = mutate_gen(color_props[j])

    return children
