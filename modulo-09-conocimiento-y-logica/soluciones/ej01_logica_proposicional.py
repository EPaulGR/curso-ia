"""Ejercicio 01 — Lógica proposicional: semántica y verificación de modelos (AIMA 7.4).

Fórmulas como tuplas anidadas:
    'p'                 átomo
    ('no', A)           ¬A
    ('y', A, B)         A ∧ B
    ('o', A, B)         A ∨ B
    ('implica', A, B)   A ⇒ B
    ('sii', A, B)       A ⇔ B
KB ⊨ α  ⇔  α es verdadera en todo modelo donde KB es verdadera (TT-ENTAILS).
"""
from itertools import product


def evaluar(f, modelo):
    """Valor de verdad de f en `modelo` (dict átomo → bool)."""
    if isinstance(f, str):
        return modelo[f]
    op = f[0]
    if op == "no":
        return not evaluar(f[1], modelo)
    a, b = evaluar(f[1], modelo), evaluar(f[2], modelo)
    return {"y": a and b, "o": a or b, "implica": (not a) or b, "sii": a == b}[op]


def simbolos(f):
    """Conjunto de átomos que aparecen en f."""
    if isinstance(f, str):
        return {f}
    return set().union(*(simbolos(x) for x in f[1:]))


def tt_implica(kb, alfa):
    """True si kb ⊨ alfa, enumerando todos los modelos (2^n)."""
    s = sorted(simbolos(kb) | simbolos(alfa))
    for vals in product([True, False], repeat=len(s)):
        m = dict(zip(s, vals))
        if evaluar(kb, m) and not evaluar(alfa, m):
            return False
    return True


def es_tautologia(f):
    """True si f es válida (verdadera en todo modelo)."""
    return tt_implica(("o", "_T", ("no", "_T")), f)


def es_satisfacible(f):
    """True si existe un modelo de f."""
    return not es_tautologia(("no", f))
