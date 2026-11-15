"""Ej 01 — Perceptrón de Rosenblatt."""
import numpy as np


def entrenar_perceptron(X, y, epocas=50, lr=1.0):
    """y ∈ {-1, +1}. Regla: si y·(w·x+b) <= 0 → w += lr·y·x, b += lr·y. Devuelve (w, b)."""
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(epocas):
        for xi, yi in zip(X, y):
            if yi * (xi @ w + b) <= 0:
                w += lr * yi * xi
                b += lr * yi
    return w, b


def predecir(X, w, b):
    """Devuelve el signo (-1/+1) de X·w + b."""
    return np.where(X @ w + b >= 0, 1, -1)
