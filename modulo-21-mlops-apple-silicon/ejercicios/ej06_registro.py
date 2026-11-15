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
        raise NotImplementedError  # TODO: implementa esta función

    def promover(self, nombre, version, etapa):
        raise NotImplementedError  # TODO: implementa esta función

    def en_etapa(self, nombre, etapa):
        raise NotImplementedError  # TODO: implementa esta función

    def ultima_version(self, nombre):
        raise NotImplementedError  # TODO: implementa esta función


def enrutar_canario(id_usuario, porcentaje):
    raise NotImplementedError  # TODO: implementa esta función
