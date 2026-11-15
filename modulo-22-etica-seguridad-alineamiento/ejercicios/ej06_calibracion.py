"""Ejercicio 6 — Calibración e incertidumbre.

- `ece(probs, y, bins=10)`: Expected Calibration Error para clasificación binaria con
  probs = P(y=1). Usa la confianza max(p, 1-p), predicción p>=0.5, bins uniformes en [0.5, 1]
  (el último bin incluye 1.0); ECE = sum (n_b/N) |exactitud_b - confianza_b|.
- `escalado_temperatura(logits, y, temps)`: elige T en `temps` que minimiza la NLL de
  sigmoid(logits/T). Devuelve T.
Guo et al. 2017, "On Calibration of Modern Neural Networks".
"""
import numpy as np


def ece(probs, y, bins=10):
    raise NotImplementedError  # TODO: implementa esta función


def escalado_temperatura(logits, y, temps):
    raise NotImplementedError  # TODO: implementa esta función
