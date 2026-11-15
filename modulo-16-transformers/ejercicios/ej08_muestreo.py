# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 08 — Estrategias de decodificación: temperatura, top-k y top-p (nucleus)."""
import numpy as np

def con_temperatura(logits, t):
    """Probabilidades softmax(logits / t)."""
    raise NotImplementedError  # TODO

def top_k(p, k):
    """Conserva las k probabilidades mayores y renormaliza."""
    raise NotImplementedError  # TODO

def top_p(p, umbral):
    """Conserva el menor conjunto de tokens cuya masa acumulada ≥ umbral; renormaliza."""
    raise NotImplementedError  # TODO
