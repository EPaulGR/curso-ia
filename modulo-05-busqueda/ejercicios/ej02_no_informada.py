"""Ejercicio 02 — Búsqueda no informada.
Cada función devuelve (camino_de_estados, nodos_expandidos) o (None, nodos_expandidos) si no hay solución.
camino_de_estados incluye el estado inicial y el final."""
from collections import deque

def _camino(padres, s):
    c = []
    while s is not None:
        c.append(s)
        s = padres[s]
    return c[::-1]

def bfs(p):
    """Búsqueda en anchura (en grafo) con prueba de meta al generar."""
    raise NotImplementedError  # TODO

def dfs(p, max_nodos=100000):
    """Búsqueda en profundidad (en grafo, pila explícita). Detente tras max_nodos expansiones."""
    raise NotImplementedError  # TODO

def dls(p, limite):
    """Profundidad limitada recursiva (evita ciclos en el camino actual).
Devuelve (camino | 'corte' | None, nodos_expandidos)."""
    raise NotImplementedError  # TODO

def iddfs(p, max_prof=50):
    """Profundización iterativa: nodos_expandidos es la suma de todas las iteraciones."""
    raise NotImplementedError  # TODO
