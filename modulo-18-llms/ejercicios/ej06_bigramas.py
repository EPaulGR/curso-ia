"""Ejercicio 6 — Modelo de lenguaje de bigramas y perplejidad.

- `entrenar_bigramas(tokens, vocab_size, suavizado=1.0)`: matriz P (V x V) con
  P[a, b] = (conteo(a,b) + suavizado) / (conteo(a) + suavizado*V).
- `perplejidad(P, tokens)`: exp(-promedio log P[t_i, t_{i+1}]).
- `generar(P, inicio, n, rng)`: lista de n tokens tras `inicio` muestreando de P.
La perplejidad es la métrica base del preentrenamiento (Jurafsky & Martin, cap. 3).
"""
import numpy as np


def entrenar_bigramas(tokens, vocab_size, suavizado=1.0):
    raise NotImplementedError  # TODO: implementa esta función


def perplejidad(P, tokens):
    raise NotImplementedError  # TODO: implementa esta función


def generar(P, inicio, n, rng):
    raise NotImplementedError  # TODO: implementa esta función
