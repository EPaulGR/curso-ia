# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 06 — Mini motor de autodiferenciación escalar (estilo micrograd)."""
import math

class Valor:
    """Nodo de un grafo computacional con gradiente."""

    def __init__(self, dato, hijos=(), op=''):
        raise NotImplementedError  # TODO

    def __add__(self, o):
        """Suma."""
        raise NotImplementedError  # TODO

    def __mul__(self, o):
        """Producto."""
        raise NotImplementedError  # TODO

    def __pow__(self, k):
        """Potencia con exponente numérico."""
        raise NotImplementedError  # TODO

    def tanh(self):
        """Tangente hiperbólica."""
        raise NotImplementedError  # TODO

    def exp(self):
        """Exponencial."""
        raise NotImplementedError  # TODO

    def backward(self):
        """Orden topológico y propagación hacia atrás desde este nodo."""
        raise NotImplementedError  # TODO

    def __radd__(self, o):
        """o + self."""
        raise NotImplementedError  # TODO

    def __rmul__(self, o):
        """o * self."""
        raise NotImplementedError  # TODO

    def __neg__(self):
        """-self."""
        raise NotImplementedError  # TODO

    def __sub__(self, o):
        """self - o."""
        raise NotImplementedError  # TODO

    def __truediv__(self, o):
        """self / o."""
        raise NotImplementedError  # TODO
