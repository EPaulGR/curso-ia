"""Ejercicio 03 — Agente basado en modelo: recuerda qué celdas sabe limpias y se detiene (NoOp)."""


class AgenteModelo:
    def __init__(self):
        self.conocido = {}

    def __call__(self, percepcion):
        """Acción: 'Aspirar', 'Derecha', 'Izquierda' o 'NoOp' cuando sabe que A y B están limpias."""
        ubic, estado = percepcion
        if estado == "Sucio":
            self.conocido[ubic] = "Limpio"
            return "Aspirar"
        self.conocido[ubic] = "Limpio"
        if self.conocido.get("A") == "Limpio" and self.conocido.get("B") == "Limpio":
            return "NoOp"
        return "Derecha" if ubic == "A" else "Izquierda"
