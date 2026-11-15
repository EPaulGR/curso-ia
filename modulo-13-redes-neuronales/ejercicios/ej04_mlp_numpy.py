# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 04 — MLP de una capa oculta con backprop manual en NumPy (clasificación multiclase)."""
import numpy as np

class MLP:
    """x → Linear(d,h) → ReLU → Linear(h,c) → softmax + entropía cruzada."""

    def __init__(self, d, h, c, semilla=0):
        """Inicialización He para W1, Xavier para W2; sesgos en cero."""
        raise NotImplementedError  # TODO

    def forward(self, X):
        """Devuelve logits (n, c) y guarda la caché necesaria para backward."""
        raise NotImplementedError  # TODO

    def perdida(self, logits, y):
        """Entropía cruzada media con etiquetas enteras y; guarda probabilidades."""
        raise NotImplementedError  # TODO

    def backward(self):
        """Calcula y devuelve dict de gradientes {'W1','b1','W2','b2'}."""
        raise NotImplementedError  # TODO

    def paso(self, g, lr):
        """Descenso de gradiente sobre los parámetros."""
        raise NotImplementedError  # TODO

def entrenar(X, y, h=32, epocas=300, lr=0.5, semilla=0):
    """Entrena un MLP con gradiente completo; devuelve (modelo, historial_de_perdidas)."""
    raise NotImplementedError  # TODO
