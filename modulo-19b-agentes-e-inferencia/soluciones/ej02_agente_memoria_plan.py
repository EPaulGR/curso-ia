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
    historial = [{"rol": "usuario", "contenido": tarea}]
    for _ in range(max_pasos):
        accion = llm(historial)
        historial.append({"rol": "asistente", "accion": accion})
        if accion["tipo"] == "final":
            return accion["respuesta"], historial
        fn = herramientas.get(accion["nombre"])
        resultado = fn(**accion.get("args", {})) if fn else "ERROR: herramienta desconocida"
        historial.append({"rol": "herramienta", "nombre": accion["nombre"], "resultado": resultado})
    return None, historial


class Memoria:
    def __init__(self, max_items=5):
        self.max_items = max_items
        self.items = []

    def agregar(self, texto):
        self.items.append(texto)
        while len(self.items) > self.max_items:
            a, b = self.items.pop(0), self.items.pop(0)
            self.items.insert(0, f"RESUMEN: {a} | {b}")

    def recuperar(self, consulta, k=2):
        q = set(consulta.lower().split())
        puntuados = sorted(self.items, key=lambda t: -len(q & set(t.lower().split())))
        return puntuados[:k]


def ejecutar_plan(pasos):
    resultados, visitando = {}, set()

    def visitar(i):
        if i in resultados:
            return
        if i not in pasos:
            raise ValueError(f"dependencia inexistente: {i}")
        if i in visitando:
            raise ValueError(f"ciclo en {i}")
        visitando.add(i)
        deps, fn = pasos[i]
        for d in deps:
            visitar(d)
        resultados[i] = fn({d: resultados[d] for d in deps})
        visitando.discard(i)

    for i in pasos:
        visitar(i)
    return resultados
