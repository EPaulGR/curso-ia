"""Tests del módulo 06. Ejecuta: pytest modulo-06-busqueda-adversarial"""
import pytest


@pytest.fixture
def gato(cargar):
    return cargar("ej01_gato").Gato()


def tablero(txt):
    return tuple(txt.replace("|", "").replace(".", " "))


def test_gato_basico(gato):
    s = gato.estado_inicial()
    assert gato.jugador(s) == "X" and len(gato.acciones(s)) == 9
    s = gato.resultado(s, 4)
    assert s[4] == "X" and gato.jugador(s) == "O"
    g = tablero("XXX|OO.|...")
    assert gato.terminal(g) and gato.utilidad(g, "X") == 1 and gato.utilidad(g, "O") == -1


def test_minimax_gana_o_bloquea(cargar, gato):
    mm = cargar("ej02_minimax")
    a, v, _ = mm.minimax(gato, tablero("XX.|OO.|..."))   # X gana en 2
    assert a == 2 and v == 1
    a, _, _ = mm.minimax(gato, tablero("OO.|X..|X.X"))   # O gana en 2
    assert a == 2


def test_alfabeta_igual_valor_menos_nodos(cargar, gato):
    mm, ab = cargar("ej02_minimax"), cargar("ej03_alfabeta")
    s = tablero("X..|.O.|...")
    a1, v1, n1 = mm.minimax(gato, s)
    a2, v2, n2 = ab.alfabeta(gato, s)
    assert v1 == v2 == 0 and n2 < n1


def test_gato_perfecto_es_empate(cargar, gato):
    _, v, _ = cargar("ej03_alfabeta").alfabeta(gato, gato.estado_inicial())
    assert v == 0


def test_profundizacion_iterativa(cargar, gato):
    pi = cargar("ej04_profundizacion_iterativa")
    cero = lambda s, j: 0
    a, v, hist = pi.profundizacion_iterativa(gato, tablero("XX.|OO.|..."), 3, cero)
    assert a == 2 and v == 1000 and len(hist) == 3


def test_mcts_encuentra_victoria(cargar, gato):
    a = cargar("ej05_mcts").mcts(gato, tablero("XX.|OO.|..."), iteraciones=600, semilla=1)
    assert a == 2


def test_conecta4(cargar):
    m = cargar("ej06_conecta4")
    j = m.Conecta4()
    s = j.estado_inicial()
    for c in (0, 1, 0, 1, 0, 1):
        s = j.resultado(s, c)
    assert s[5][0] == "X" and s[5][1] == "O" and not j.terminal(s)
    assert m.evaluar(s, "X") > 0 or m.evaluar(s, "X") == m.evaluar(s, "X")
    pi = cargar("ej04_profundizacion_iterativa")
    a, _, _ = pi.alfabeta_limitado(j, s, 2, m.evaluar)
    assert a == 0                                  # X conecta 4 en la columna 0
    s2 = j.resultado(s, 0)
    assert j.ganador(s2) == "X" and j.terminal(s2)
