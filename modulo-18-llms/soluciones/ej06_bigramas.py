"""Ejercicio 6 — Modelo de lenguaje de bigramas y perplejidad.

- `entrenar_bigramas(tokens, vocab_size, suavizado=1.0)`: matriz P (V x V) con
  P[a, b] = (conteo(a,b) + suavizado) / (conteo(a) + suavizado*V).
- `perplejidad(P, tokens)`: exp(-promedio log P[t_i, t_{i+1}]).
- `generar(P, inicio, n, rng)`: lista de n tokens tras `inicio` muestreando de P.
La perplejidad es la métrica base del preentrenamiento (Jurafsky & Martin, cap. 3).
"""
import numpy as np


def entrenar_bigramas(tokens, vocab_size, suavizado=1.0):
    C = np.full((vocab_size, vocab_size), suavizado)
    for a, b in zip(tokens, tokens[1:]):
        C[a, b] += 1
    return C / C.sum(1, keepdims=True)


def perplejidad(P, tokens):
    lp = [np.log(P[a, b]) for a, b in zip(tokens, tokens[1:])]
    return float(np.exp(-np.mean(lp)))


def generar(P, inicio, n, rng):
    out, t = [], inicio
    for _ in range(n):
        t = int(rng.choice(P.shape[1], p=P[t]))
        out.append(t)
    return out
