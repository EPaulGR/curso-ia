"""Ejercicio 04 — Grafos como dict nodo -> lista de vecinos."""
from collections import deque

def bfs_orden(g, inicio):
    """Orden de visita BFS (vecinos en el orden de la lista)."""
    raise NotImplementedError  # TODO

def dfs_orden(g, inicio):
    """Orden de visita DFS recursivo."""
    raise NotImplementedError  # TODO

def orden_topologico(g):
    """Algoritmo de Kahn; ValueError si hay ciclo. Desempate: nodos con grado 0 en orden de aparición."""
    raise NotImplementedError  # TODO

def componentes_conexas(g):
    """Número de componentes conexas de un grafo no dirigido."""
    raise NotImplementedError  # TODO
