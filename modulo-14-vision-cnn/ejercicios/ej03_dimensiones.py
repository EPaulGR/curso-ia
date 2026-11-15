# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 03 — Aritmética de dimensiones y parámetros en CNNs."""

def tam_salida(n, k, stride=1, padding=0, dilatacion=1):
    """floor((n + 2p - d(k-1) - 1)/s) + 1"""
    raise NotImplementedError  # TODO

def params_conv(c_in, c_out, k, sesgo=True):
    """Número de parámetros de una Conv2d con kernel k×k."""
    raise NotImplementedError  # TODO

def campo_receptivo(capas):
    """capas: lista de (k, stride). Devuelve el campo receptivo de la última capa."""
    raise NotImplementedError  # TODO
