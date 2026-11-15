"""Ejercicio 09 — Comparativa experimental y factor de ramificación efectivo."""
import random


def factor_ramificacion_efectivo(N, d, tol=1e-6):
    """b* tal que N + 1 = 1 + b* + b*^2 + ... + b*^d, por bisección."""
    if d == 0:
        return 0.0
    total = lambda b: sum(b ** i for i in range(d + 1))
    lo, hi = 0.0, float(max(N, 2))
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if total(mid) < N + 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def estado_aleatorio(problema_cls, pasos, semilla=0):
    """Genera un 8-puzzle a `pasos` movimientos aleatorios de la meta (siempre resoluble)."""
    rng = random.Random(semilla); p = problema_cls(tuple(range(1, 9)) + (0,)); s = p.meta
    for _ in range(pasos):
        s = p.resultado(s, rng.choice(p.acciones(s)))
    return s
