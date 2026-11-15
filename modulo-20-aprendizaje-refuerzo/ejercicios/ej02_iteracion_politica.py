"""Ejercicio 2 — Iteración de política.

Usa el formato de MDP del ejercicio 1.
- `evaluar_politica(P, pol, gamma, tol=1e-10)`: V^pi iterativo.
- `iteracion_politica(P, gamma)`: parte de pol = 0 en todos los estados; alterna evaluación y mejora
  hasta que la política no cambie. Devuelve (V, pol, n_iteraciones).
"""
import numpy as np


def _q(P, V, s, a, gamma):
    return sum(p * (r + (0 if t else gamma * V[s2])) for p, s2, r, t in P[s][a])


def evaluar_politica(P, pol, gamma=0.99, tol=1e-10):
    raise NotImplementedError  # TODO: implementa esta función


def iteracion_politica(P, gamma=0.99):
    raise NotImplementedError  # TODO: implementa esta función
