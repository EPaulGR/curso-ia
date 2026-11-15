"""Ej 01 — Atención de producto punto escalado en NumPy."""
import numpy as np


def softmax(z, eje=-1):
    """Softmax estable."""
    e = np.exp(z - z.max(axis=eje, keepdims=True))
    return e / e.sum(axis=eje, keepdims=True)


def atencion(Q, K, V, mascara=None):
    """Q (n,d), K (m,d), V (m,dv). mascara (n,m) booleana: True = permitido.
    Devuelve (salida (n,dv), pesos (n,m)). softmax(QKᵀ/√d) V."""
    s = Q @ K.T / np.sqrt(Q.shape[-1])
    if mascara is not None:
        s = np.where(mascara, s, -1e9)
    p = softmax(s)
    return p @ V, p
