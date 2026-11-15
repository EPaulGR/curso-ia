"""Ejercicio 06 — Algoritmo evolutivo (1+1) sobre OneMax (maximizar número de unos)."""
import random


def onemax(bits):
    """Aptitud: número de unos."""
    return sum(bits)


def mutar(bits, p, rng):
    """Voltea cada bit con probabilidad p."""
    return [b ^ (rng.random() < p) for b in bits]


def uno_mas_uno(n, generaciones=5000, semilla=0):
    """(1+1)-EA: hijo reemplaza al padre si su aptitud es >=. Devuelve (mejor, generacion_en_que_llego_a_n o None)."""
    rng = random.Random(semilla)
    padre = [rng.randint(0, 1) for _ in range(n)]
    for g in range(generaciones):
        if onemax(padre) == n:
            return padre, g
        hijo = mutar(padre, 1 / n, rng)
        if onemax(hijo) >= onemax(padre):
            padre = hijo
    return padre, None
