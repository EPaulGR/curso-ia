"""Ejercicio 05 — Evaluación de agentes.

- pass_at_k(n, c, k): estimador insesgado (Chen et al., 2021) de la probabilidad
  de que AL MENOS uno de k intentos sea correcto, con n muestras y c correctas:
  1 - C(n-c, k)/C(n, k).
- pass_pow_k(n, c, k): "pass^k" (τ-bench): probabilidad de que LOS k intentos
  sean correctos: C(c, k)/C(n, k). Mide confiabilidad, no solo capacidad.
- metricas_trayectoria(trayectoria, pasos_optimos): trayectoria = lista de dicts
  {"herramienta": str, "error": bool}. Devuelve {"pasos", "eficiencia"
  (= pasos_optimos/pasos, máx 1), "tasa_error_herramientas", "herramientas_distintas"}.
"""
from math import comb


def pass_at_k(n, c, k):
    raise NotImplementedError  # TODO


def pass_pow_k(n, c, k):
    raise NotImplementedError  # TODO


def metricas_trayectoria(trayectoria, pasos_optimos):
    raise NotImplementedError  # TODO
