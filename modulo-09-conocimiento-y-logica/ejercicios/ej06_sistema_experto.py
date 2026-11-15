"""Ejercicio 06 — Mini sistema experto / mini-Prolog (AIMA 9.3–9.4; Negnevitsky cap. 2).

Base de conocimiento de primer orden con cláusulas definidas:
    hechos: átomos base, p. ej. ('padre', 'ana', 'luis')
    reglas: (lista_de_premisas, conclusion) con variables, p. ej.
            ([('padre','?x','?y'), ('padre','?y','?z')], ('abuelo','?x','?z'))

1. encadenamiento_adelante_fol: aplica reglas hasta punto fijo (FOL-FC-ASK) → todos los hechos.
2. consultar: encadenamiento hacia atrás estilo Prolog (SLD, profundidad primero), genera
   todas las sustituciones que hacen verdadera la meta; renombra variables de cada regla.
3. explicar: devuelve la cadena de reglas usadas para derivar un hecho (capacidad de
   explicación típica de sistemas expertos como MYCIN).
"""
import itertools

_contador = itertools.count()


def _var(t):
    return isinstance(t, str) and t.startswith("?")


def _sust(t, th):
    if _var(t):
        return _sust(th[t], th) if t in th else t
    if isinstance(t, tuple):
        return tuple(_sust(x, th) for x in t)
    return t


def _unificar(x, y, th):
    """DADO (ver ej05)."""
    if th is None:
        return None
    x, y = _sust(x, th), _sust(y, th)
    if x == y:
        return th
    if _var(x):
        return {**th, x: y}
    if _var(y):
        return {**th, y: x}
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            th = _unificar(a, b, th)
        return th
    return None


def _renombrar(t, sufijo):
    if _var(t):
        return f"{t}_{sufijo}"
    if isinstance(t, tuple):
        return tuple(_renombrar(x, sufijo) for x in t)
    return t


def encadenamiento_adelante_fol(hechos, reglas):
    """Conjunto de todos los hechos base derivables."""
    raise NotImplementedError  # TODO: implementa esta función


def consultar(meta, hechos, reglas, profundidad=20):
    """Generador de sustituciones (dict) restringidas a las variables de `meta`."""
    raise NotImplementedError  # TODO: implementa esta función


def explicar(hecho, hechos, reglas):
    """Lista de pasos (premisas_instanciadas, conclusion) que prueban `hecho`, desde los
    hechos hasta la conclusión; [] si es un hecho dado; None si no se puede probar."""
    raise NotImplementedError  # TODO: implementa esta función
