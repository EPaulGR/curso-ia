"""Ejercicio 5 — Bucle de agente con herramientas (patrón ReAct / tool use).

El LLM (función mensajes -> dict) responde o bien {"herramienta": nombre, "args": {...}}
o bien {"final": texto}. Implementa `ejecutar_agente(llm, herramientas, tarea, max_pasos=5)`:
1. mensajes = [{"rol": "usuario", "contenido": tarea}]
2. En cada paso llama llm(mensajes).
   - Si trae "final": devuelve {"respuesta": final, "pasos": n_llamadas_a_herramientas, "mensajes": mensajes}.
   - Si trae "herramienta": ejecútala con **args (si no existe o lanza excepción, el resultado es
     "ERROR: <mensaje>"), y agrega {"rol": "herramienta", "nombre": ..., "contenido": str(resultado)}.
3. Si se agotan los pasos devuelve respuesta None.
Con la API de Claude esto corresponde a `tool_use` / `tool_result` (modelo claude-opus-5-5).
"""


def ejecutar_agente(llm, herramientas, tarea, max_pasos=5):
    raise NotImplementedError  # TODO: implementa esta función
