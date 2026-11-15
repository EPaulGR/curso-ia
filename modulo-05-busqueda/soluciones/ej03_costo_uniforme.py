"""Ejercicio 03 — Búsqueda de costo uniforme. Devuelve (camino, costo, nodos_expandidos)."""
import heapq
import itertools


def ucs(p):
    """UCS en grafo: prueba de meta al extraer de la frontera."""
    cont = itertools.count()
    frontera = [(0, next(cont), p.inicial)]; g = {p.inicial: 0}; padres = {p.inicial: None}; exp = 0
    while frontera:
        c, _, s = heapq.heappop(frontera)
        if c > g[s]:
            continue
        if p.es_meta(s):
            cam = []
            while s is not None:
                cam.append(s); s = padres[s]
            return cam[::-1], c, exp
        exp += 1
        for a in p.acciones(s):
            h = p.resultado(s, a); nc = c + p.costo(s, a, h)
            if nc < g.get(h, float("inf")):
                g[h] = nc; padres[h] = s; heapq.heappush(frontera, (nc, next(cont), h))
    return None, float("inf"), exp
