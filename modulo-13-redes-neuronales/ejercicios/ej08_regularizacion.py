# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-13-redes-neuronales

"""Ej 08 — Dropout invertido, weight decay y early stopping."""
import numpy as np

def dropout(a, p, entrenando, rng):
    """Dropout invertido: en entrenamiento apaga con prob p y escala por 1/(1-p); en inferencia identidad."""
    raise NotImplementedError  # TODO

def l2_grad(W, lam):
    """Gradiente de (lam/2)·‖W‖²."""
    raise NotImplementedError  # TODO

def early_stopping(perdidas_val, paciencia):
    """Devuelve el índice de la época donde se detendría el entrenamiento (la mejor antes de agotar paciencia)."""
    raise NotImplementedError  # TODO
