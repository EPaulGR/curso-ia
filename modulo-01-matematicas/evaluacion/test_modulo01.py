import numpy as np


def test_vectores(cargar):
    m = cargar("ej01_vectores")
    assert np.isclose(m.norma([3, -4]), 5) and np.isclose(m.norma([3, -4], 1), 7) and m.norma([3, -4], np.inf) == 4
    assert np.isclose(m.similitud_coseno([1, 0], [1, 1]), np.sqrt(2) / 2)
    assert np.allclose(m.proyeccion([2, 3], [1, 0]), [2, 0])


def test_gauss(cargar):
    m = cargar("ej02_eliminacion_gauss")
    rng = np.random.default_rng(0); A = rng.normal(size=(6, 6)); b = rng.normal(size=6)
    assert np.allclose(m.resolver(A, b), np.linalg.solve(A, b))
    assert np.allclose(m.resolver([[0, 1], [1, 0]], [2, 3]), [3, 2])
    assert np.isclose(m.determinante(A), np.linalg.det(A))
    import pytest
    with pytest.raises(ValueError):
        m.resolver([[1, 2], [2, 4]], [1, 2])


def test_qr(cargar):
    m = cargar("ej03_gram_schmidt")
    A = np.random.default_rng(1).normal(size=(5, 3))
    Q, R = m.qr(A)
    assert np.allclose(Q.T @ Q, np.eye(3)) and np.allclose(Q @ R, A) and np.allclose(np.tril(R, -1), 0)


def test_potencia(cargar):
    m = cargar("ej04_metodo_potencia")
    A = np.array([[2.0, 1], [1, 3]])
    lam, v = m.metodo_potencia(A)
    assert np.isclose(lam, max(np.linalg.eigvalsh(A))) and np.allclose(A @ v, lam * v, atol=1e-6)
    r = m.pagerank([[0, 0, 1], [1, 0, 0], [1, 1, 0]])
    assert np.isclose(r.sum(), 1) and r.argmax() == 2


def test_svd(cargar):
    m = cargar("ej05_svd_compresion")
    rng = np.random.default_rng(2)
    A = rng.normal(size=(20, 2)) @ rng.normal(size=(2, 15))
    assert np.allclose(m.rango_bajo(A, 2), A)
    assert np.isclose(m.energia_retenida(A, 2), 1)
    assert m.k_minimo(np.diag([10.0, 1, 1]), 0.9) == 1


def test_gradientes(cargar):
    m = cargar("ej06_gradiente_numerico")
    rng = np.random.default_rng(3); A = rng.normal(size=(4, 4)); b = rng.normal(size=4); x = rng.normal(size=4)
    f = lambda z: 0.5 * z @ A @ z - b @ z
    assert m.error_relativo(m.gradiente_numerico(f, x), m.grad_cuadratica(A, b, x)) < 1e-6
    X = rng.normal(size=(10, 3)); y = rng.normal(size=10); w = rng.normal(size=3)
    L = lambda z: ((X @ z - y) ** 2).mean()
    assert m.error_relativo(m.gradiente_numerico(L, w), m.grad_minimos_cuadrados(X, y, w)) < 1e-6


def test_optimizadores(cargar):
    m = cargar("ej07_descenso_gradiente")
    g = lambda x: 2 * x
    assert np.allclose(m.gd(g, [5.0, -3], 0.1, 200)[0], 0, atol=1e-6)
    assert np.allclose(m.momentum(g, [5.0, -3], 0.05, 0.9, 500)[0], 0, atol=1e-4)
    assert np.allclose(m.adam(m.grad_rosenbrock, [-1.0, 1.0], 0.02, pasos=5000)[0], [1, 1], atol=0.05)
    assert len(m.gd(g, [1.0], pasos=10)[1]) == 11


def test_regresion(cargar):
    m = cargar("ej08_regresion_minimos_cuadrados")
    rng = np.random.default_rng(4); X = m.agregar_sesgo(rng.normal(size=(100, 2)))
    w_real = np.array([1.0, 2, -3]); y = X @ w_real + 0.01 * rng.normal(size=100)
    w = m.ecuaciones_normales(X, y)
    assert np.allclose(w, w_real, atol=0.01) and np.allclose(m.regresion_gd(X, y), w, atol=1e-3)
    assert np.linalg.norm(m.ridge(X, y, 100.0)) < np.linalg.norm(w)
