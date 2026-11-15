"""Ejercicio 4 — Monitoreo de deriva de datos (data drift).

- `psi(referencia, actual, bins=10)`: Population Stability Index. Bordes por cuantiles de la
  referencia (np.quantile, extremos -inf/inf); proporciones con mínimo 1e-6;
  PSI = sum (a - r) * ln(a / r).
- `ks_estadistico(a, b)`: máximo |F_a(x) - F_b(x)| sobre todos los valores observados.
- `alerta(psi_valor)`: "estable" < 0.1 <= "moderado" < 0.25 <= "severo".
"""
import numpy as np


def psi(referencia, actual, bins=10):
    bordes = np.quantile(referencia, np.linspace(0, 1, bins + 1))
    bordes[0], bordes[-1] = -np.inf, np.inf
    r = np.histogram(referencia, bordes)[0] / len(referencia)
    a = np.histogram(actual, bordes)[0] / len(actual)
    r, a = np.maximum(r, 1e-6), np.maximum(a, 1e-6)
    return float(np.sum((a - r) * np.log(a / r)))


def ks_estadistico(a, b):
    a, b = np.sort(a), np.sort(b)
    x = np.concatenate([a, b])
    Fa = np.searchsorted(a, x, side="right") / len(a)
    Fb = np.searchsorted(b, x, side="right") / len(b)
    return float(np.max(np.abs(Fa - Fb)))


def alerta(psi_valor):
    if psi_valor < 0.1:
        return "estable"
    return "moderado" if psi_valor < 0.25 else "severo"
