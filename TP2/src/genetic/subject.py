import numpy as np
from colors import get_distance_between_colors, MAX_DISTANCIA

class Subject:
   
    def __init__(self, palette, generation, target_color):
        self.color_proportions = np.random.default_rng().uniform(0., 1., size=(len(palette)))
        self.color_rgb = self.mix_color(palette)
        self.generation = generation
        self.fitness = self.calculate_fitness(target_color)

        
    def set_color_proportions(self, color_proportions):
        self.color_proportions = color_proportions

    def set_color_rgb(self, color_rgb):
        self.color_rgb = color_rgb

    def get_color_proportions(self):
        return self.color_proportions

    def get_color_rgb(self):
        return self.color_rgb
    
    def get_generation(self):
        return self.generation
    
    def get_fitness(self):
        return self.fitness
    
    def mix_color(self, palette):
        #TODO
        """
        """

    def calculate_fitness(self, target_color):
        return 1 - (get_distance_between_colors(self.color_rgb, target_color) / MAX_DISTANCIA)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.color_rgb != other.color_rgb:
            return False
        return True

    def __hash__(self):
        return hash(self.color_rgb)
    