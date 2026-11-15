import numpy as np
import pytest


def test_estructuras(cargar):
    m = cargar("ej01_estructuras")
    assert m.frecuencias("a b A c") == {"a": 2, "b": 1, "c": 1}
    assert m.top_k("b a b c a b", 2) == [("b", 3), ("a", 2)]
    assert m.invertir_dict({"x": 1, "y": 2, "z": 1}) == {1: ["x", "z"], 2: ["y"]}
    assert m.pares_que_suman([1, 2, 3, 4, 5], 6) == {(1, 5), (2, 4)}


def test_generadores(cargar):
    m = cargar("ej02_generadores")
    assert m.primeros(m.fibonacci(), 7) == [0, 1, 1, 2, 3, 5, 8]
    assert list(m.lotes([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    a = list(m.todas_asignaciones(["A", "B"], [0, 1]))
    assert len(a) == 4 and {"A": 1, "B": 0} in a


def test_decoradores(cargar):
    m = cargar("ej03_decoradores")

    @m.contar_llamadas
    def f(x):
        return x
    f(1); f(2)
    assert f.llamadas == 2

    @m.memoizar
    def fib(n):
        return n if n < 2 else fib(n - 1) + fib(n - 2)
    assert fib(80) == 23416728348467685
    c = m.crear_contador(5)
    assert [c(), c(), c()] == [5, 6, 7]


def test_clases(cargar):
    m = cargar("ej04_clases")
    V = m.Vector2
    assert V(1, 2) + V(3, 4) == V(4, 6)
    assert V(1, 2) * 3 == V(3, 6)
    assert V(1, 0).punto(V(0, 1)) == 0
    assert V(3, 4).norma() == 5
    assert abs(V(3, 4).normalizar().norma() - 1) < 1e-9
    with pytest.raises(ValueError):
        V(0, 0).normalizar()


def test_numpy_basico(cargar):
    m = cargar("ej05_numpy_basico")
    assert m.matriz_tablero(3).tolist() == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert m.reemplazar_negativos(np.array([-1, 2, -3])).tolist() == [0, 2, 0]
    Z = m.normalizar_columnas(np.random.default_rng(0).normal(5, 3, (100, 3)))
    assert np.allclose(Z.mean(0), 0) and np.allclose(Z.std(0), 1)
    assert m.tabla_multiplicar(3)[2, 1] == 6


def test_numpy_vectorizado(cargar):
    m = cargar("ej06_numpy_vectorizado")
    rng = np.random.default_rng(1)
    X, Y = rng.normal(size=(5, 3)), rng.normal(size=(4, 3))
    ref = np.array([[np.linalg.norm(x - y) for y in Y] for x in X])
    assert np.allclose(m.distancias_pares(X, Y), ref)
    s = m.softmax(np.array([[1000.0, 1000.0], [0.0, np.log(3)]]))
    assert np.allclose(s, [[0.5, 0.5], [0.25, 0.75]])
    assert m.one_hot(np.array([0, 2]), 3).tolist() == [[1, 0, 0], [0, 0, 1]]
    Xt = np.array([[0, 0], [10, 10]]); yt = np.array([0, 1])
    assert m.vecino_mas_cercano(Xt, yt, np.array([[1, 1], [9, 8]])).tolist() == [0, 1]


def test_pandas(cargar):
    pd = pytest.importorskip("pandas")
    m = cargar("ej07_pandas")
    df = pd.DataFrame({"g": ["a", "a", "b", "b"], "v": [1.0, None, 3.0, 3.0]})
    l = m.limpiar(df)
    assert len(l) == 3 and l["v"].isna().sum() == 0
    r = m.resumen_por_grupo(pd.DataFrame({"g": ["a", "a", "b"], "v": [1, 3, 10]}), "g", "v")
    assert list(r.index) == ["b", "a"] and r.loc["a", "media"] == 2 and r.loc["a", "conteo"] == 2
