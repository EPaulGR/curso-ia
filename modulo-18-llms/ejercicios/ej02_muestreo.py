"""Ejercicio 2 — Estrategias de muestreo para generación de texto.

Todas reciben `logits` (np.ndarray 1-D) y devuelven una distribución de probabilidad.
- `softmax_temperatura(logits, T)`: softmax(logits / T), numéricamente estable.
- `top_k(logits, k)`: conserva los k logits mayores (resto prob 0) y normaliza.
- `top_p(logits, p)`: núcleo mínimo de tokens (ordenados por prob) cuya suma >= p.
- `muestrear(probs, rng)`: índice muestreado con `rng.choice`.
"""
import numpy as np


def softmax_temperatura(logits, T=1.0):
    raise NotImplementedError  # TODO: implementa esta función


def top_k(logits, k):
    raise NotImplementedError  # TODO: implementa esta función


def top_p(logits, p):
    raise NotImplementedError  # TODO: implementa esta función


def muestrear(probs, rng):
    raise NotImplementedError  # TODO: implementa esta función
