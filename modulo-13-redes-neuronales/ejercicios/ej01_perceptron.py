# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 01 — Perceptrón de Rosenblatt."""
import numpy as np

def entrenar_perceptron(X, y, epocas=50, lr=1.0):
    """y ∈ {-1, +1}. Regla: si y·(w·x+b) <= 0 → w += lr·y·x, b += lr·y. Devuelve (w, b)."""
    raise NotImplementedError  # TODO

def predecir(X, w, b):
    """Devuelve el signo (-1/+1) de X·w + b."""
    raise NotImplementedError  # TODO
