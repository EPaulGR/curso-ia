"""Ejercicio 2 — Estrategias de muestreo para generación de texto.

Todas reciben `logits` (np.ndarray 1-D) y devuelven una distribución de probabilidad.
- `softmax_temperatura(logits, T)`: softmax(logits / T), numéricamente estable.
- `top_k(logits, k)`: conserva los k logits mayores (resto prob 0) y normaliza.
- `top_p(logits, p)`: núcleo mínimo de tokens (ordenados por prob) cuya suma >= p.
- `muestrear(probs, rng)`: índice muestreado con `rng.choice`.
"""
import numpy as np


def softmax_temperatura(logits, T=1.0):
    z = np.asarray(logits, float) / T
    z = z - z.max()
    e = np.exp(z)
    return e / e.sum()


def top_k(logits, k):
    logits = np.asarray(logits, float)
    idx = np.argsort(logits)[::-1][:k]
    m = np.full_like(logits, -np.inf)
    m[idx] = logits[idx]
    return softmax_temperatura(m)


def top_p(logits, p):
    probs = softmax_temperatura(logits)
    orden = np.argsort(probs)[::-1]
    acum = np.cumsum(probs[orden])
    n = int(np.searchsorted(acum, p) + 1)
    out = np.zeros_like(probs)
    out[orden[:n]] = probs[orden[:n]]
    return out / out.sum()


def muestrear(probs, rng):
    return int(rng.choice(len(probs), p=probs))
