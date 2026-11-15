"""Ejercicio 06 — Planificación clásica con STRIPS (AIMA cap. 11).

Estado = frozenset de hechos (cadenas). Una acción tiene precondiciones, lista de
agregados y lista de borrados:
    aplicable(s, a)  ⇔  pre(a) ⊆ s
    resultado(s, a)  =  (s − borrar(a)) ∪ agregar(a)
Meta = conjunto de hechos que deben ser ciertos.

Implementa:
- planificar_bfs: búsqueda hacia adelante en anchura (plan más corto).
- h_ignorar_borrados: heurística = nº de pasos del plan relajado (ignorando listas de
  borrado) calculado en capas: cuántas capas hacen falta para alcanzar la meta.
- planificar_astar con esa heurística.
- acciones_bloques: genera las acciones del mundo de bloques.
"""
import heapq
from collections import deque, namedtuple

Accion = namedtuple("Accion", "nombre pre agregar borrar")


def aplicable(s, a):
    """True si las precondiciones de a están en s."""
    raise NotImplementedError  # TODO: implementa esta función


def resultado(s, a):
    """Estado sucesor."""
    raise NotImplementedError  # TODO: implementa esta función


def planificar_bfs(inicial, meta, acciones):
    """Lista de nombres de acciones del plan más corto, o None."""
    raise NotImplementedError  # TODO: implementa esta función


def h_ignorar_borrados(s, meta, acciones):
    """Número de capas de expansión relajada hasta cubrir la meta (inf si imposible)."""
    raise NotImplementedError  # TODO: implementa esta función


def planificar_astar(inicial, meta, acciones):
    """A* con h_ignorar_borrados (costo 1 por acción). Devuelve (plan, nodos_expandidos)."""
    raise NotImplementedError  # TODO: implementa esta función


def acciones_bloques(bloques):
    """Acciones del mundo de bloques con hechos 'sobre(x,y)', 'sobre(x,mesa)', 'libre(x)':
    mover(x, desde, hacia) para x bloque, desde/hacia ∈ bloques ∪ {'mesa'}, todos distintos.
    pre = {sobre(x,desde), libre(x)} ∪ {libre(hacia) si hacia ≠ mesa}
    agregar = {sobre(x,hacia)} ∪ {libre(desde) si desde ≠ mesa}
    borrar = {sobre(x,desde)} ∪ {libre(hacia) si hacia ≠ mesa}"""
    raise NotImplementedError  # TODO: implementa esta función
