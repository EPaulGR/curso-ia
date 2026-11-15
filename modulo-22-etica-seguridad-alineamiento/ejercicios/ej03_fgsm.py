"""Ejercicio 3 — Ataque adversarial FGSM sobre regresión logística (NumPy).

Modelo: p(y=1|x) = sigmoid(w·x + b).
- `gradiente_entrada(w, b, x, y)`: d pérdida_BCE / d x = (p - y) * w.
- `fgsm(w, b, x, y, eps)`: x_adv = clip(x + eps * sign(grad), 0, 1).
- `exactitud(w, b, X, Y)`.
- `entrenamiento_adversarial(X, Y, eps, epocas, lr, seed)`: regresión logística entrenada con
  gradiente descendente sobre una mezcla 50/50 de ejemplos limpios y FGSM generados con el
  modelo actual en cada época. Devuelve (w, b).
Goodfellow, Shlens & Szegedy 2015; Madry et al. 2018 (PGD).
"""
import numpy as np


def _sig(z):
    return 1 / (1 + np.exp(-z))


def gradiente_entrada(w, b, x, y):
    raise NotImplementedError  # TODO: implementa esta función


def fgsm(w, b, x, y, eps):
    raise NotImplementedError  # TODO: implementa esta función


def exactitud(w, b, X, Y):
    raise NotImplementedError  # TODO: implementa esta función


def entrenamiento_adversarial(X, Y, eps, epocas=200, lr=0.5, seed=0):
    raise NotImplementedError  # TODO: implementa esta función
