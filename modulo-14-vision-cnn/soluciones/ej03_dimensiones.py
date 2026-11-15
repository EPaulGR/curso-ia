"""Ej 03 — Aritmética de dimensiones y parámetros en CNNs."""


def tam_salida(n, k, stride=1, padding=0, dilatacion=1):
    """floor((n + 2p - d(k-1) - 1)/s) + 1"""
    return (n + 2 * padding - dilatacion * (k - 1) - 1) // stride + 1


def params_conv(c_in, c_out, k, sesgo=True):
    """Número de parámetros de una Conv2d con kernel k×k."""
    return c_out * c_in * k * k + (c_out if sesgo else 0)


def campo_receptivo(capas):
    """capas: lista de (k, stride). Devuelve el campo receptivo de la última capa."""
    r, salto = 1, 1
    for k, s in capas:
        r += (k - 1) * salto
        salto *= s
    return r
