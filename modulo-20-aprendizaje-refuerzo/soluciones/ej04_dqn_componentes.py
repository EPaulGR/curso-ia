"""Ejercicio 4 — Componentes de DQN (sin depender de PyTorch).

- Clase `BufferRepeticion(capacidad, seed)`: `agregar(s, a, r, s2, terminal)` (circular),
  `muestrear(n)` -> tupla de arrays (S, A, R, S2, T), `__len__`.
- `objetivos_dqn(R, Q_sig, T, gamma)`: y = R + gamma * (1-T) * max Q_sig.
- `objetivos_double_dqn(R, Q_sig_online, Q_sig_target, T, gamma)`: acción elegida con la red
  online y evaluada con la target.
- `actualizacion_suave(target, online, tau)`: dict de arrays; target <- tau*online + (1-tau)*target.
Mnih et al. 2015 (Nature), van Hasselt 2016 (Double DQN).
Reto: arma el DQN completo en PyTorch (MPS) con gymnasium CartPole-v1.
"""
import numpy as np


class BufferRepeticion:

    def __init__(self, capacidad, seed=0):
        self.cap, self.datos, self.pos = capacidad, [], 0
        self.rng = np.random.default_rng(seed)

    def agregar(self, s, a, r, s2, terminal):
        t = (s, a, r, s2, terminal)
        if len(self.datos) < self.cap:
            self.datos.append(t)
        else:
            self.datos[self.pos] = t
        self.pos = (self.pos + 1) % self.cap

    def muestrear(self, n):
        idx = self.rng.choice(len(self.datos), n, replace=False)
        cols = zip(*[self.datos[i] for i in idx])
        return tuple(np.array(c) for c in cols)

    def __len__(self):
        return len(self.datos)


def objetivos_dqn(R, Q_sig, T, gamma):
    return R + gamma * (1 - T) * Q_sig.max(1)


def objetivos_double_dqn(R, Q_sig_online, Q_sig_target, T, gamma):
    a = Q_sig_online.argmax(1)
    return R + gamma * (1 - T) * Q_sig_target[np.arange(len(a)), a]


def actualizacion_suave(target, online, tau):
    return {k: tau * online[k] + (1 - tau) * target[k] for k in target}
