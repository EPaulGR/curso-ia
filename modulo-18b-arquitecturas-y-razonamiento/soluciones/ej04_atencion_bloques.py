"""Ejercicio 04 — Atención por bloques con online softmax (idea de FlashAttention).

FlashAttention nunca materializa la matriz T x T: recorre K,V por bloques y
mantiene, por fila, el máximo m, la suma l y el acumulador o, reescalándolos:
    m' = max(m, max(s_blk));  l' = l*e^(m-m') + sum e^(s_blk-m')
    o' = o*e^(m-m') + e^(s_blk-m') V_blk
Al final o / l es exactamente softmax(QK^T/sqrt(d)) V.
"""
import numpy as np


def atencion_ingenua(Q, K, V):
    """Referencia: softmax(QK^T/sqrt(d)) V (sin máscara)."""
    s = Q @ K.T / np.sqrt(Q.shape[1])
    s = s - s.max(axis=1, keepdims=True)
    p = np.exp(s)
    return (p / p.sum(axis=1, keepdims=True)) @ V


def atencion_por_bloques(Q, K, V, bloque=4):
    """Misma salida que atencion_ingenua procesando K,V en bloques."""
    T, d = Q.shape
    m = np.full(T, -np.inf)
    l = np.zeros(T)
    o = np.zeros((T, V.shape[1]))
    for i in range(0, K.shape[0], bloque):
        s = Q @ K[i:i + bloque].T / np.sqrt(d)
        m_nuevo = np.maximum(m, s.max(axis=1))
        escala = np.exp(m - m_nuevo)
        p = np.exp(s - m_nuevo[:, None])
        l = l * escala + p.sum(axis=1)
        o = o * escala[:, None] + p @ V[i:i + bloque]
        m = m_nuevo
    return o / l[:, None]
