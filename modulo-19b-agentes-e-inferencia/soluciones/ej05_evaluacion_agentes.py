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
    if n - c < k:
        return 1.0
    return 1.0 - comb(n - c, k) / comb(n, k)


def pass_pow_k(n, c, k):
    return comb(c, k) / comb(n, k)


def metricas_trayectoria(trayectoria, pasos_optimos):
    pasos = len(trayectoria)
    if pasos == 0:
        return {"pasos": 0, "eficiencia": 0.0, "tasa_error_herramientas": 0.0, "herramientas_distintas": 0}
    errores = sum(1 for t in trayectoria if t["error"])
    return {"pasos": pasos,
            "eficiencia": min(1.0, pasos_optimos / pasos),
            "tasa_error_herramientas": errores / pasos,
            "herramientas_distintas": len({t["herramienta"] for t in trayectoria})}
