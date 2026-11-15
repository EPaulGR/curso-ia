"""Ejercicio 4 — Monitoreo de deriva de datos (data drift).

- `psi(referencia, actual, bins=10)`: Population Stability Index. Bordes por cuantiles de la
  referencia (np.quantile, extremos -inf/inf); proporciones con mínimo 1e-6;
  PSI = sum (a - r) * ln(a / r).
- `ks_estadistico(a, b)`: máximo |F_a(x) - F_b(x)| sobre todos los valores observados.
- `alerta(psi_valor)`: "estable" < 0.1 <= "moderado" < 0.25 <= "severo".
"""
import numpy as np


def psi(referencia, actual, bins=10):
    raise NotImplementedError  # TODO: implementa esta función


def ks_estadistico(a, b):
    raise NotImplementedError  # TODO: implementa esta función


def alerta(psi_valor):
    raise NotImplementedError  # TODO: implementa esta función
