# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-14-vision-cnn

"""Ej 06 — Data augmentation básica en NumPy."""
import numpy as np

def voltear_h(img):
    """Espejo horizontal de (H, W) o (H, W, C)."""
    raise NotImplementedError  # TODO

def recorte_aleatorio(img, tam, rng, padding=0):
    """Rellena con ceros `padding` y recorta un cuadro (tam × tam) en posición aleatoria."""
    raise NotImplementedError  # TODO

def normalizar(img, media, std):
    """(img - media) / std por canal."""
    raise NotImplementedError  # TODO
