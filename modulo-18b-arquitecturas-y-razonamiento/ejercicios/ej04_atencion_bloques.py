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
    raise NotImplementedError  # TODO


def atencion_por_bloques(Q, K, V, bloque=4):
    """Misma salida que atencion_ingenua procesando K,V en bloques."""
    raise NotImplementedError  # TODO
