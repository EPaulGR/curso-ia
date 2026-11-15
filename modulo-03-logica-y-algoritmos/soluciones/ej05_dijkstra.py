"""Ejercicio 05 — Dijkstra. Grafo: dict u -> lista de (v, peso)."""
import heapq


def dijkstra(g, s):
    """Devuelve (dist, padre) desde s."""
    dist, padre, pq = {s: 0}, {s: None}, [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v], padre[v] = nd, u; heapq.heappush(pq, (nd, v))
    return dist, padre


def camino(padre, t):
    """Reconstruye el camino hasta t (lista desde el origen)."""
    c = []
    while t is not None:
        c.append(t); t = padre[t]
    return c[::-1]
