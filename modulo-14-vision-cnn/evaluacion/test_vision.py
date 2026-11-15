import numpy as np
import pytest


def test_conv(cargar):
    m = cargar("ej01_convolucion")
    img = np.arange(16.0).reshape(4, 4)
    k = np.array([[1.0, 0], [0, -1]])
    out = m.conv2d(img, k)
    assert out.shape == (3, 3) and np.allclose(out, -5)
    assert m.conv2d(img, np.ones((3, 3)), stride=1, padding=1).shape == (4, 4)
    assert m.conv2d(np.ones((7, 7)), np.ones((3, 3)), stride=2).shape == (3, 3)
    escalon = np.zeros((8, 8)); escalon[:, 4:] = 1
    b = m.sobel_bordes(escalon)
    assert b[4, 3:5].min() > b[4, 1] and b[4, 1] == 0


def test_pool(cargar):
    m = cargar("ej02_pooling")
    x = np.arange(16.0).reshape(4, 4)
    assert np.array_equal(m.max_pool(x), [[5, 7], [13, 15]])
    assert np.allclose(m.avg_pool(x), [[2.5, 4.5], [10.5, 12.5]])


def test_dimensiones(cargar):
    m = cargar("ej03_dimensiones")
    assert m.tam_salida(224, 7, 2, 3) == 112
    assert m.tam_salida(32, 3, 1, 1) == 32
    assert m.tam_salida(32, 3, dilatacion=2) == 28
    assert m.params_conv(3, 64, 3) == 1792
    assert m.campo_receptivo([(3, 1), (3, 1), (3, 1)]) == 7
    assert m.campo_receptivo([(3, 2), (3, 2)]) == 7


def test_im2col_vs_torch(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej04_im2col")
    rng = np.random.default_rng(0)
    x = rng.normal(size=(3, 6, 6)); W = rng.normal(size=(4, 3, 3, 3)); b = rng.normal(size=4)
    ref = torch.nn.functional.conv2d(torch.tensor(x)[None], torch.tensor(W), torch.tensor(b), stride=1)[0].numpy()
    assert np.allclose(m.conv_multicanal(x, W, b), ref)
    ref2 = torch.nn.functional.conv2d(torch.tensor(x)[None], torch.tensor(W), torch.tensor(b), stride=2)[0].numpy()
    assert np.allclose(m.conv_multicanal(x, W, b, stride=2), ref2)


def test_cnn(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej05_cnn_torch")
    g = torch.Generator().manual_seed(0)
    X = torch.rand(200, 1, 16, 16, generator=g) * 0.3
    y = torch.arange(200) % 2
    X[y == 0, :, 6:10, :] += 1.0   # barra horizontal
    X[y == 1, :, :, 6:10] += 1.0   # barra vertical
    modelo, acc = m.entrenar(X, y, 2, epocas=10, dispositivo="cpu")
    assert modelo(X[:3]).shape == (3, 2)
    assert acc > 0.95


def test_aumentacion(cargar):
    m = cargar("ej06_aumentacion")
    img = np.arange(12.0).reshape(3, 4)
    assert np.array_equal(m.voltear_h(img)[0], [3, 2, 1, 0])
    r = m.recorte_aleatorio(np.ones((32, 32, 3)), 32, np.random.default_rng(0), padding=4)
    assert r.shape == (32, 32, 3)
    assert np.allclose(m.normalizar(np.full((2, 2, 3), 0.5), [0.5] * 3, [0.25] * 3), 0)


def test_residual(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej07_bloque_residual")
    x = torch.randn(2, 8, 16, 16)
    assert m.BloqueResidual(8, 8)(x).shape == (2, 8, 16, 16)
    assert m.BloqueResidual(8, 16, 2)(x).shape == (2, 16, 8, 8)


def test_deteccion(cargar):
    m = cargar("ej08_deteccion")
    assert np.isclose(m.iou([0, 0, 2, 2], [1, 1, 3, 3]), 1 / 7)
    assert m.iou([0, 0, 1, 1], [2, 2, 3, 3]) == 0
    cajas = np.array([[0, 0, 10, 10], [1, 1, 11, 11], [20, 20, 30, 30]])
    assert m.nms(cajas, np.array([0.9, 0.8, 0.7])) == [0, 2]
