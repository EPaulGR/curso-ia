# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-12-no-supervisado

"""Ej 01 — K-means (algoritmo de Lloyd) desde cero con NumPy."""
import numpy as np

def asignar(X, centroides):
    """Devuelve un arreglo (n,) con el índice del centroide más cercano (distancia euclidiana) a cada punto."""
    raise NotImplementedError  # TODO

def actualizar(X, etiquetas, k):
    """Devuelve (k, d) con la media de los puntos de cada cluster."""
    raise NotImplementedError  # TODO

def _lloyd(X, k, iters, rng):
    """Una corrida de Lloyd desde k puntos aleatorios de X. Devuelve (centroides, etiquetas, inercia)."""
    raise NotImplementedError  # TODO

def kmeans(X, k, iters=100, semilla=0, n_init=10):
    """K-means completo con varios reinicios. Devuelve (centroides, etiquetas, inercia)."""
    raise NotImplementedError  # TODO
