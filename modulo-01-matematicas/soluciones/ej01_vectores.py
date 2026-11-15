"""Ejercicio 01 — Vectores. Usa NumPy pero NO np.linalg.norm."""
import numpy as np


def norma(x, p=2):
    """Norma Lp de x; p puede ser 1, 2 o np.inf."""
    x = np.abs(np.asarray(x, float))
    if p == np.inf:
        return x.max()
    return (x ** p).sum() ** (1 / p)


def similitud_coseno(x, y):
    """cos(theta) entre x y y."""
    return float(np.dot(x, y) / (norma(x) * norma(y)))


def proyeccion(x, y):
    """Proyección de x sobre y."""
    y = np.asarray(y, float)
    return np.dot(x, y) / np.dot(y, y) * y
