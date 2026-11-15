"""Ejercicio 01 — Tablas de verdad.
Una fórmula se representa como función Python de variables booleanas, p. ej. lambda p, q: (not p) or q."""
import inspect
import itertools


def variables(f):
    """Nombres de los parámetros de la fórmula."""
    return list(inspect.signature(f).parameters)


def tabla_verdad(f):
    """Lista de (tupla_valores, resultado) en orden de itertools.product([False, True], ...)."""
    n = len(variables(f))
    return [(v, bool(f(*v))) for v in itertools.product([False, True], repeat=n)]


def es_tautologia(f):
    """True si f es verdadera en todos los modelos."""
    return all(r for _, r in tabla_verdad(f))


def es_satisfacible(f):
    """True si existe un modelo."""
    return any(r for _, r in tabla_verdad(f))


def equivalentes(f, g):
    """True si f y g (mismas variables) tienen la misma tabla."""
    return [r for _, r in tabla_verdad(f)] == [r for _, r in tabla_verdad(g)]


def implica(kb, alfa):
    """KB |= alfa (mismas variables)."""
    return all(alfa(*v) for v, r in tabla_verdad(kb) if r)
