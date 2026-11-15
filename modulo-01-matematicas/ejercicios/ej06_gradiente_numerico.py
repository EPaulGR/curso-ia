"""Ejercicio 06 — Gradiente numérico y verificación de gradientes."""
import numpy as np

def gradiente_numerico(f, x, h=1e-05):
    """Gradiente de f en x por diferencias centrales."""
    raise NotImplementedError  # TODO

def grad_cuadratica(A, b, x):
    """Gradiente analítico de f(x) = 0.5 x^T A x - b^T x (A no necesariamente simétrica)."""
    raise NotImplementedError  # TODO

def grad_minimos_cuadrados(X, y, w):
    """Gradiente de L(w) = ||Xw - y||^2 / n."""
    raise NotImplementedError  # TODO

def error_relativo(g1, g2):
    """||g1-g2|| / (||g1||+||g2||+1e-12): < 1e-6 indica gradiente correcto."""
    raise NotImplementedError  # TODO
