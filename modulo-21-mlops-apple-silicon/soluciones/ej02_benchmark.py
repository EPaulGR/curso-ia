"""Ejercicio 2 — Medición de rendimiento (profiling) correcta.

- `medir(fn, repeticiones=20, calentamiento=3, sincronizar=None)`: ejecuta `calentamiento`
  veces sin medir, luego mide cada repetición con time.perf_counter (llamando a
  `sincronizar()` tras cada llamada si se da: p. ej. torch.mps.synchronize o mx.eval).
  Devuelve dict con "media", "mediana", "p95", "min" en segundos.
- `gflops_matmul(n, segundos)`: 2*n^3 / segundos / 1e9.
- `ancho_banda_gbs(bytes_, segundos)`.
Clave en GPU: las operaciones son asíncronas; sin sincronizar mides solo el encolado.
"""
import time
import numpy as np


def medir(fn, repeticiones=20, calentamiento=3, sincronizar=None):
    for _ in range(calentamiento):
        fn()
        if sincronizar:
            sincronizar()
    t = []
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        fn()
        if sincronizar:
            sincronizar()
        t.append(time.perf_counter() - t0)
    t = np.array(t)
    return {"media": float(t.mean()), "mediana": float(np.median(t)),
            "p95": float(np.percentile(t, 95)), "min": float(t.min())}


def gflops_matmul(n, segundos):
    return 2 * n ** 3 / segundos / 1e9


def ancho_banda_gbs(bytes_, segundos):
    return bytes_ / segundos / 1e9
