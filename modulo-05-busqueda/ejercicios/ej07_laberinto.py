"""Ejercicio 07 — Pathfinding en cuadrícula.
Laberinto como lista de strings: '#' muro, '.' libre, 'S' inicio, 'G' meta. Movimientos 4-conexos, costo 1.
Celdas con dígito '1'-'9' son libres con ese costo de entrada (terreno)."""
import importlib.util
import pathlib
_d = pathlib.Path(__file__).parent

def _mod(n):
    spec = importlib.util.spec_from_file_location(n, _d / f'{n}.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m
_p = _mod('ej01_problema')
_a = _mod('ej05_a_estrella')

class Laberinto(_p.Problema):

    def __init__(self, mapa):
        self.mapa = [list(f) for f in mapa]
        for f, fila in enumerate(self.mapa):
            for c, ch in enumerate(fila):
                if ch == 'S':
                    ini = (f, c)
                if ch == 'G':
                    meta = (f, c)
        super().__init__(ini, meta)

    def acciones(self, s):
        """Celdas vecinas transitables en orden arriba, abajo, izquierda, derecha."""
        raise NotImplementedError  # TODO

    def resultado(self, s, a):
        raise NotImplementedError  # TODO

    def costo(self, s, a, s2):
        """1 por defecto o el dígito de la celda destino."""
        raise NotImplementedError  # TODO

def h_manhattan(lab):
    """Devuelve una función h(s) con la distancia Manhattan a la meta de lab."""
    raise NotImplementedError  # TODO

def resolver(mapa):
    """Devuelve (camino, costo) con A* y Manhattan."""
    raise NotImplementedError  # TODO

def dibujar(mapa, camino):
    """Devuelve el mapa como lista de strings con '*' en las celdas del camino (sin tapar S ni G)."""
    raise NotImplementedError  # TODO
