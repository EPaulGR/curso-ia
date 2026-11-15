"""Ejercicio 07 — Algoritmo memético (BUAP 4.5; Moscato 1989; Eiben & Smith cap. 10).

Memético = algoritmo evolutivo + búsqueda local aplicada a cada descendiente
(evolución lamarckiana: el individuo mejorado reemplaza al original).
Para TSP: AG con cruce OX + mutación por intercambio + 2-opt de primera mejora.
"""
import random


def _longitud(r, D):
    return sum(D[r[i]][r[(i + 1) % len(r)]] for i in range(len(r)))


def dos_opt_local(ruta, D):
    """Aplica 2-opt de primera mejora hasta óptimo local. Devuelve nueva ruta."""
    r, n = ruta[:], len(ruta)
    mejora = True
    while mejora:
        mejora = False
        for i in range(n - 1):
            for j in range(i + 2, n if i > 0 else n - 1):
                a, b, c, d = r[i], r[i + 1], r[j], r[(j + 1) % n]
                if D[a][c] + D[b][d] < D[a][b] + D[c][d] - 1e-12:
                    r[i + 1:j + 1] = r[i + 1:j + 1][::-1]
                    mejora = True
    return r


def _ox(p1, p2, rng):
    n = len(p1)
    i, j = sorted(rng.sample(range(n), 2))
    h = [None] * n
    h[i:j + 1] = p1[i:j + 1]
    resto = [g for g in p2 if g not in set(h[i:j + 1])]
    for k, pos in enumerate(list(range(j + 1, n)) + list(range(i))):
        h[pos] = resto[k]
    return h


def memetico_tsp(D, tam_pob=20, generaciones=30, p_mut=0.2, semilla=0):
    """Devuelve (mejor_ruta, longitud)."""
    rng = random.Random(semilla)
    n = len(D)
    pob = []
    for _ in range(tam_pob):
        r = list(range(n))
        rng.shuffle(r)
        pob.append(dos_opt_local(r, D))
    for _ in range(generaciones):
        hijos = []
        for _ in range(tam_pob):
            a, b = rng.sample(pob, 2)
            h = _ox(a, b, rng)
            if rng.random() < p_mut:
                i, j = rng.sample(range(n), 2)
                h[i], h[j] = h[j], h[i]
            hijos.append(dos_opt_local(h, D))
        pob = sorted(pob + hijos, key=lambda r: _longitud(r, D))[:tam_pob]
    return pob[0], _longitud(pob[0], D)
