"""Ejercicio 05 — Búsqueda primero el mejor: voraz, A* y weighted A*.
Todas devuelven (camino, costo, nodos_expandidos)."""
import heapq
import itertools


def primero_mejor(p, f):
    """Best-first genérico; f(estado, g) -> prioridad. Prueba de meta al extraer."""
    cont = itertools.count()
    frontera = [(f(p.inicial, 0), next(cont), p.inicial)]
    g = {p.inicial: 0}; padres = {p.inicial: None}; cerrados = set(); exp = 0
    while frontera:
        _, _, s = heapq.heappop(frontera)
        if s in cerrados:
            continue
        if p.es_meta(s):
            cam, x = [], s
            while x is not None:
                cam.append(x); x = padres[x]
            return cam[::-1], g[s], exp
        cerrados.add(s); exp += 1
        for a in p.acciones(s):
            h = p.resultado(s, a); ng = g[s] + p.costo(s, a, h)
            if h not in cerrados and ng < g.get(h, float("inf")):
                g[h] = ng; padres[h] = s; heapq.heappush(frontera, (f(h, ng), next(cont), h))
    return None, float("inf"), exp


def voraz(p, h):
    """Primero el mejor voraz: f = h."""
    return primero_mejor(p, lambda s, g: h(s))


def a_estrella(p, h):
    """A*: f = g + h."""
    return primero_mejor(p, lambda s, g: g + h(s))


def a_estrella_ponderado(p, h, w=2.0):
    """Weighted A*: f = g + w*h."""
    return primero_mejor(p, lambda s, g: g + w * h(s))
