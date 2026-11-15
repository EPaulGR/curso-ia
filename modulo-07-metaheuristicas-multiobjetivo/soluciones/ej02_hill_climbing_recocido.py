"""Ejercicio 02 — Búsqueda local: ascenso de colinas y recocido simulado (BUAP 4.2, AIMA 4.1).

Hill climbing (mejor mejora, vecindario 2-opt) con reinicios aleatorios.
Recocido simulado: acepta un vecino peor con probabilidad exp(−Δ/T); T ← α·T.
Las funciones de ej01 se reescriben aquí para que el archivo sea autocontenido.
"""
import math
import random


def _longitud(ruta, D):
    return sum(D[ruta[i]][ruta[(i + 1) % len(ruta)]] for i in range(len(ruta)))


def hill_climbing_tsp(D, reinicios=5, semilla=0):
    """Devuelve (mejor_ruta, longitud). Cada reinicio parte de una permutación aleatoria
    y aplica el mejor movimiento 2-opt mientras mejore."""
    rng = random.Random(semilla)
    n = len(D)
    mejor, mejor_l = None, float("inf")
    for _ in range(reinicios):
        r = list(range(n))
        rng.shuffle(r)
        l = _longitud(r, D)
        while True:
            cand, cand_l = None, l
            for i in range(1, n - 1):
                for j in range(i + 1, n):
                    s = r[:i] + r[i:j + 1][::-1] + r[j + 1:]
                    ls = _longitud(s, D)
                    if ls < cand_l - 1e-12:
                        cand, cand_l = s, ls
            if cand is None:
                break
            r, l = cand, cand_l
        if l < mejor_l:
            mejor, mejor_l = r, l
    return mejor, mejor_l


def recocido_simulado_tsp(D, T0=10.0, alfa=0.995, iteraciones=20000, semilla=0):
    """Devuelve (mejor_ruta, longitud). Vecino = 2-opt aleatorio."""
    rng = random.Random(semilla)
    n = len(D)
    r = list(range(n))
    rng.shuffle(r)
    l = _longitud(r, D)
    mejor, mejor_l, T = r[:], l, T0
    for _ in range(iteraciones):
        i, j = sorted(rng.sample(range(n), 2))
        s = r[:i] + r[i:j + 1][::-1] + r[j + 1:]
        ls = _longitud(s, D)
        d = ls - l
        if d < 0 or rng.random() < math.exp(-d / max(T, 1e-12)):
            r, l = s, ls
            if l < mejor_l:
                mejor, mejor_l = r[:], l
        T *= alfa
    return mejor, mejor_l
