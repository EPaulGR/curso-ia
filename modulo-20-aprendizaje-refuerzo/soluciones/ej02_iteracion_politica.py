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
    V = np.zeros(len(P))
    while True:
        delta = 0
        for s in range(len(P)):
            v = _q(P, V, s, pol[s], gamma)
            delta = max(delta, abs(v - V[s]))
            V[s] = v
        if delta < tol:
            return V


def iteracion_politica(P, gamma=0.99):
    pol = np.zeros(len(P), int)
    it = 0
    while True:
        it += 1
        V = evaluar_politica(P, pol, gamma)
        nueva = pol.copy()
        for s in range(len(P)):
            qs = [_q(P, V, s, a, gamma) for a in P[s]]
            if qs[pol[s]] < max(qs) - 1e-12:
                nueva[s] = int(np.argmax(qs))
        if np.array_equal(nueva, pol):
            return V, pol, it
        pol = nueva
