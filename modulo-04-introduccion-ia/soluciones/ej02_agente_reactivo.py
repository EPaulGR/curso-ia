"""Ejercicio 02 — Agente aspiradora reactivo (mundo de 2 celdas A y B)."""


def agente_reactivo(percepcion):
    """percepcion = (ubicacion, estado) con ubicacion en {'A','B'} y estado en {'Sucio','Limpio'}.
    Devuelve 'Aspirar', 'Derecha' o 'Izquierda'."""
    ubic, estado = percepcion
    if estado == "Sucio":
        return "Aspirar"
    return "Derecha" if ubic == "A" else "Izquierda"


def simular(agente, mundo, ubicacion, pasos):
    """mundo: dict {'A': estado, 'B': estado}. Ejecuta el agente y devuelve el puntaje:
    +1 por cada celda limpia en cada paso (medida de desempeño de AIMA)."""
    mundo = dict(mundo); puntaje = 0
    for _ in range(pasos):
        a = agente((ubicacion, mundo[ubicacion]))
        if a == "Aspirar":
            mundo[ubicacion] = "Limpio"
        elif a == "Derecha":
            ubicacion = "B"
        elif a == "Izquierda":
            ubicacion = "A"
        puntaje += sum(v == "Limpio" for v in mundo.values())
    return puntaje
