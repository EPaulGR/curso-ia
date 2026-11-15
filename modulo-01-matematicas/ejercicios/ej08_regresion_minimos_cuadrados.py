"""Ejercicio 08 — Regresión lineal: ecuaciones normales vs descenso de gradiente."""
import numpy as np

def agregar_sesgo(X):
    """Añade una columna de unos al inicio."""
    raise NotImplementedError  # TODO

def ecuaciones_normales(X, y):
    """w que minimiza ||Xw-y||^2 resolviendo X^T X w = X^T y (usa np.linalg.solve)."""
    raise NotImplementedError  # TODO

def ridge(X, y, lam):
    """Regresión ridge: (X^T X + lam I) w = X^T y."""
    raise NotImplementedError  # TODO

def regresion_gd(X, y, lr=0.1, pasos=2000):
    """w por descenso de gradiente sobre el MSE, iniciando en ceros."""
    raise NotImplementedError  # TODO
