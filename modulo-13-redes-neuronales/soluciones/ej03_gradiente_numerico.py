"""Ej 03 — Verificación de gradientes por diferencias finitas."""
import numpy as np


def gradiente_numerico(f, x, h=1e-5):
    """Gradiente de f escalar respecto a x (array) con diferencias centrales."""
    g = np.zeros_like(x, dtype=float)
    it = np.nditer(x, flags=["multi_index"])
    for _ in it:
        i = it.multi_index
        orig = x[i]
        x[i] = orig + h
        fp = f(x)
        x[i] = orig - h
        fm = f(x)
        x[i] = orig
        g[i] = (fp - fm) / (2 * h)
    return g


def error_relativo(a, b):
    """‖a−b‖ / max(‖a‖+‖b‖, 1e-12)."""
    return float(np.linalg.norm(a - b) / max(np.linalg.norm(a) + np.linalg.norm(b), 1e-12))
