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
    probs, y = np.asarray(probs, float), np.asarray(y)
    conf = np.maximum(probs, 1 - probs)
    pred = (probs >= 0.5).astype(int)
    bordes = np.linspace(0.5, 1, bins + 1)
    idx = np.clip(np.digitize(conf, bordes) - 1, 0, bins - 1)
    total = 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            total += m.mean() * abs((pred[m] == y[m]).mean() - conf[m].mean())
    return float(total)


def escalado_temperatura(logits, y, temps):
    logits, y = np.asarray(logits, float), np.asarray(y)
    def nll(T):
        p = np.clip(1 / (1 + np.exp(-logits / T)), 1e-12, 1 - 1e-12)
        return -np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))
    return min(temps, key=nll)
