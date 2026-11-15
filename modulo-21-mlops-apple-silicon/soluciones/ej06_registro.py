"""Ejercicio 6 — Registro de modelos y despliegue canario.

Clase `RegistroModelos`:
- `registrar(nombre, version, metricas: dict)`; versiones semánticas "MAJOR.MINOR.PATCH".
- `promover(nombre, version, etapa)`: etapa en {"staging", "produccion"}; solo una versión por etapa
  (la anterior en esa etapa pasa a "archivado"). Lanza KeyError si no existe.
- `en_etapa(nombre, etapa)` -> version o None.
- `ultima_version(nombre)`: mayor versión semántica (no lexicográfica: "1.10.0" > "1.9.0").
Función `enrutar_canario(id_usuario, porcentaje)`: True si el usuario va al modelo nuevo;
determinista: hash md5 del id (hex -> int) % 100 < porcentaje.
"""
import hashlib


class RegistroModelos:

    def __init__(self):
        self.modelos = {}

    def registrar(self, nombre, version, metricas):
        self.modelos.setdefault(nombre, {})[version] = {"metricas": metricas, "etapa": None}

    def promover(self, nombre, version, etapa):
        vs = self.modelos[nombre]
        if version not in vs:
            raise KeyError(version)
        for v in vs.values():
            if v["etapa"] == etapa:
                v["etapa"] = "archivado"
        vs[version]["etapa"] = etapa

    def en_etapa(self, nombre, etapa):
        return next((v for v, d in self.modelos.get(nombre, {}).items() if d["etapa"] == etapa), None)

    def ultima_version(self, nombre):
        return max(self.modelos[nombre], key=lambda v: tuple(map(int, v.split("."))))


def enrutar_canario(id_usuario, porcentaje):
    return int(hashlib.md5(str(id_usuario).encode()).hexdigest(), 16) % 100 < porcentaje
