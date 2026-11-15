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
        return tuple((" ",) * COLS for _ in range(FILAS))

    def jugador(self, s):
        """'X' u 'O'."""
        n = sum(fila.count(" ") for fila in s)
        return "X" if (FILAS * COLS - n) % 2 == 0 else "O"

    def acciones(self, s):
        """Columnas no llenas, ordenadas desde el centro hacia afuera (3,2,4,1,5,0,6)."""
        return [c for c in (3, 2, 4, 1, 5, 0, 6) if s[0][c] == " "]

    def resultado(self, s, c):
        """Deja caer la ficha del jugador en turno en la columna c."""
        t = [list(f) for f in s]
        for f in range(FILAS - 1, -1, -1):
            if t[f][c] == " ":
                t[f][c] = self.jugador(s)
                break
        return tuple(tuple(f) for f in t)

    def ganador(self, s):
        """'X', 'O' o None."""
        for pos in VENTANAS:
            vals = {s[f][c] for f, c in pos}
            if len(vals) == 1 and " " not in vals:
                return vals.pop()
        return None

    def terminal(self, s):
        """Hay ganador o tablero lleno."""
        return self.ganador(s) is not None or all(s[0][c] != " " for c in range(COLS))

    def utilidad(self, s, jugador):
        """+1/-1/0."""
        g = self.ganador(s)
        return 0 if g is None else (1 if g == jugador else -1)


def evaluar(s, jugador):
    """Heurística descrita en el enunciado."""
    rival = "O" if jugador == "X" else "X"
    total = 3 * sum(1 for f in range(FILAS) if s[f][3] == jugador)
    for pos in VENTANAS:
        celdas = [s[f][c] for f, c in pos]
        p, r, v = celdas.count(jugador), celdas.count(rival), celdas.count(" ")
        if p == 3 and v == 1:
            total += 100
        elif p == 2 and v == 2:
            total += 10
        if r == 3 and v == 1:
            total -= 100
        elif r == 2 and v == 2:
            total -= 10
    return total
