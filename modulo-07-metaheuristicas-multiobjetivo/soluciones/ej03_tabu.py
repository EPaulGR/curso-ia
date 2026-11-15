"""Ejercicio 03 — Búsqueda tabú para la mochila 0/1 (BUAP 4.3; Glover 1986).

Vecindario: (a) invertir un bit, (b) intercambio: sacar un objeto i y meter un objeto j.
Lista tabú: los bits modificados quedan prohibidos `tenencia` iteraciones. Criterio de aspiración: un movimiento tabú se permite si produce una
solución mejor que la mejor encontrada. Se toma SIEMPRE el mejor vecino no tabú
(aunque empeore) — eso permite escapar de óptimos locales.
"""
import random


def _valor(x, pesos, valores, cap):
    p = sum(w for w, b in zip(pesos, x) if b)
    v = sum(val for val, b in zip(valores, x) if b)
    return v if p <= cap else v - 10 * max(valores) * (p - cap)


def busqueda_tabu_mochila(pesos, valores, capacidad, iteraciones=200, tenencia=3, semilla=0):
    """Devuelve (mejor_x, mejor_valor) con x lista de 0/1."""
    rng = random.Random(semilla)
    n = len(pesos)
    x = [0] * n
    mejor, mejor_v = x[:], _valor(x, pesos, valores, capacidad)
    tabu = {}
    for it in range(iteraciones):
        cand, cand_v, cand_mov = None, float("-inf"), None
        movs = [(i,) for i in range(n)]
        movs += [(i, j) for i in range(n) if x[i] for j in range(n) if not x[j]]
        rng.shuffle(movs)
        for mov in movs:
            y = x[:]
            for i in mov:
                y[i] ^= 1
            v = _valor(y, pesos, valores, capacidad)
            es_tabu = any(tabu.get(i, -1) > it for i in mov)
            if (not es_tabu or v > mejor_v) and v > cand_v:
                cand, cand_v, cand_mov = y, v, mov
        if cand is None:
            continue
        x = cand
        for i in cand_mov:
            tabu[i] = it + tenencia
        if cand_v > mejor_v:
            mejor, mejor_v = x[:], cand_v
    return mejor, mejor_v
