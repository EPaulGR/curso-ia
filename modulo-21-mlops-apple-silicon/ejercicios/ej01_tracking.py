"""Ejercicio 1 — Rastreador de experimentos mínimo (como MLflow/W&B, en archivos).

Clase `Rastreador(directorio)`:
- `iniciar(nombre, params: dict) -> run_id` (str único); crea <dir>/<run_id>/params.json.
- `log_metrica(run_id, clave, valor, paso)`: agrega una línea JSON a metrics.jsonl.
- `historial(run_id, clave)`: lista de (paso, valor).
- `mejor_run(clave, modo="min")`: run_id cuyo ÚLTIMO valor de la métrica es el mejor.
"""
import json
import uuid
from pathlib import Path


class Rastreador:

    def __init__(self, directorio):
        self.dir = Path(directorio)
        self.dir.mkdir(parents=True, exist_ok=True)

    def iniciar(self, nombre, params):
        raise NotImplementedError  # TODO: implementa esta función

    def log_metrica(self, run_id, clave, valor, paso):
        raise NotImplementedError  # TODO: implementa esta función

    def historial(self, run_id, clave):
        raise NotImplementedError  # TODO: implementa esta función

    def mejor_run(self, clave, modo="min"):
        raise NotImplementedError  # TODO: implementa esta función
