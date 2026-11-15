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
        raise NotImplementedError  # TODO: implementa esta función

    def muestrear(self, n):
        raise NotImplementedError  # TODO: implementa esta función

    def __len__(self):
        return len(self.datos)


def objetivos_dqn(R, Q_sig, T, gamma):
    raise NotImplementedError  # TODO: implementa esta función


def objetivos_double_dqn(R, Q_sig_online, Q_sig_target, T, gamma):
    raise NotImplementedError  # TODO: implementa esta función


def actualizacion_suave(target, online, tau):
    raise NotImplementedError  # TODO: implementa esta función
