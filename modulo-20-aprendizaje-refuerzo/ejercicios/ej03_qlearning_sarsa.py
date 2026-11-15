"""Ejercicio 3 — Q-learning y SARSA tabulares.

Entorno: clase `EntornoMDP(P, inicio, rng)` con `reset() -> s` y `step(a) -> (s2, r, terminal)`
(ya implementada abajo, no la modifiques).
- `epsilon_greedy(Q, s, eps, rng)`.
- `q_learning(env, n_estados, n_acciones, episodios, alpha, gamma, eps, rng, max_pasos=100)`:
  objetivo off-policy r + gamma * max_a Q(s2, a). Devuelve Q.
- `sarsa(...)` misma firma: objetivo on-policy r + gamma * Q(s2, a2).
Referencia: Sutton & Barto cap. 6.
"""
import numpy as np


class EntornoMDP:

    def __init__(self, P, inicio, rng):
        self.P, self.inicio, self.rng = P, inicio, rng

    def reset(self):
        self.s = self.inicio
        return self.s

    def step(self, a):
        trans = self.P[self.s][a]
        i = self.rng.choice(len(trans), p=[t[0] for t in trans])
        _, s2, r, term = trans[i]
        self.s = s2
        return s2, r, term


def epsilon_greedy(Q, s, eps, rng):
    raise NotImplementedError  # TODO: implementa esta función


def q_learning(env, n_estados, n_acciones, episodios, alpha, gamma, eps, rng, max_pasos=100):
    raise NotImplementedError  # TODO: implementa esta función


def sarsa(env, n_estados, n_acciones, episodios, alpha, gamma, eps, rng, max_pasos=100):
    raise NotImplementedError  # TODO: implementa esta función
