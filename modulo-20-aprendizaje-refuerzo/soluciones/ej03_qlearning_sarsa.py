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
    if rng.random() < eps:
        return int(rng.integers(Q.shape[1]))
    return int(np.argmax(Q[s]))


def q_learning(env, n_estados, n_acciones, episodios, alpha, gamma, eps, rng, max_pasos=100):
    Q = np.zeros((n_estados, n_acciones))
    for _ in range(episodios):
        s = env.reset()
        for _ in range(max_pasos):
            a = epsilon_greedy(Q, s, eps, rng)
            s2, r, t = env.step(a)
            obj = r if t else r + gamma * Q[s2].max()
            Q[s, a] += alpha * (obj - Q[s, a])
            s = s2
            if t:
                break
    return Q


def sarsa(env, n_estados, n_acciones, episodios, alpha, gamma, eps, rng, max_pasos=100):
    Q = np.zeros((n_estados, n_acciones))
    for _ in range(episodios):
        s = env.reset()
        a = epsilon_greedy(Q, s, eps, rng)
        for _ in range(max_pasos):
            s2, r, t = env.step(a)
            a2 = epsilon_greedy(Q, s2, eps, rng)
            obj = r if t else r + gamma * Q[s2, a2]
            Q[s, a] += alpha * (obj - Q[s, a])
            s, a = s2, a2
            if t:
                break
    return Q
