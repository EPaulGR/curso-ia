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
    raise NotImplementedError  # TODO: implementa esta función


def gflops_matmul(n, segundos):
    raise NotImplementedError  # TODO: implementa esta función


def ancho_banda_gbs(bytes_, segundos):
    raise NotImplementedError  # TODO: implementa esta función
