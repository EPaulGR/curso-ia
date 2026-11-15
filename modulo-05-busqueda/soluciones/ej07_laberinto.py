"""Ejercicio 07 — Pathfinding en cuadrícula.
Laberinto como lista de strings: '#' muro, '.' libre, 'S' inicio, 'G' meta. Movimientos 4-conexos, costo 1.
Celdas con dígito '1'-'9' son libres con ese costo de entrada (terreno)."""
import importlib.util
import pathlib

_d = pathlib.Path(__file__).parent


def _mod(n):
    spec = importlib.util.spec_from_file_location(n, _d / f"{n}.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); return m


_p = _mod("ej01_problema")
_a = _mod("ej05_a_estrella")


class Laberinto(_p.Problema):
    def __init__(self, mapa):
        self.mapa = [list(f) for f in mapa]
        for f, fila in enumerate(self.mapa):
            for c, ch in enumerate(fila):
                if ch == "S": ini = (f, c)
                if ch == "G": meta = (f, c)
        super().__init__(ini, meta)

    def acciones(self, s):
        """Celdas vecinas transitables en orden arriba, abajo, izquierda, derecha."""
        f, c = s; r = []
        for df, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nf, nc = f + df, c + dc
            if 0 <= nf < len(self.mapa) and 0 <= nc < len(self.mapa[nf]) and self.mapa[nf][nc] != "#":
                r.append((nf, nc))
        return r

    def resultado(self, s, a):
        return a

    def costo(self, s, a, s2):
        """1 por defecto o el dígito de la celda destino."""
        ch = self.mapa[s2[0]][s2[1]]
        return int(ch) if ch.isdigit() else 1


def h_manhattan(lab):
    """Devuelve una función h(s) con la distancia Manhattan a la meta de lab."""
    return lambda s: abs(s[0] - lab.meta[0]) + abs(s[1] - lab.meta[1])


def resolver(mapa):
    """Devuelve (camino, costo) con A* y Manhattan."""
    lab = Laberinto(mapa)
    cam, costo, _ = _a.a_estrella(lab, h_manhattan(lab))
    return cam, costo


def dibujar(mapa, camino):
    """Devuelve el mapa como lista de strings con '*' en las celdas del camino (sin tapar S ni G)."""
    m = [list(f) for f in mapa]
    for f, c in camino or []:
        if m[f][c] not in "SG":
            m[f][c] = "*"
    return ["".join(f) for f in m]
