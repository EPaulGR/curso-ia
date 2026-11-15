"""Ejercicio 02 — Regresión logística binaria (ISLP cap. 4; Bishop cap. 5).

p(y=1|x) = σ(wᵀx + b),  σ(z) = 1/(1+e^{−z})
Pérdida (entropía cruzada binaria + L2):
    J = −(1/n) Σ [y log p + (1−y) log(1−p)] + (λ/2)‖w‖²
Gradiente: ∇_w = (1/n) Xᵀ(p − y) + λw ;  ∇_b = mean(p − y)
"""
import numpy as np


def sigmoide(z):
    """σ(z) numéricamente estable."""
    raise NotImplementedError  # TODO: implementa esta función


def entropia_cruzada(y, p, eps=1e-12):
    """Entropía cruzada binaria media."""
    raise NotImplementedError  # TODO: implementa esta función


def entrenar_logistica(X, y, lr=0.1, epocas=2000, lam=0.0):
    """Devuelve (w, b) entrenados por descenso de gradiente desde cero."""
    raise NotImplementedError  # TODO: implementa esta función


def predecir_proba(w, b, X):
    """p(y=1|x)."""
    raise NotImplementedError  # TODO: implementa esta función
