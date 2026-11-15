"""Ejercicio 02 — Forma normal conjuntiva y resolución (AIMA 7.5).

Pasos a FNC: (1) eliminar ⇔, (2) eliminar ⇒, (3) mover ¬ hacia adentro (De Morgan,
doble negación), (4) distribuir ∨ sobre ∧.
Cláusula = frozenset de literales; literal = 'p' o '-p'.
Resolución por refutación: KB ⊨ α  ⇔  KB ∧ ¬α es insatisfacible (se deriva la cláusula vacía).
"""
from itertools import combinations


def _neg(l):
    """DADO: niega un literal."""
    return l[1:] if l.startswith("-") else "-" + l


def eliminar_implicaciones(f):
    """Reescribe ⇔ y ⇒ usando ¬, ∧, ∨."""
    raise NotImplementedError  # TODO: implementa esta función


def mover_negaciones(f):
    """Empuja ¬ hasta los átomos (supone que ya no hay ⇒ ni ⇔)."""
    raise NotImplementedError  # TODO: implementa esta función


def a_clausulas(f):
    """Convierte f a FNC y devuelve un conjunto de cláusulas (frozensets).
    Elimina cláusulas tautológicas (que contienen p y -p)."""
    raise NotImplementedError  # TODO: implementa esta función


def resolver(c1, c2):
    """Conjunto de resolventes de dos cláusulas (sin tautologías)."""
    raise NotImplementedError  # TODO: implementa esta función


def resolucion(kb, alfa):
    """True si kb ⊨ alfa (kb y alfa son fórmulas) usando PL-RESOLUTION."""
    raise NotImplementedError  # TODO: implementa esta función
