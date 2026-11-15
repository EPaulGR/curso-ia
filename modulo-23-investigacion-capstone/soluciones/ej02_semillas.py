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
    random.seed(seed)
    np.random.seed(seed)
    hechas = ["random", "numpy"]
    if importlib.util.find_spec("torch"):
        import torch
        torch.manual_seed(seed)
        hechas.append("torch")
    if importlib.util.find_spec("mlx"):
        import mlx.core as mx
        mx.random.seed(seed)
        hechas.append("mlx")
    return hechas


def correr_semillas(fn, semillas):
    v = np.array([fn(s) for s in semillas], float)
    return {"media": float(v.mean()), "std": float(v.std(ddof=1)) if len(v) > 1 else 0.0, "valores": v.tolist()}


def formato_resultado(res, decimales=2):
    return f"{res['media']:.{decimales}f} ± {res['std']:.{decimales}f} (n={len(res['valores'])})"
