"""Ej 04 — Convolución multicanal vectorizada con im2col (como lo hacen las librerías)."""
import numpy as np


def im2col(x, k, stride=1):
    """x (C, H, W) → matriz (C·k·k, H_out·W_out) con cada parche como columna."""
    C, H, W = x.shape
    Ho, Wo = (H - k) // stride + 1, (W - k) // stride + 1
    cols = np.empty((C * k * k, Ho * Wo))
    idx = 0
    for i in range(Ho):
        for j in range(Wo):
            cols[:, idx] = x[:, i * stride:i * stride + k, j * stride:j * stride + k].ravel()
            idx += 1
    return cols, Ho, Wo


def conv_multicanal(x, W, b, stride=1):
    """x (C,H,W), W (F,C,k,k), b (F,). Devuelve (F, H_out, W_out) usando una sola multiplicación de matrices."""
    F, C, k, _ = W.shape
    cols, Ho, Wo = im2col(x, k, stride)
    return (W.reshape(F, -1) @ cols + b[:, None]).reshape(F, Ho, Wo)
