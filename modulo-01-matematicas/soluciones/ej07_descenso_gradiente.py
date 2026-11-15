"""Ejercicio 07 — Descenso de gradiente, momentum y Adam.
Cada función recibe grad(x), punto inicial x0 y devuelve (x_final, historia) donde historia es la lista de x."""
import numpy as np


def gd(grad, x0, lr=0.1, pasos=100):
    """Descenso de gradiente simple."""
    x = np.array(x0, float); h = [x.copy()]
    for _ in range(pasos):
        x = x - lr * grad(x); h.append(x.copy())
    return x, h


def momentum(grad, x0, lr=0.01, beta=0.9, pasos=100):
    """Descenso con momentum: v = beta v + g ; x -= lr v."""
    x = np.array(x0, float); v = np.zeros_like(x); h = [x.copy()]
    for _ in range(pasos):
        v = beta * v + grad(x); x = x - lr * v; h.append(x.copy())
    return x, h


def adam(grad, x0, lr=0.1, b1=0.9, b2=0.999, eps=1e-8, pasos=100):
    """Adam con corrección de sesgo."""
    x = np.array(x0, float); m = np.zeros_like(x); s = np.zeros_like(x); h = [x.copy()]
    for t in range(1, pasos + 1):
        g = grad(x)
        m = b1 * m + (1 - b1) * g; s = b2 * s + (1 - b2) * g * g
        x = x - lr * (m / (1 - b1 ** t)) / (np.sqrt(s / (1 - b2 ** t)) + eps); h.append(x.copy())
    return x, h


def grad_rosenbrock(x):
    """Gradiente de Rosenbrock f(x,y) = (1-x)^2 + 100 (y-x^2)^2."""
    return np.array([-2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2), 200 * (x[1] - x[0] ** 2)])
