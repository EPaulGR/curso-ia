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
    raise NotImplementedError  # TODO: implementa esta función


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
    raise NotImplementedError  # TODO: implementa esta función
