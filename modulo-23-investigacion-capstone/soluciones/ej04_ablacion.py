"""Ejercicio 4 — Diseño de ablaciones y búsqueda de hiperparámetros.

- `rejilla(espacio: dict)`: lista de dicts con todas las combinaciones (orden de claves preservado).
- `busqueda_aleatoria(espacio_dist: dict, n, seed)`: cada valor es una función rng -> valor.
- `ablacion(fn, config_base: dict, componentes: list)`: fn(config) -> métrica. Para cada componente
  evalúa la config con ese componente en False. Devuelve dict {"base": m, componente: m - base, ...}.
"""
import itertools
import numpy as np


def rejilla(espacio):
    claves = list(espacio)
    return [dict(zip(claves, vals)) for vals in itertools.product(*espacio.values())]


def busqueda_aleatoria(espacio_dist, n, seed=0):
    rng = np.random.default_rng(seed)
    return [{k: f(rng) for k, f in espacio_dist.items()} for _ in range(n)]


def ablacion(fn, config_base, componentes):
    base = fn(config_base)
    out = {"base": base}
    for c in componentes:
        out[c] = fn({**config_base, c: False}) - base
    return out
