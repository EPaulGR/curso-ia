"""Ejercicio 08 — Búsqueda bidireccional BFS (acciones reversibles, costo unitario).
Requiere p.meta conocido. Devuelve (camino, nodos_expandidos)."""
from collections import deque


def bidireccional(p):
    """Alterna una capa completa desde cada lado; al encontrar intersección arma el camino."""
    if p.inicial == p.meta:
        return [p.inicial], 0
    pa, pb = {p.inicial: None}, {p.meta: None}
    qa, qb = deque([p.inicial]), deque([p.meta]); exp = 0

    def expandir(q, padres, otros):
        nonlocal exp
        for _ in range(len(q)):
            s = q.popleft(); exp += 1
            for a in p.acciones(s):
                h = p.resultado(s, a)
                if h not in padres:
                    padres[h] = s
                    if h in otros:
                        return h
                    q.append(h)
        return None

    while qa and qb:
        x = expandir(qa, pa, pb) if len(qa) <= len(qb) else expandir(qb, pb, pa)
        if x is not None:
            ida, s = [], x
            while s is not None:
                ida.append(s); s = pa[s]
            vuelta, s = [], pb[x]
            while s is not None:
                vuelta.append(s); s = pb[s]
            return ida[::-1] + vuelta, exp
    return None, exp
