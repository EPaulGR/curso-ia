"""Ejercicio 02 — Búsqueda no informada.
Cada función devuelve (camino_de_estados, nodos_expandidos) o (None, nodos_expandidos) si no hay solución.
camino_de_estados incluye el estado inicial y el final."""
from collections import deque


def _camino(padres, s):
    c = []
    while s is not None:
        c.append(s); s = padres[s]
    return c[::-1]


def bfs(p):
    """Búsqueda en anchura (en grafo) con prueba de meta al generar."""
    if p.es_meta(p.inicial):
        return [p.inicial], 0
    padres = {p.inicial: None}; q = deque([p.inicial]); exp = 0
    while q:
        s = q.popleft(); exp += 1
        for a in p.acciones(s):
            h = p.resultado(s, a)
            if h not in padres:
                padres[h] = s
                if p.es_meta(h):
                    return _camino(padres, h), exp
                q.append(h)
    return None, exp


def dfs(p, max_nodos=100000):
    """Búsqueda en profundidad (en grafo, pila explícita). Detente tras max_nodos expansiones."""
    padres = {p.inicial: None}; pila = [p.inicial]; exp = 0
    while pila and exp < max_nodos:
        s = pila.pop()
        if p.es_meta(s):
            return _camino(padres, s), exp
        exp += 1
        for a in reversed(p.acciones(s)):
            h = p.resultado(s, a)
            if h not in padres:
                padres[h] = s; pila.append(h)
    return None, exp


def dls(p, limite):
    """Profundidad limitada recursiva (evita ciclos en el camino actual).
    Devuelve (camino | 'corte' | None, nodos_expandidos)."""
    exp = 0

    def rec(s, camino, l):
        nonlocal exp
        if p.es_meta(s):
            return camino
        if l == 0:
            return "corte"
        exp += 1; hubo_corte = False
        for a in p.acciones(s):
            h = p.resultado(s, a)
            if h in camino:
                continue
            r = rec(h, camino + [h], l - 1)
            if r == "corte":
                hubo_corte = True
            elif r is not None:
                return r
        return "corte" if hubo_corte else None
    return rec(p.inicial, [p.inicial], limite), exp


def iddfs(p, max_prof=50):
    """Profundización iterativa: nodos_expandidos es la suma de todas las iteraciones."""
    total = 0
    for l in range(max_prof + 1):
        r, e = dls(p, l); total += e
        if r != "corte":
            return r, total
    return None, total
