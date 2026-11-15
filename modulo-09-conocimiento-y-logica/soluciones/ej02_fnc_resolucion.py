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
    if isinstance(f, str):
        return f
    op, args = f[0], [eliminar_implicaciones(x) for x in f[1:]]
    if op == "implica":
        return ("o", ("no", args[0]), args[1])
    if op == "sii":
        a, b = args
        return ("y", ("o", ("no", a), b), ("o", ("no", b), a))
    return (op, *args)


def mover_negaciones(f):
    """Empuja ¬ hasta los átomos (supone que ya no hay ⇒ ni ⇔)."""
    if isinstance(f, str):
        return f
    if f[0] == "no":
        g = f[1]
        if isinstance(g, str):
            return f
        if g[0] == "no":
            return mover_negaciones(g[1])
        dual = "o" if g[0] == "y" else "y"
        return (dual, mover_negaciones(("no", g[1])), mover_negaciones(("no", g[2])))
    return (f[0], mover_negaciones(f[1]), mover_negaciones(f[2]))


def a_clausulas(f):
    """Convierte f a FNC y devuelve un conjunto de cláusulas (frozensets).
    Elimina cláusulas tautológicas (que contienen p y -p)."""
    g = mover_negaciones(eliminar_implicaciones(f))

    def cnf(g):
        if isinstance(g, str):
            return {frozenset([g])}
        if g[0] == "no":
            return {frozenset(["-" + g[1]])}
        a, b = cnf(g[1]), cnf(g[2])
        if g[0] == "y":
            return a | b
        return {x | y for x in a for y in b}

    return {c for c in cnf(g) if not any(_neg(l) in c for l in c)}


def resolver(c1, c2):
    """Conjunto de resolventes de dos cláusulas (sin tautologías)."""
    res = set()
    for l in c1:
        if _neg(l) in c2:
            r = (c1 - {l}) | (c2 - {_neg(l)})
            if not any(_neg(x) in r for x in r):
                res.add(frozenset(r))
    return res


def resolucion(kb, alfa):
    """True si kb ⊨ alfa (kb y alfa son fórmulas) usando PL-RESOLUTION."""
    clausulas = a_clausulas(("y", kb, ("no", alfa)))
    while True:
        nuevas = set()
        for c1, c2 in combinations(clausulas, 2):
            r = resolver(c1, c2)
            if frozenset() in r:
                return True
            nuevas |= r
        if nuevas <= clausulas:
            return False
        clausulas |= nuevas
