"""Ejercicio 4 — Saliencia y Gradientes Integrados (para un modelo diferenciable dado).

`f(x)` escalar y `grad_f(x)` su gradiente (vectores NumPy).
- `saliencia(grad_f, x)`: |grad_f(x)|.
- `gradiente_x_entrada(grad_f, x)`: grad_f(x) * x.
- `gradientes_integrados(grad_f, x, base, pasos=50)`: (x - base) * promedio de grad_f evaluado en
  base + (k/pasos)(x - base) para k = 1..pasos (regla de Riemann derecha).
Propiedad (completitud): sum(IG) ≈ f(x) - f(base). Sundararajan et al. 2017.
"""
import numpy as np


def saliencia(grad_f, x):
    raise NotImplementedError  # TODO: implementa esta función


def gradiente_x_entrada(grad_f, x):
    raise NotImplementedError  # TODO: implementa esta función


def gradientes_integrados(grad_f, x, base, pasos=50):
    raise NotImplementedError  # TODO: implementa esta función
