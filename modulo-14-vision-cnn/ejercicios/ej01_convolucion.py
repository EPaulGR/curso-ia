# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 01 — Convolución 2D (correlación cruzada, como en deep learning) en NumPy."""
import numpy as np

def conv2d(img, kernel, stride=1, padding=0):
    """img (H, W), kernel (kh, kw). Devuelve el mapa de salida (correlación cruzada, sin voltear el kernel)."""
    raise NotImplementedError  # TODO

def sobel_bordes(img):
    """Magnitud del gradiente con kernels de Sobel (padding=1)."""
    raise NotImplementedError  # TODO
