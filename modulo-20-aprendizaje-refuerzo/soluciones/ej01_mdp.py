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
    mov = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def destino(s, a):
        f, c = divmod(s, cols)
        nf, nc = f + mov[a][0], c + mov[a][1]
        return nf * cols + nc if 0 <= nf < filas and 0 <= nc < cols else s
    P = {}
    for s in range(filas * cols):
        P[s] = {}
        for a in range(4):
            if s == meta or s in trampas:
                P[s][a] = [(1.0, s, 0.0, True)]
                continue
            opciones = [(1 - deslizamiento, a)]
            if deslizamiento:
                opciones += [(deslizamiento / 2, (a + 1) % 4), (deslizamiento / 2, (a + 3) % 4)]
            trans = []
            for p, b in opciones:
                s2 = destino(s, b)
                if s2 == meta:
                    trans.append((p, s2, 1.0, True))
                elif s2 in trampas:
                    trans.append((p, s2, -1.0, True))
                else:
                    trans.append((p, s2, paso, False))
            P[s][a] = trans
    return P


def _q(P, V, s, a, gamma):
    return sum(p * (r + (0 if t else gamma * V[s2])) for p, s2, r, t in P[s][a])


def iteracion_valor(P, gamma=0.99, tol=1e-8):
    n = len(P)
    V = np.zeros(n)
    while True:
        delta = 0
        for s in range(n):
            v = max(_q(P, V, s, a, gamma) for a in P[s])
            delta = max(delta, abs(v - V[s]))
            V[s] = v
        if delta < tol:
            break
    pol = np.array([max(P[s], key=lambda a: _q(P, V, s, a, gamma)) for s in range(n)])
    return V, pol
