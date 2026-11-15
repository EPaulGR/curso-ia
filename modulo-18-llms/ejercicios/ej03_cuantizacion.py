"""Ejercicio 3 — Cuantización de pesos a mano.

- `cuantizar_int8(w)`: simétrica por tensor. escala = max|w| / 127. Devuelve (q int8, escala).
- `decuantizar(q, escala)`.
- `cuantizar_4bit_grupos(w, grupo)`: w 1-D, por grupos de tamaño `grupo`, asimétrica:
  escala = (max-min)/15, cero = min; q en [0, 15] (uint8). Devuelve (q, escalas, ceros).
- `decuantizar_4bit(q, escalas, ceros, grupo)`.
- `error_mse(a, b)`.
Así funcionan (simplificado) los formatos GGUF Q4 y MLX 4-bit.
"""
import numpy as np


def cuantizar_int8(w):
    raise NotImplementedError  # TODO: implementa esta función


def decuantizar(q, escala):
    raise NotImplementedError  # TODO: implementa esta función


def cuantizar_4bit_grupos(w, grupo=32):
    raise NotImplementedError  # TODO: implementa esta función


def decuantizar_4bit(q, escalas, ceros, grupo=32):
    raise NotImplementedError  # TODO: implementa esta función


def error_mse(a, b):
    raise NotImplementedError  # TODO: implementa esta función
