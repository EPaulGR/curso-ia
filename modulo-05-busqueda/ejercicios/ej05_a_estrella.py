"""Ejercicio 05 — Búsqueda primero el mejor: voraz, A* y weighted A*.
Todas devuelven (camino, costo, nodos_expandidos)."""
import heapq
import itertools

def primero_mejor(p, f):
    """Best-first genérico; f(estado, g) -> prioridad. Prueba de meta al extraer."""
    raise NotImplementedError  # TODO

def voraz(p, h):
    """Primero el mejor voraz: f = h."""
    raise NotImplementedError  # TODO

def a_estrella(p, h):
    """A*: f = g + h."""
    raise NotImplementedError  # TODO

def a_estrella_ponderado(p, h, w=2.0):
    """Weighted A*: f = g + w*h."""
    raise NotImplementedError  # TODO
