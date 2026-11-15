# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 04 — Convolución multicanal vectorizada con im2col (como lo hacen las librerías)."""
import numpy as np

def im2col(x, k, stride=1):
    """x (C, H, W) → matriz (C·k·k, H_out·W_out) con cada parche como columna."""
    raise NotImplementedError  # TODO

def conv_multicanal(x, W, b, stride=1):
    """x (C,H,W), W (F,C,k,k), b (F,). Devuelve (F, H_out, W_out) usando una sola multiplicación de matrices."""
    raise NotImplementedError  # TODO
