"""Ejercicio 05 — Unificación en lógica de primer orden (AIMA 9.2.2).

Términos:
    '?x'                      variable (empieza con '?')
    'juan'                    constante
    ('padre', 'juan', '?y')   término compuesto / átomo: (functor, args...)
Una sustitución θ es un dict variable → término.
UNIFICAR(x, y, θ) devuelve el unificador más general o None. Incluye la
verificación de ocurrencia (occurs check): ?x no unifica con f(?x).
"""


def es_variable(t):
    """DADO."""
    return isinstance(t, str) and t.startswith("?")


def sustituir(t, theta):
    """Aplica θ a t de forma recursiva (siguiendo cadenas ?x→?y→c)."""
    if es_variable(t):
        return sustituir(theta[t], theta) if t in theta else t
    if isinstance(t, tuple):
        return tuple(sustituir(x, theta) for x in t)
    return t


def ocurre(v, t, theta):
    """True si la variable v aparece en t (bajo θ)."""
    t = sustituir(t, theta)
    if t == v:
        return True
    return isinstance(t, tuple) and any(ocurre(v, x, theta) for x in t)


def unificar(x, y, theta=None):
    """Unificador más general de x e y extendiendo θ, o None."""
    if theta is None:
        theta = {}
    x, y = sustituir(x, theta), sustituir(y, theta)
    if x == y:
        return theta
    if es_variable(x):
        return None if ocurre(x, y, theta) else {**theta, x: y}
    if es_variable(y):
        return None if ocurre(y, x, theta) else {**theta, y: x}
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            theta = unificar(a, b, theta)
            if theta is None:
                return None
        return theta
    return None
