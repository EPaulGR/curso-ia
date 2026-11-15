"""Ejercicio 2 — Reproducibilidad: semillas y resumen multi-semilla.

- `fijar_semillas(seed)`: fija random, numpy (np.random.seed) y, si están instalados, torch y mlx.
  Devuelve lista de nombres de librerías fijadas (siempre incluye "random" y "numpy").
- `correr_semillas(fn, semillas)`: fn(seed) -> float; devuelve dict {"media", "std" (ddof=1), "valores"}.
- `formato_resultado(res, decimales=2)`: "media ± std (n=K)".
"""
import importlib.util
import random
import numpy as np


def fijar_semillas(seed):
    raise NotImplementedError  # TODO: implementa esta función


def correr_semillas(fn, semillas):
    raise NotImplementedError  # TODO: implementa esta función


def formato_resultado(res, decimales=2):
    raise NotImplementedError  # TODO: implementa esta función
