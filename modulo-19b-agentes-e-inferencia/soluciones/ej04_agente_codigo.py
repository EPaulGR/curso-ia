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
    ns = {}
    try:
        exec(codigo, ns)
    except Exception as e:
        return [f"error al cargar: {type(e).__name__}: {e}"]
    fn = ns.get(nombre_funcion)
    if not callable(fn):
        return [f"no se encontró la función {nombre_funcion}"]
    fallos = []
    for args, esperado in casos:
        try:
            obtenido = fn(*args)
        except Exception as e:
            fallos.append(f"{nombre_funcion}{tuple(args)} lanzó {type(e).__name__}: {e}")
            continue
        if obtenido != esperado:
            fallos.append(f"{nombre_funcion}{tuple(args)} = {obtenido!r}, esperado {esperado!r}")
    return fallos


def agente_codigo(llm, nombre_funcion, casos, max_iter=5):
    retro, codigo = "", ""
    for i in range(1, max_iter + 1):
        codigo = llm(retro)
        fallos = ejecutar_tests(codigo, nombre_funcion, casos)
        if not fallos:
            return {"exito": True, "codigo": codigo, "iteraciones": i}
        retro = "\n".join(fallos)
    return {"exito": False, "codigo": codigo, "iteraciones": max_iter}
