import random
import pytest


def test_logica(cargar):
    m = cargar("ej01_tablas_verdad")
    assert m.es_tautologia(lambda p: p or not p)
    assert not m.es_satisfacible(lambda p: p and not p)
    assert m.equivalentes(lambda p, q: not (p and q), lambda p, q: (not p) or (not q))
    assert m.implica(lambda p, q: p and ((not p) or q), lambda p, q: q)
    assert not m.implica(lambda p, q: p or q, lambda p, q: q)
    assert len(m.tabla_verdad(lambda a, b, c: a)) == 8


def test_dpll(cargar):
    m = cargar("ej02_cnf_dpll")
    cnf = [[1, 2], [-1, 3], [-2, -3], [2, 3]]
    a = m.dpll(cnf)
    assert a is not None and m.satisface(cnf, a)
    assert m.dpll([[1], [-1]]) is None
    # palomar: 3 palomas en 2 agujeros es UNSAT
    v = lambda p, h: p * 2 + h + 1
    ph = [[v(p, 0), v(p, 1)] for p in range(3)] + [[-v(p, h), -v(q, h)] for h in range(2) for p in range(3) for q in range(p + 1, 3)]
    assert m.dpll(ph) is None


def test_heap(cargar):
    m = cargar("ej03_heap")
    xs = [random.Random(0).randint(0, 100) for _ in range(200)]
    assert m.heapsort(xs) == sorted(xs)
    h = m.MinHeap(); h.push(5); h.push(1)
    assert h.peek() == 1 and len(h) == 2
    with pytest.raises(IndexError):
        m.MinHeap().pop()


def test_grafos(cargar):
    m = cargar("ej04_grafos")
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert m.bfs_orden(g, "A") == ["A", "B", "C", "D"]
    assert m.dfs_orden(g, "A") == ["A", "B", "D", "C"]
    assert m.orden_topologico(g) == ["A", "B", "C", "D"]
    with pytest.raises(ValueError):
        m.orden_topologico({"a": ["b"], "b": ["a"]})
    assert m.componentes_conexas({1: [2], 2: [1], 3: []}) == 2


def test_dijkstra(cargar):
    m = cargar("ej05_dijkstra")
    g = {"A": [("B", 1), ("C", 4)], "B": [("C", 2), ("D", 5)], "C": [("D", 1)]}
    d, p = m.dijkstra(g, "A")
    assert d["D"] == 4 and m.camino(p, "D") == ["A", "B", "C", "D"]


def test_kruskal(cargar):
    m = cargar("ej06_union_find_kruskal")
    total, mst = m.kruskal("ABCD", [(1, "A", "B"), (3, "A", "C"), (2, "B", "C"), (4, "C", "D"), (5, "B", "D")])
    assert total == 7 and len(mst) == 3


def test_dp(cargar):
    m = cargar("ej07_programacion_dinamica")
    assert m.mochila([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert m.lcs("ABCBDAB", "BDCABA") == 4
    assert m.distancia_edicion("kitten", "sitting") == 3


def test_backtracking(cargar):
    m = cargar("ej08_backtracking")
    assert [m.n_reinas(n) for n in range(1, 9)] == [1, 0, 0, 2, 10, 4, 40, 92]
    assert sorted(m.suma_subconjuntos([1, 2, 3, 4], 5)) == [[1, 4], [2, 3]]
