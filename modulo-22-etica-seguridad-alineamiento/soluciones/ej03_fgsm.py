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
    p = _sig(x @ w + b)
    return (p - y)[..., None] * w if np.ndim(p) else (p - y) * w


def fgsm(w, b, x, y, eps):
    return np.clip(x + eps * np.sign(gradiente_entrada(w, b, x, y)), 0, 1)


def exactitud(w, b, X, Y):
    return float(np.mean((_sig(X @ w + b) > 0.5) == Y))


def entrenamiento_adversarial(X, Y, eps, epocas=200, lr=0.5, seed=0):
    rng = np.random.default_rng(seed)
    w, b = rng.normal(0, 0.01, X.shape[1]), 0.0
    for _ in range(epocas):
        Xa = fgsm(w, b, X, Y, eps)
        Xm, Ym = np.vstack([X, Xa]), np.concatenate([Y, Y])
        p = _sig(Xm @ w + b)
        w -= lr * Xm.T @ (p - Ym) / len(Ym)
        b -= lr * np.mean(p - Ym)
    return w, b
