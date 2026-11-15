# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 01 — Atención de producto punto escalado en NumPy."""
import numpy as np

def softmax(z, eje=-1):
    """Softmax estable."""
    raise NotImplementedError  # TODO

def atencion(Q, K, V, mascara=None):
    """Q (n,d), K (m,d), V (m,dv). mascara (n,m) booleana: True = permitido.
    Devuelve (salida (n,dv), pesos (n,m)). softmax(QKᵀ/√d) V."""
    raise NotImplementedError  # TODO
