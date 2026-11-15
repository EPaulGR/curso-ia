"""Ejercicio 07 — Descenso de gradiente, momentum y Adam.
Cada función recibe grad(x), punto inicial x0 y devuelve (x_final, historia) donde historia es la lista de x."""
import numpy as np

def gd(grad, x0, lr=0.1, pasos=100):
    """Descenso de gradiente simple."""
    raise NotImplementedError  # TODO

def momentum(grad, x0, lr=0.01, beta=0.9, pasos=100):
    """Descenso con momentum: v = beta v + g ; x -= lr v."""
    raise NotImplementedError  # TODO

def adam(grad, x0, lr=0.1, b1=0.9, b2=0.999, eps=1e-08, pasos=100):
    """Adam con corrección de sesgo."""
    raise NotImplementedError  # TODO

def grad_rosenbrock(x):
    """Gradiente de Rosenbrock f(x,y) = (1-x)^2 + 100 (y-x^2)^2."""
    raise NotImplementedError  # TODO
