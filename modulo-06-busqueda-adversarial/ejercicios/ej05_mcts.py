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
    raise NotImplementedError  # TODO: implementa esta función
