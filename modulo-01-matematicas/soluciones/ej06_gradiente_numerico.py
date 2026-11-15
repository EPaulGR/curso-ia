"""Ejercicio 06 — Gradiente numérico y verificación de gradientes."""
import numpy as np


def gradiente_numerico(f, x, h=1e-5):
    """Gradiente de f en x por diferencias centrales."""
    x = np.asarray(x, float); g = np.zeros_like(x)
    for i in range(x.size):
        e = np.zeros_like(x); e.flat[i] = h
        g.flat[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g


def grad_cuadratica(A, b, x):
    """Gradiente analítico de f(x) = 0.5 x^T A x - b^T x (A no necesariamente simétrica)."""
    A = np.asarray(A, float)
    return 0.5 * (A + A.T) @ x - b


def grad_minimos_cuadrados(X, y, w):
    """Gradiente de L(w) = ||Xw - y||^2 / n."""
    return 2 * X.T @ (X @ w - y) / len(y)


def error_relativo(g1, g2):
    """||g1-g2|| / (||g1||+||g2||+1e-12): < 1e-6 indica gradiente correcto."""
    return float(np.linalg.norm(g1 - g2) / (np.linalg.norm(g1) + np.linalg.norm(g2) + 1e-12))
