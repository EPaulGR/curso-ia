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
        inst = payload.get("instancias") if isinstance(payload, dict) else None
        if not isinstance(inst, list) or not inst:
            raise ValueError("'instancias' debe ser una lista no vacía")
        if len(inst) > self.max_lote:
            raise ValueError(f"máximo {self.max_lote} instancias")
        if not all(isinstance(x, list) and all(isinstance(v, (int, float)) for v in x) for x in inst):
            raise ValueError("cada instancia debe ser lista de números")
        if len({len(x) for x in inst}) != 1:
            raise ValueError("todas las instancias deben tener la misma longitud")

    def predecir(self, payload):
        self.validar(payload)
        t0 = time.perf_counter()
        pred = list(self.modelo(payload["instancias"]))
        self.n += 1
        return {"predicciones": pred, "version": self.version,
                "latencia_ms": (time.perf_counter() - t0) * 1000}

    def salud(self):
        return {"estado": "ok", "version": self.version, "peticiones": self.n}
