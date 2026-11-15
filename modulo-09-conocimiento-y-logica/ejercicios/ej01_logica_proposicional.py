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
    raise NotImplementedError  # TODO: implementa esta función


def simbolos(f):
    """Conjunto de átomos que aparecen en f."""
    raise NotImplementedError  # TODO: implementa esta función


def tt_implica(kb, alfa):
    """True si kb ⊨ alfa, enumerando todos los modelos (2^n)."""
    raise NotImplementedError  # TODO: implementa esta función


def es_tautologia(f):
    """True si f es válida (verdadera en todo modelo)."""
    raise NotImplementedError  # TODO: implementa esta función


def es_satisfacible(f):
    """True si existe un modelo de f."""
    raise NotImplementedError  # TODO: implementa esta función
