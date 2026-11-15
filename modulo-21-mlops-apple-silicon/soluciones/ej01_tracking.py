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
        run_id = f"{nombre}-{uuid.uuid4().hex[:8]}"
        d = self.dir / run_id
        d.mkdir()
        (d / "params.json").write_text(json.dumps(params))
        return run_id

    def log_metrica(self, run_id, clave, valor, paso):
        with open(self.dir / run_id / "metrics.jsonl", "a") as f:
            f.write(json.dumps({"clave": clave, "valor": valor, "paso": paso}) + "\n")

    def historial(self, run_id, clave):
        p = self.dir / run_id / "metrics.jsonl"
        if not p.exists():
            return []
        filas = [json.loads(l) for l in p.read_text().splitlines()]
        return [(f["paso"], f["valor"]) for f in filas if f["clave"] == clave]

    def mejor_run(self, clave, modo="min"):
        finales = {}
        for d in self.dir.iterdir():
            h = self.historial(d.name, clave)
            if h:
                finales[d.name] = max(h)[1]
        elige = min if modo == "min" else max
        return elige(finales, key=finales.get)
