"""Ejercicio 3 — Lógica de un servicio de inferencia (independiente del framework web).

Implementa la clase `ServicioModelo(modelo, version, max_lote=32)` donde `modelo` es una
función que recibe lista de listas de floats y devuelve lista de predicciones.
- `validar(payload)`: payload dict con "instancias": lista no vacía de listas de números de
  igual longitud y len <= max_lote. Lanza ValueError con mensaje si no.
- `predecir(payload)`: valida y devuelve {"predicciones": [...], "version": version, "latencia_ms": float}.
- `salud()`: {"estado": "ok", "version": ..., "peticiones": n_peticiones_exitosas}.
Después envuélvelo con FastAPI (ver `servidor_fastapi.py` en soluciones).
"""
import time


class ServicioModelo:

    def __init__(self, modelo, version, max_lote=32):
        self.modelo, self.version, self.max_lote = modelo, version, max_lote
        self.n = 0

    def validar(self, payload):
        raise NotImplementedError  # TODO: implementa esta función

    def predecir(self, payload):
        raise NotImplementedError  # TODO: implementa esta función

    def salud(self):
        raise NotImplementedError  # TODO: implementa esta función
