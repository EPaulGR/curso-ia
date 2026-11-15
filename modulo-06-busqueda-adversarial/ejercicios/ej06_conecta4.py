"""Ejercicio 06 — Motor de Conecta-4 (BUAP 3.2 y 3.7: diseño de funciones de evaluación
y aplicación práctica).

Tablero de 6 filas × 7 columnas como tupla de tuplas (fila 0 = arriba), fichas 'X'/'O'/' '.
La acción es la columna (0..6); la ficha cae a la fila libre más baja. Gana quien
alinee 4 en horizontal, vertical o diagonal. 'X' empieza.

Debes implementar la interfaz de juego y una función `evaluar(s, jugador)` heurística:
por cada ventana de 4 casillas, suma +100 si tiene 3 propias y 1 vacía, +10 si 2 propias
y 2 vacías, y resta lo mismo para el rival; +3 por cada ficha propia en la columna central.
"""
FILAS, COLS = 6, 7


def _ventanas():
    """DADO: todas las ventanas de 4 posiciones (fila, col)."""
    v = []
    for f in range(FILAS):
        for c in range(COLS):
            for df, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                pos = [(f + k * df, c + k * dc) for k in range(4)]
                if all(0 <= x < FILAS and 0 <= y < COLS for x, y in pos):
                    v.append(pos)
    return v


VENTANAS = _ventanas()


class Conecta4:
    def estado_inicial(self):
        """Tablero vacío."""
        raise NotImplementedError  # TODO: implementa esta función

    def jugador(self, s):
        """'X' u 'O'."""
        raise NotImplementedError  # TODO: implementa esta función

    def acciones(self, s):
        """Columnas no llenas, ordenadas desde el centro hacia afuera (3,2,4,1,5,0,6)."""
        raise NotImplementedError  # TODO: implementa esta función

    def resultado(self, s, c):
        """Deja caer la ficha del jugador en turno en la columna c."""
        raise NotImplementedError  # TODO: implementa esta función

    def ganador(self, s):
        """'X', 'O' o None."""
        raise NotImplementedError  # TODO: implementa esta función

    def terminal(self, s):
        """Hay ganador o tablero lleno."""
        raise NotImplementedError  # TODO: implementa esta función

    def utilidad(self, s, jugador):
        """+1/-1/0."""
        raise NotImplementedError  # TODO: implementa esta función


def evaluar(s, jugador):
    """Heurística descrita en el enunciado."""
    raise NotImplementedError  # TODO: implementa esta función
