"""Ejercicio 05 — Monte Carlo Tree Search con UCT (BUAP 3.4 "nuevas técnicas", AIMA 5.4).

Cada iteración: SELECCIÓN (UCB1) → EXPANSIÓN → SIMULACIÓN (playout aleatorio) → RETROPROPAGACIÓN.

    UCB1(n) = Q(n)/N(n) + c * sqrt( ln N(padre) / N(n) ),   c ≈ √2

Q(n) se acumula desde el punto de vista del jugador que hizo la jugada que llevó a n.
Es la base de AlphaGo/AlphaZero (con una red en lugar del playout aleatorio).
"""
import math
import random


class _Nodo:
    def __init__(self, estado, padre=None, accion=None, por=None):
        self.estado, self.padre, self.accion, self.por = estado, padre, accion, por
        self.hijos, self.sin_probar = [], None
        self.N, self.Q = 0, 0.0


def mcts(juego, estado, iteraciones=1000, c=math.sqrt(2), semilla=0):
    """Devuelve la acción de la raíz con más visitas tras `iteraciones`."""
    rng = random.Random(semilla)
    raiz = _Nodo(estado)
    raiz.sin_probar = list(juego.acciones(estado))
    for _ in range(iteraciones):
        n = raiz
        # selección
        while not n.sin_probar and n.hijos:
            n = max(n.hijos, key=lambda h: h.Q / h.N + c * math.sqrt(math.log(n.N) / h.N))
        # expansión
        if n.sin_probar:
            a = n.sin_probar.pop(rng.randrange(len(n.sin_probar)))
            s2 = juego.resultado(n.estado, a)
            h = _Nodo(s2, n, a, juego.jugador(n.estado))
            h.sin_probar = [] if juego.terminal(s2) else list(juego.acciones(s2))
            n.hijos.append(h)
            n = h
        # simulación
        s = n.estado
        while not juego.terminal(s):
            s = juego.resultado(s, rng.choice(juego.acciones(s)))
        # retropropagación
        while n is not None:
            n.N += 1
            if n.por is not None:
                n.Q += (juego.utilidad(s, n.por) + 1) / 2
            n = n.padre
    return max(raiz.hijos, key=lambda h: h.N).accion
