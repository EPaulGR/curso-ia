"""Ejercicio 04 — Grafos como dict nodo -> lista de vecinos."""
from collections import deque


def bfs_orden(g, inicio):
    """Orden de visita BFS (vecinos en el orden de la lista)."""
    vis, q, orden = {inicio}, deque([inicio]), []
    while q:
        u = q.popleft(); orden.append(u)
        for v in g.get(u, []):
            if v not in vis:
                vis.add(v); q.append(v)
    return orden


def dfs_orden(g, inicio):
    """Orden de visita DFS recursivo."""
    vis, orden = set(), []

    def visita(u):
        vis.add(u); orden.append(u)
        for v in g.get(u, []):
            if v not in vis:
                visita(v)
    visita(inicio)
    return orden


def orden_topologico(g):
    """Algoritmo de Kahn; ValueError si hay ciclo. Desempate: nodos con grado 0 en orden de aparición."""
    nodos = list(dict.fromkeys(list(g) + [v for vs in g.values() for v in vs]))
    gin = {u: 0 for u in nodos}
    for vs in g.values():
        for v in vs: gin[v] += 1
    q = deque(u for u in nodos if gin[u] == 0); res = []
    while q:
        u = q.popleft(); res.append(u)
        for v in g.get(u, []):
            gin[v] -= 1
            if gin[v] == 0: q.append(v)
    if len(res) != len(nodos):
        raise ValueError("el grafo tiene ciclo")
    return res


def componentes_conexas(g):
    """Número de componentes conexas de un grafo no dirigido."""
    vis, c = set(), 0
    for u in g:
        if u not in vis:
            c += 1; vis.update(bfs_orden(g, u))
    return c
