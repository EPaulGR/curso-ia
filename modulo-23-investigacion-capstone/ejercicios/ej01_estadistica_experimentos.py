"""Ejercicio 1 — Rigor estadístico al comparar modelos.

- `intervalo_bootstrap(valores, n=2000, alpha=0.05, seed=0)`: IC percentil de la media.
- `prueba_permutacion(a, b, n=5000, seed=0)`: p-valor bilateral de la diferencia de medias
  (|media(a)-media(b)| permutando etiquetas; p = (conteo_extremos + 1) / (n + 1)).
- `mcnemar(pred_a, pred_b, y)`: estadístico chi² con corrección de continuidad
  (|b01 - b10| - 1)^2 / (b01 + b10), donde b01 = A acierta y B falla, b10 al revés. 0 si no hay discordantes.
- `bonferroni(pvalores, alpha=0.05)`: lista de bool (rechaza H0).
"""
import numpy as np


def intervalo_bootstrap(valores, n=2000, alpha=0.05, seed=0):
    raise NotImplementedError  # TODO: implementa esta función


def prueba_permutacion(a, b, n=5000, seed=0):
    raise NotImplementedError  # TODO: implementa esta función


def mcnemar(pred_a, pred_b, y):
    raise NotImplementedError  # TODO: implementa esta función


def bonferroni(pvalores, alpha=0.05):
    raise NotImplementedError  # TODO: implementa esta función
