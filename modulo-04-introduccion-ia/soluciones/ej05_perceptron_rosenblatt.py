"""Ejercicio 05 — Perceptrón de Rosenblatt (1958) y la crítica de Minsky-Papert (XOR)."""
import numpy as np


def entrenar_perceptron(X, y, lr=1.0, epocas=100):
    """y en {0,1}. Regla: w += lr (y - y_hat) x, con sesgo. Devuelve (w, b, convergio)."""
    X = np.asarray(X, float); w = np.zeros(X.shape[1]); b = 0.0
    for _ in range(epocas):
        errores = 0
        for xi, yi in zip(X, y):
            e = yi - int(xi @ w + b > 0)
            if e:
                w += lr * e * xi; b += lr * e; errores += 1
        if errores == 0:
            return w, b, True
    return w, b, False


def predecir(w, b, X):
    """Predicciones 0/1."""
    return (np.asarray(X, float) @ w + b > 0).astype(int)
