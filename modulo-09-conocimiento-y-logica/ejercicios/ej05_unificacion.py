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
    raise NotImplementedError  # TODO: implementa esta función


def ocurre(v, t, theta):
    """True si la variable v aparece en t (bajo θ)."""
    raise NotImplementedError  # TODO: implementa esta función


def unificar(x, y, theta=None):
    """Unificador más general de x e y extendiendo θ, o None."""
    raise NotImplementedError  # TODO: implementa esta función
