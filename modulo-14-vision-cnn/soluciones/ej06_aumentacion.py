"""Ej 06 — Data augmentation básica en NumPy."""
import numpy as np


def voltear_h(img):
    """Espejo horizontal de (H, W) o (H, W, C)."""
    return img[:, ::-1]


def recorte_aleatorio(img, tam, rng, padding=0):
    """Rellena con ceros `padding` y recorta un cuadro (tam × tam) en posición aleatoria."""
    if padding:
        img = np.pad(img, [(padding, padding), (padding, padding)] + [(0, 0)] * (img.ndim - 2))
    i = rng.integers(0, img.shape[0] - tam + 1)
    j = rng.integers(0, img.shape[1] - tam + 1)
    return img[i:i + tam, j:j + tam]


def normalizar(img, media, std):
    """(img - media) / std por canal."""
    return (img - np.asarray(media)) / np.asarray(std)
