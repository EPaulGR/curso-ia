"""Ejercicio 04 — Agente de código: bucle editar → ejecutar → test.

1. ejecutar_tests(codigo, nombre_funcion, casos): ejecuta `codigo` con exec en un
   namespace limpio, y para cada (args, esperado) compara fn(*args) == esperado.
   Devuelve lista de mensajes de fallo (vacía si todo pasa). Errores de sintaxis,
   excepciones o función ausente también son fallos (mensaje con el error).
2. agente_codigo(llm, nombre_funcion, casos, max_iter=5): llm(retroalimentacion)
   devuelve código (str). La primera retroalimentación es "". Repite hasta que
   los tests pasen. Devuelve {"exito", "codigo", "iteraciones"}.
⚠️ exec de código generado es peligroso: en un agente real usa un sandbox
(proceso aparte, contenedor, sin red). Aquí es solo didáctico.
"""


def ejecutar_tests(codigo, nombre_funcion, casos):
    raise NotImplementedError  # TODO


def agente_codigo(llm, nombre_funcion, casos, max_iter=5):
    raise NotImplementedError  # TODO
