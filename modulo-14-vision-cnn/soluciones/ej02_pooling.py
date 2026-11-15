"""Ej 02 — Max pooling y average pooling."""
import numpy as np


def max_pool(x, k=2, stride=2):
    """x (H, W). Devuelve el max pooling."""
    H = (x.shape[0] - k) // stride + 1
    W = (x.shape[1] - k) // stride + 1
    return np.array([[x[i * stride:i * stride + k, j * stride:j * stride + k].max() for j in range(W)] for i in range(H)])


def avg_pool(x, k=2, stride=2):
    """x (H, W). Devuelve el average pooling."""
    H = (x.shape[0] - k) // stride + 1
    W = (x.shape[1] - k) // stride + 1
    return np.array([[x[i * stride:i * stride + k, j * stride:j * stride + k].mean() for j in range(W)] for i in range(H)])
