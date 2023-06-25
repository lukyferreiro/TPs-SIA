from abc import ABC, abstractmethod
import numpy as np

class Activation(ABC):
    _name = "activation name"

    @abstractmethod
    def apply(self, x):
        pass

    @abstractmethod
    def derivative(self, x):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Identity(Activation):
    _name = "Identity function"
    range = [None, None]

    def apply(self, x):
        return x

    def derivative(self, x):
        return np.ones(x.shape)

    def __str__(self):
        return "Identity"


class Sigmoid(Activation):
    _name = "Sigmoid function"

    range = [0, 1]

    def apply(self, x):
        return 1. / (1. + np.exp(-x))

    def derivative(self, x):
        return self.apply(x) * (1. - self.apply(x))

    def __str__(self):
        return "Sigmoid"


class Tanh(Activation):
    _name = "Tanh - Hyperbolic tangent"

    range = [-1, 1]
    def apply(self, x):
        return np.tanh(x)

    def derivative(self, x):
        return 1. - np.power(np.tanh(x), 2)

    def __str__(self):
        return "Tanh"


class ReLU(Activation):
    _name = "ReLU - Rectified linear unit"

    range = [0, None]
    def apply(self, x):
        return x * (x > 0)

    def derivative(self, x):
        return 1. * (x > 0)

    def __str__(self):
        return "ReLU"
