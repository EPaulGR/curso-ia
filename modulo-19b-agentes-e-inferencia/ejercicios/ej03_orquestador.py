"""Ejercicio 03 — Multi-agente: patrón orquestador-trabajadores.

orquestar(tarea, descomponer, trabajadores, agregar, max_hilos=4):
- descomponer(tarea) -> lista de (tipo, entrada).
- trabajadores: dict tipo -> fn(entrada). Ejecuta las subtareas EN PARALELO
  (concurrent.futures.ThreadPoolExecutor) conservando el orden original.
- Si un trabajador lanza excepción o el tipo no existe, su resultado es
  {"error": "<mensaje>"} (el orquestador no se cae).
- Devuelve agregar(lista_de_resultados).
"""
from concurrent.futures import ThreadPoolExecutor


def _ejecutar(trabajadores, tipo, entrada):
    try:
        if tipo not in trabajadores:
            raise KeyError(f"sin trabajador para {tipo}")
        return trabajadores[tipo](entrada)
    except Exception as e:
        return {"error": str(e)}


def orquestar(tarea, descomponer, trabajadores, agregar, max_hilos=4):
    raise NotImplementedError  # TODO
