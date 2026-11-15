"""Ejercicio 01 — Formalización de un juego: el gato (tic-tac-toe).

Un juego de suma cero se define por (AIMA cap. 5.1):
  S0, JUGADOR(s), ACCIONES(s), RESULTADO(s, a), TERMINAL(s), UTILIDAD(s, j)

Representa el tablero como una tupla de 9 casillas con 'X', 'O' o ' '.
Índices:
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
'X' siempre empieza. UTILIDAD devuelve +1 si gana `jugador`, -1 si pierde, 0 empate.
"""

LINEAS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


class Gato:
    def estado_inicial(self):
        """Devuelve el tablero vacío."""
        return (" ",) * 9

    def jugador(self, s):
        """Devuelve 'X' u 'O': a quién le toca mover en s."""
        return "X" if s.count("X") == s.count("O") else "O"

    def acciones(self, s):
        """Lista de índices libres, en orden ascendente."""
        return [i for i, c in enumerate(s) if c == " "]

    def resultado(self, s, a):
        """Nuevo estado tras colocar la ficha del jugador en turno en la casilla a."""
        t = list(s)
        t[a] = self.jugador(s)
        return tuple(t)

    def ganador(self, s):
        """'X', 'O' o None."""
        for a, b, c in LINEAS:
            if s[a] != " " and s[a] == s[b] == s[c]:
                return s[a]
        return None

    def terminal(self, s):
        """True si hay ganador o el tablero está lleno."""
        return self.ganador(s) is not None or " " not in s

    def utilidad(self, s, jugador):
        """+1 / -1 / 0 desde el punto de vista de `jugador`."""
        g = self.ganador(s)
        if g is None:
            return 0
        return 1 if g == jugador else -1
