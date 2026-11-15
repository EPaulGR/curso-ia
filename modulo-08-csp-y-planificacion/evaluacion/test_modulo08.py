"""Tests del módulo 08."""
import pytest

SUDOKU = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
SOL = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"


def valida_coloreo(csp, a):
    return all(a[v] != a[w] for v in csp.variables for w in csp.vecinos[v])


def test_modelo(cargar):
    m = cargar("ej01_csp_modelo")
    c = m.coloreo_australia()
    assert c.consistente({"WA": "R"}, "NT", "G") and not c.consistente({"WA": "R"}, "NT", "R")
    assert c.conflictos({"WA": "R", "Q": "R"}, "NT", "R") == 2


def test_backtracking(cargar):
    m, bt = cargar("ej01_csp_modelo"), cargar("ej02_backtracking")
    c = m.coloreo_australia()
    a, _ = bt.backtracking(c)
    assert valida_coloreo(c, a)
    assert bt.backtracking(m.coloreo_australia(("R", "G")))[0] is None
    q = m.n_reinas(8)
    a, n_heur = bt.backtracking(q)
    assert all(q.restriccion(i, a[i], j, a[j]) for i in range(8) for j in range(8) if i != j)
    _, n_simple = bt.backtracking(m.n_reinas(8), mrv=False, lcv=False, forward_checking=False)
    assert n_heur < n_simple
    assert q.dominios[0] == list(range(8))


def test_ac3(cargar):
    m, ac = cargar("ej01_csp_modelo"), cargar("ej03_ac3")
    c = m.coloreo_australia()
    c.dominios.update({"WA": ["R"], "NT": ["G"]})
    assert ac.ac3(c) and c.dominios["SA"] == ["B"] and c.dominios["Q"] == ["R"]
    c2 = m.coloreo_australia(("R", "G"))
    assert ac.ac3(c2) is True  # AC-3 no detecta esta inconsistencia (necesita búsqueda)
    c3 = m.coloreo_australia()
    c3.dominios.update({"WA": ["R"], "NT": ["R"]})
    assert ac.ac3(c3) is False


@pytest.mark.parametrize("n", [8, 50, 200])
def test_min_conflictos(cargar, n):
    f = cargar("ej04_min_conflictos").n_reinas_min_conflictos(n, semilla=1)
    assert f is not None and len(set(f)) == n
    assert len({f[c] - c for c in range(n)}) == n and len({f[c] + c for c in range(n)}) == n


def test_sudoku(cargar):
    s = cargar("ej05_sudoku")
    assert s.resolver_sudoku(SUDOKU) == SOL
    assert s.resolver_sudoku("55" + "0" * 79) is None


def test_strips(cargar):
    m = cargar("ej06_strips")
    acs = m.acciones_bloques(["A", "B", "C"])
    # Anomalía de Sussman: C sobre A; A y B en la mesa → meta A sobre B sobre C
    ini = {"sobre(C,A)", "sobre(A,mesa)", "sobre(B,mesa)", "libre(C)", "libre(B)"}
    meta = {"sobre(A,B)", "sobre(B,C)"}
    plan = m.planificar_bfs(ini, meta, acs)
    assert plan == ["mover(C,A,mesa)", "mover(B,mesa,C)", "mover(A,mesa,B)"]
    plan2, _ = m.planificar_astar(ini, meta, acs)
    assert len(plan2) == 3
    s = frozenset(ini)
    for nombre in plan2:
        a = next(x for x in acs if x.nombre == nombre)
        assert m.aplicable(s, a)
        s = m.resultado(s, a)
    assert meta <= s
