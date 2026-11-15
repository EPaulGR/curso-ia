"""Ejercicio 01 — Tablas de verdad.
Una fórmula se representa como función Python de variables booleanas, p. ej. lambda p, q: (not p) or q."""
import inspect
import itertools

def variables(f):
    """Nombres de los parámetros de la fórmula."""
    raise NotImplementedError  # TODO

def tabla_verdad(f):
    """Lista de (tupla_valores, resultado) en orden de itertools.product([False, True], ...)."""
    raise NotImplementedError  # TODO

def es_tautologia(f):
    """True si f es verdadera en todos los modelos."""
    raise NotImplementedError  # TODO

def es_satisfacible(f):
    """True si existe un modelo."""
    raise NotImplementedError  # TODO

def equivalentes(f, g):
    """True si f y g (mismas variables) tienen la misma tabla."""
    raise NotImplementedError  # TODO

def implica(kb, alfa):
    """KB |= alfa (mismas variables)."""
    raise NotImplementedError  # TODO
