"""Ejercicio 4 — Diseño de ablaciones y búsqueda de hiperparámetros.

- `rejilla(espacio: dict)`: lista de dicts con todas las combinaciones (orden de claves preservado).
- `busqueda_aleatoria(espacio_dist: dict, n, seed)`: cada valor es una función rng -> valor.
- `ablacion(fn, config_base: dict, componentes: list)`: fn(config) -> métrica. Para cada componente
  evalúa la config con ese componente en False. Devuelve dict {"base": m, componente: m - base, ...}.
"""
import itertools
import numpy as np


def rejilla(espacio):
    raise NotImplementedError  # TODO: implementa esta función


def busqueda_aleatoria(espacio_dist, n, seed=0):
    raise NotImplementedError  # TODO: implementa esta función


def ablacion(fn, config_base, componentes):
    raise NotImplementedError  # TODO: implementa esta función
