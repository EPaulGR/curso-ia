"""Ej 08 — Dropout invertido, weight decay y early stopping."""
import numpy as np


def dropout(a, p, entrenando, rng):
    """Dropout invertido: en entrenamiento apaga con prob p y escala por 1/(1-p); en inferencia identidad."""
    if not entrenando or p == 0:
        return a
    mascara = (rng.random(a.shape) >= p) / (1 - p)
    return a * mascara


def l2_grad(W, lam):
    """Gradiente de (lam/2)·‖W‖²."""
    return lam * W


def early_stopping(perdidas_val, paciencia):
    """Devuelve el índice de la época donde se detendría el entrenamiento (la mejor antes de agotar paciencia)."""
    mejor, idx, sin_mejora = np.inf, 0, 0
    for i, v in enumerate(perdidas_val):
        if v < mejor:
            mejor, idx, sin_mejora = v, i, 0
        else:
            sin_mejora += 1
            if sin_mejora >= paciencia:
                break
    return idx
