"""Ejercicio 08 — Regresión lineal: ecuaciones normales vs descenso de gradiente."""
import numpy as np


def agregar_sesgo(X):
    """Añade una columna de unos al inicio."""
    return np.hstack([np.ones((len(X), 1)), X])


def ecuaciones_normales(X, y):
    """w que minimiza ||Xw-y||^2 resolviendo X^T X w = X^T y (usa np.linalg.solve)."""
    return np.linalg.solve(X.T @ X, X.T @ y)


def ridge(X, y, lam):
    """Regresión ridge: (X^T X + lam I) w = X^T y."""
    return np.linalg.solve(X.T @ X + lam * np.eye(X.shape[1]), X.T @ y)


def regresion_gd(X, y, lr=0.1, pasos=2000):
    """w por descenso de gradiente sobre el MSE, iniciando en ceros."""
    w = np.zeros(X.shape[1])
    for _ in range(pasos):
        w -= lr * 2 * X.T @ (X @ w - y) / len(y)
    return w
