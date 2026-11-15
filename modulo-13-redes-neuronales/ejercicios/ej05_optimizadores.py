# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 05 — SGD con momentum y Adam implementados a mano."""
import numpy as np

class Momentum:
    """v = β·v + g ; θ -= lr·v"""

    def __init__(self, lr=0.01, beta=0.9):
        raise NotImplementedError  # TODO

    def paso(self, theta, g):
        """Devuelve theta actualizado."""
        raise NotImplementedError  # TODO

class Adam:
    """Adam (Kingma & Ba, 2015) con corrección de sesgo."""

    def __init__(self, lr=0.001, b1=0.9, b2=0.999, eps=1e-08):
        raise NotImplementedError  # TODO

    def paso(self, theta, g):
        """Devuelve theta actualizado."""
        raise NotImplementedError  # TODO

def minimizar_rosenbrock(opt, pasos=5000):
    """Minimiza f(x,y)=(1-x)^2+100(y-x^2)^2 desde (-1.5, 2). Devuelve el punto final."""
    raise NotImplementedError  # TODO
