"""Ejercicio 3 — Cuantización de pesos a mano.

- `cuantizar_int8(w)`: simétrica por tensor. escala = max|w| / 127. Devuelve (q int8, escala).
- `decuantizar(q, escala)`.
- `cuantizar_4bit_grupos(w, grupo)`: w 1-D, por grupos de tamaño `grupo`, asimétrica:
  escala = (max-min)/15, cero = min; q en [0, 15] (uint8). Devuelve (q, escalas, ceros).
- `decuantizar_4bit(q, escalas, ceros, grupo)`.
- `error_mse(a, b)`.
Así funcionan (simplificado) los formatos GGUF Q4 y MLX 4-bit.
"""
import numpy as np


def cuantizar_int8(w):
    escala = float(np.abs(w).max()) / 127 or 1.0
    q = np.clip(np.round(w / escala), -127, 127).astype(np.int8)
    return q, escala


def decuantizar(q, escala):
    return q.astype(np.float32) * escala


def cuantizar_4bit_grupos(w, grupo=32):
    g = np.asarray(w, np.float32).reshape(-1, grupo)
    mn, mx = g.min(1), g.max(1)
    escalas = np.where(mx > mn, (mx - mn) / 15, 1.0)
    q = np.clip(np.round((g - mn[:, None]) / escalas[:, None]), 0, 15).astype(np.uint8)
    return q.reshape(-1), escalas, mn


def decuantizar_4bit(q, escalas, ceros, grupo=32):
    g = q.reshape(-1, grupo).astype(np.float32)
    return (g * escalas[:, None] + ceros[:, None]).reshape(-1)


def error_mse(a, b):
    return float(np.mean((np.asarray(a) - np.asarray(b)) ** 2))
