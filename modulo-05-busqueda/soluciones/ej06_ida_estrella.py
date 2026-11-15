"""Ejercicio 06 — IDA*. Devuelve (camino, costo, nodos_expandidos)."""
import math


def ida_estrella(p, h, max_iter=100):
    """IDA* con detección de ciclos en el camino actual."""
    exp = 0
    camino = [p.inicial]; en_camino = {p.inicial}

    def buscar(g, umbral):
        nonlocal exp
        s = camino[-1]; f = g + h(s)
        if f > umbral:
            return f
        if p.es_meta(s):
            return True
        exp += 1; minimo = math.inf
        for a in p.acciones(s):
            hijo = p.resultado(s, a)
            if hijo in en_camino:
                continue
            camino.append(hijo); en_camino.add(hijo)
            t = buscar(g + p.costo(s, a, hijo), umbral)
            if t is True:
                return True
            minimo = min(minimo, t)
            camino.pop(); en_camino.remove(hijo)
        return minimo

    umbral = h(p.inicial)
    for _ in range(max_iter):
        t = buscar(0, umbral)
        if t is True:
            costo = sum(p.costo(a, b, b) for a, b in zip(camino, camino[1:]))
            return list(camino), costo, exp
        if t == math.inf:
            return None, math.inf, exp
        umbral = t
    return None, math.inf, exp
