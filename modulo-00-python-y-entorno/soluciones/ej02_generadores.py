"""Ejercicio 02 — Generadores e itertools."""
import itertools


def fibonacci():
    """Generador infinito de Fibonacci: 0, 1, 1, 2, 3, 5..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primeros(gen, n: int) -> list:
    """Toma los primeros n elementos de un generador."""
    return list(itertools.islice(gen, n))


def lotes(seq, n: int):
    """Generador de lotes (listas) de tamaño n; el último puede ser más corto."""
    for i in range(0, len(seq), n):
        yield list(seq[i:i + n])


def todas_asignaciones(variables: list, dominio: list):
    """Generador de dicts con todas las asignaciones posibles variable->valor (producto cartesiano)."""
    for combo in itertools.product(dominio, repeat=len(variables)):
        yield dict(zip(variables, combo))
