"""Ejercicio 01 — Rotary Position Embeddings (RoPE).

RoPE (Su et al., 2021) rota cada par de dimensiones (2i, 2i+1) de q y k un
ángulo pos * theta_i, con theta_i = base^(-2i/d). Propiedad clave: el producto
<rope(q, m), rope(k, n)> depende solo de (m - n): posición RELATIVA.

Implementa:
  - frecuencias(d, base): vector theta de tamaño d/2.
  - aplicar_rope(x, posiciones, base): x de forma (T, d), d par.
"""
import numpy as np


def frecuencias(d, base=10000.0):
    """Devuelve theta_i = base^(-2i/d) para i = 0..d/2-1."""
    i = np.arange(d // 2)
    return base ** (-2.0 * i / d)


def aplicar_rope(x, posiciones, base=10000.0):
    """Rota pares (x[2i], x[2i+1]) por el ángulo pos*theta_i. Devuelve (T, d)."""
    x = np.asarray(x, dtype=float)
    T, d = x.shape
    ang = np.outer(np.asarray(posiciones, dtype=float), frecuencias(d, base))
    cos, sin = np.cos(ang), np.sin(ang)
    x1, x2 = x[:, 0::2], x[:, 1::2]
    out = np.empty_like(x)
    out[:, 0::2] = x1 * cos - x2 * sin
    out[:, 1::2] = x1 * sin + x2 * cos
    return out
