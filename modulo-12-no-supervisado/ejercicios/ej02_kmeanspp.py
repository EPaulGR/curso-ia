# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-12-no-supervisado

"""Ej 02 — Inicialización k-means++ (Arthur & Vassilvitskii, 2007)."""
import numpy as np

def kmeanspp(X, k, semilla=0):
    """Elige k centroides: el primero al azar, los siguientes con probabilidad proporcional a D(x)^2."""
    raise NotImplementedError  # TODO
