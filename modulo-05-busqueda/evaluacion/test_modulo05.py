import pytest

FACIL = (1, 2, 3, 4, 5, 6, 0, 7, 8)         # 2 movimientos
MEDIO = (8, 6, 7, 2, 5, 4, 3, 0, 1)         # 31 movimientos (de los más difíciles)
OCHO = (1, 2, 3, 4, 0, 6, 7, 5, 8)          # 2 movimientos
M10 = (1, 3, 6, 5, 0, 2, 4, 7, 8)


@pytest.fixture
def P(cargar):
    return cargar("ej01_problema")


def test_problema(P):
    p = P.OchoPuzzle(FACIL)
    assert p.acciones((0, 1, 2, 3, 4, 5, 6, 7, 8)) == ["Abajo", "Derecha"]
    assert p.resultado(FACIL, "Derecha") == (1, 2, 3, 4, 5, 6, 7, 0, 8)
    assert P.inversiones((1, 2, 3, 4, 5, 6, 8, 7, 0)) == 1
    assert not P.es_resoluble((1, 2, 3, 4, 5, 6, 8, 7, 0)) and P.es_resoluble(MEDIO)
    g = P.Grafo("Arad", "Bucharest", P.RUMANIA)
    assert g.acciones("Arad") == ["Sibiu", "Timisoara", "Zerind"] and g.costo("Arad", "Sibiu", "Sibiu") == 140


def test_no_informada(cargar, P):
    m = cargar("ej02_no_informada")
    cam, _ = m.bfs(P.OchoPuzzle(M10))
    assert cam[0] == M10 and cam[-1] == P.META_8 and len(cam) - 1 == 8 if cam else False
    cam, _ = m.iddfs(P.OchoPuzzle(OCHO))
    assert len(cam) == 3
    r, _ = m.dls(P.OchoPuzzle(M10), 3)
    assert r == "corte"
    cam, _ = m.dfs(P.Grafo("Arad", "Bucharest", P.RUMANIA))
    assert cam[0] == "Arad" and cam[-1] == "Bucharest"
    cam, _ = m.bfs(P.Grafo("Arad", "Bucharest", P.RUMANIA))
    assert cam == ["Arad", "Sibiu", "Fagaras", "Bucharest"]


def test_ucs(cargar, P):
    m = cargar("ej03_costo_uniforme")
    cam, c, _ = m.ucs(P.Grafo("Arad", "Bucharest", P.RUMANIA))
    assert c == 418 and cam == ["Arad", "Sibiu", "Rimnicu Vilcea", "Pitesti", "Bucharest"]


def test_heuristicas(cargar):
    m = cargar("ej04_heuristicas")
    s = (7, 2, 4, 5, 0, 6, 8, 3, 1)   # ejemplo AIMA con meta estándar 0-al-final
    assert m.fuera_de_lugar(s) == 6 and m.manhattan(s) == 14
    assert m.conflicto_lineal((2, 1, 3, 4, 5, 6, 7, 8, 0)) == 2 + 2
    assert m.conflicto_lineal(s) >= m.manhattan(s) >= m.fuera_de_lugar(s)


def test_a_estrella(cargar, P):
    m = cargar("ej05_a_estrella"); h = cargar("ej04_heuristicas")
    g = P.Grafo("Arad", "Bucharest", P.RUMANIA)
    cam, c, _ = m.a_estrella(g, P.H_BUCHAREST.get)
    assert c == 418
    cam, c, _ = m.voraz(g, P.H_BUCHAREST.get)
    assert cam == ["Arad", "Sibiu", "Fagaras", "Bucharest"] and c == 450
    _, c1, e1 = m.a_estrella(P.OchoPuzzle(MEDIO), h.manhattan)
    _, c0, e0 = m.a_estrella(P.OchoPuzzle(MEDIO), h.fuera_de_lugar)
    assert c1 == c0 == 31 and e1 < e0
    _, cw, ew = m.a_estrella_ponderado(P.OchoPuzzle(MEDIO), h.manhattan, 3)
    assert 31 <= cw <= 93 and ew < e1


def test_ida(cargar, P):
    m = cargar("ej06_ida_estrella"); h = cargar("ej04_heuristicas")
    cam, c, _ = m.ida_estrella(P.OchoPuzzle(M10), h.manhattan)
    assert c == 8 and cam[-1] == P.META_8
    _, c, _ = m.ida_estrella(P.Grafo("Arad", "Bucharest", P.RUMANIA), P.H_BUCHAREST.get)
    assert c == 418


def test_laberinto(cargar):
    m = cargar("ej07_laberinto")
    mapa = ["S.#.....",
            ".##.###.",
            "....#...",
            ".##...#G"]
    cam, c = m.resolver(mapa)
    assert cam[0] == (0, 0) and cam[-1] == (3, 7) and c == 12
    cam, c = m.resolver(["S9G", ".#.", "..."])
    assert c == 6
    assert "*" in "".join(m.dibujar(mapa, m.resolver(mapa)[0]))


def test_bidireccional(cargar, P):
    m = cargar("ej08_bidireccional"); b = cargar("ej02_no_informada")
    cam, eb = m.bidireccional(P.OchoPuzzle(MEDIO))
    assert cam[0] == MEDIO and cam[-1] == P.META_8 and len(cam) - 1 == 31
    pr = P.OchoPuzzle(MEDIO)
    assert all(cam[i + 1] in [pr.resultado(cam[i], a) for a in pr.acciones(cam[i])] for i in range(31))


def test_comparativa(cargar, P):
    m = cargar("ej09_comparativa")
    assert abs(m.factor_ramificacion_efectivo(52, 5) - 1.92) < 0.01
    s = m.estado_aleatorio(P.OchoPuzzle, 20, 3)
    assert P.es_resoluble(s)
