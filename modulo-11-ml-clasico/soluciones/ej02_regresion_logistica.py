"""Ejercicio 02 — Regresión logística binaria (ISLP cap. 4; Bishop cap. 5).

p(y=1|x) = σ(wᵀx + b),  σ(z) = 1/(1+e^{−z})
Pérdida (entropía cruzada binaria + L2):
    J = −(1/n) Σ [y log p + (1−y) log(1−p)] + (λ/2)‖w‖²
Gradiente: ∇_w = (1/n) Xᵀ(p − y) + λw ;  ∇_b = mean(p − y)
"""
import numpy as np


def sigmoide(z):
    """σ(z) numéricamente estable."""
    z = np.asarray(z, float)
    return np.where(z >= 0, 1 / (1 + np.exp(-np.abs(z))), np.exp(-np.abs(z)) / (1 + np.exp(-np.abs(z))))


def entropia_cruzada(y, p, eps=1e-12):
    """Entropía cruzada binaria media."""
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def entrenar_logistica(X, y, lr=0.1, epocas=2000, lam=0.0):
    """Devuelve (w, b) entrenados por descenso de gradiente desde cero."""
    X = np.asarray(X, float)
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(epocas):
        p = sigmoide(X @ w + b)
        w -= lr * (X.T @ (p - y) / len(y) + lam * w)
        b -= lr * float(np.mean(p - y))
    return w, b


def predecir_proba(w, b, X):
    """p(y=1|x)."""
    return sigmoide(np.asarray(X, float) @ w + b)
