"""Ejercicio 1 — MDP de cuadrícula (GridWorld) e iteración de valor.

Un MDP se representa con P: dict estado -> dict accion -> lista de (prob, sig_estado, recompensa, terminal).
- `crear_gridworld(filas, cols, meta, trampas, paso=-0.04, deslizamiento=0.0)`:
  estados 0..filas*cols-1 (fila-mayor), acciones 0=arriba 1=derecha 2=abajo 3=izquierda.
  Moverse contra el borde deja en el mismo estado. Llegar a la meta da +1 (terminal);
  a una trampa -1 (terminal); otro movimiento `paso`. Con prob `deslizamiento` la acción
  se desvía a cada perpendicular (deslizamiento/2 cada una). Estados terminales: sin transiciones
  (dict de acciones con [(1.0, s, 0, True)]).
- `iteracion_valor(P, gamma, tol=1e-8)`: devuelve (V np.ndarray, politica np.ndarray de acciones).
"""
import numpy as np


def crear_gridworld(filas, cols, meta, trampas, paso=-0.04, deslizamiento=0.0):
    raise NotImplementedError  # TODO: implementa esta función


def _q(P, V, s, a, gamma):
    return sum(p * (r + (0 if t else gamma * V[s2])) for p, s2, r, t in P[s][a])


def iteracion_valor(P, gamma=0.99, tol=1e-8):
    raise NotImplementedError  # TODO: implementa esta función
