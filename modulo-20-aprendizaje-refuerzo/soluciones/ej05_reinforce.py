"""Ejercicio 5 — REINFORCE (gradiente de política) en un bandido contextual / MDP simple.

Política softmax lineal: pi(a|s) = softmax(theta[s]) con theta (n_estados x n_acciones).
- `retornos(recompensas, gamma)`: G_t = sum_k gamma^k r_{t+k}.
- `grad_log_softmax(theta_s, a)`: gradiente de log pi(a|s) respecto a theta[s] = onehot(a) - pi.
- `reinforce_bandido(recompensas_medias, episodios, lr, rng, baseline=True)`: bandido de 1 estado;
  cada episodio: muestrea a, recibe r ~ N(recompensas_medias[a], 1), actualiza
  theta += lr * (r - b) * grad, con b = promedio móvil de r si baseline. Devuelve theta (1-D).
Sutton & Barto cap. 13; Williams 1992.
"""
import numpy as np


def _softmax(z):
    e = np.exp(z - z.max())
    return e / e.sum()


def retornos(recompensas, gamma):
    G, out = 0.0, []
    for r in reversed(recompensas):
        G = r + gamma * G
        out.append(G)
    return np.array(out[::-1])


def grad_log_softmax(theta_s, a):
    g = -_softmax(theta_s)
    g[a] += 1
    return g


def reinforce_bandido(recompensas_medias, episodios, lr, rng, baseline=True):
    theta = np.zeros(len(recompensas_medias))
    b = 0.0
    for n in range(1, episodios + 1):
        a = rng.choice(len(theta), p=_softmax(theta))
        r = rng.normal(recompensas_medias[a], 1)
        ventaja = r - b if baseline else r
        theta += lr * ventaja * grad_log_softmax(theta, a)
        b += (r - b) / n
    return theta
