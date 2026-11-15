"""Ej 01 — Convolución 2D (correlación cruzada, como en deep learning) en NumPy."""
import numpy as np


def conv2d(img, kernel, stride=1, padding=0):
    """img (H, W), kernel (kh, kw). Devuelve el mapa de salida (correlación cruzada, sin voltear el kernel)."""
    if padding:
        img = np.pad(img, padding)
    kh, kw = kernel.shape
    H = (img.shape[0] - kh) // stride + 1
    W = (img.shape[1] - kw) // stride + 1
    out = np.empty((H, W))
    for i in range(H):
        for j in range(W):
            out[i, j] = (img[i * stride:i * stride + kh, j * stride:j * stride + kw] * kernel).sum()
    return out


def sobel_bordes(img):
    """Magnitud del gradiente con kernels de Sobel (padding=1)."""
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float)
    return np.hypot(conv2d(img, kx, padding=1), conv2d(img, kx.T, padding=1))
