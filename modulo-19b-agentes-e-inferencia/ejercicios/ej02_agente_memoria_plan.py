"""Ejercicio 02 — Bucle de agente, memoria y planificación.

1. ejecutar_agente(llm, herramientas, tarea, max_pasos): el LLM recibe el
   historial (lista de dicts) y devuelve {"tipo": "herramienta", "nombre", "args"}
   o {"tipo": "final", "respuesta"}. Ejecuta herramientas, agrega
   {"rol": "herramienta", "nombre", "resultado"} al historial. Si la herramienta
   no existe, el resultado es "ERROR: herramienta desconocida". Devuelve
   (respuesta, historial); si se agotan los pasos, respuesta = None.
2. Memoria(max_items): agregar(texto), recuperar(consulta, k) por solapamiento
   de palabras (minúsculas), y al superar max_items compacta las 2 entradas más
   antiguas en una sola "RESUMEN: a | b".
3. ejecutar_plan(pasos): pasos = {id: (dependencias, fn)}; fn recibe un dict con
   los resultados de sus dependencias. Ejecuta en orden topológico y devuelve
   {id: resultado}. Lanza ValueError si hay ciclo o dependencia inexistente.
"""


def ejecutar_agente(llm, herramientas, tarea, max_pasos=10):
    raise NotImplementedError  # TODO


class Memoria:
    def __init__(self, max_items=5):
        self.max_items = max_items
        self.items = []

    def agregar(self, texto):
        raise NotImplementedError  # TODO

    def recuperar(self, consulta, k=2):
        raise NotImplementedError  # TODO


def ejecutar_plan(pasos):
    raise NotImplementedError  # TODO
