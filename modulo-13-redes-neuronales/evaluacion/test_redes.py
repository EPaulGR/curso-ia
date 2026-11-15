import numpy as np
import pytest


def espirales(n=100, semilla=0):
    rng = np.random.default_rng(semilla)
    X, y = [], []
    for c in range(3):
        r = np.linspace(0, 1, n)
        t = np.linspace(c * 4, (c + 1) * 4, n) + rng.normal(0, 0.2, n)
        X.append(np.c_[r * np.sin(t), r * np.cos(t)])
        y.append(np.full(n, c))
    return np.vstack(X), np.concatenate(y)


def test_perceptron(cargar):
    m = cargar("ej01_perceptron")
    rng = np.random.default_rng(0)
    X = rng.normal(size=(100, 2))
    y = np.where(X[:, 0] + 2 * X[:, 1] > 0.3, 1, -1)
    w, b = m.entrenar_perceptron(X, y, epocas=100)
    assert (m.predecir(X, w, b) == y).mean() > 0.97


def test_activaciones(cargar):
    m = cargar("ej02_activaciones")
    z = np.array([-1000.0, -1, 0, 1, 1000])
    assert np.allclose(m.sigmoide(z), [0, 0.2689414, 0.5, 0.7310586, 1], atol=1e-6)
    assert np.isclose(m.d_sigmoide(np.array([0.0]))[0], 0.25)
    assert np.allclose(m.d_relu(z), [0, 0, 0, 1, 1])
    s = m.softmax(np.array([[1.0, 2, 3], [1000, 1000, 1000]]))
    assert np.allclose(s.sum(1), 1) and np.allclose(s[1], 1 / 3)


def test_gradiente_numerico(cargar):
    m = cargar("ej03_gradiente_numerico")
    x = np.array([1.0, -2.0, 3.0])
    g = m.gradiente_numerico(lambda v: (v ** 2).sum() + v[0] * v[1], x)
    assert m.error_relativo(g, np.array([2 * 1 - 2, -4 + 1, 6])) < 1e-7


def test_mlp_backprop_vs_numerico(cargar):
    m = cargar("ej04_mlp_numpy")
    g_num = cargar("ej03_gradiente_numerico") if False else None
    rng = np.random.default_rng(1)
    X = rng.normal(size=(5, 3)); y = np.array([0, 1, 2, 1, 0])
    net = m.MLP(3, 4, 3, semilla=2)
    net.perdida(net.forward(X), y)
    g = net.backward()
    for nombre in ["W1", "b1", "W2", "b2"]:
        P = getattr(net, nombre)
        num = np.zeros_like(P)
        for i in np.ndindex(P.shape):
            o = P[i]
            P[i] = o + 1e-5; fp = net.perdida(net.forward(X), y)
            P[i] = o - 1e-5; fm = net.perdida(net.forward(X), y)
            P[i] = o
            num[i] = (fp - fm) / 2e-5
        assert np.allclose(num, g[nombre], atol=1e-6), nombre


def test_mlp_aprende_espirales(cargar):
    m = cargar("ej04_mlp_numpy")
    X, y = espirales()
    net, hist = m.entrenar(X, y, h=64, epocas=1500, lr=1.0)
    assert hist[-1] < hist[0] / 3
    assert (net.forward(X).argmax(1) == y).mean() > 0.9


def test_optimizadores(cargar):
    m = cargar("ej05_optimizadores")
    assert np.allclose(m.minimizar_rosenbrock(m.Adam(lr=0.02), 8000), [1, 1], atol=0.05)
    p = m.minimizar_rosenbrock(m.Momentum(lr=1e-4, beta=0.9), 20000)
    assert np.allclose(p, [1, 1], atol=0.1)


def test_autograd(cargar):
    m = cargar("ej06_autograd")
    a, b = m.Valor(2.0), m.Valor(-3.0)
    c = (a * b + a ** 2).tanh() + (a / b).exp()
    c.backward()
    import math
    t = math.tanh(-6 + 4)
    e = math.exp(2 / -3)
    assert math.isclose(a.grad, (1 - t ** 2) * (-3 + 4) + e * (1 / -3), rel_tol=1e-6)
    assert math.isclose(b.grad, (1 - t ** 2) * 2 + e * (-2 / 9), rel_tol=1e-6)


def test_pytorch(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej07_pytorch_mps")
    X, y = espirales()
    _, acc = m.entrenar_torch(torch.tensor(X, dtype=torch.float32), torch.tensor(y), h=64, epocas=400, dispositivo="cpu")
    assert acc > 0.9


def test_regularizacion(cargar):
    m = cargar("ej08_regularizacion")
    rng = np.random.default_rng(0)
    a = np.ones((1000, 100))
    d = m.dropout(a, 0.3, True, rng)
    assert abs(d.mean() - 1) < 0.02 and np.isclose((d == 0).mean(), 0.3, atol=0.02)
    assert np.array_equal(m.dropout(a, 0.3, False, rng), a)
    assert np.allclose(m.l2_grad(np.array([1.0, -2]), 0.1), [0.1, -0.2])
    assert m.early_stopping([5, 4, 3, 3.1, 3.2, 3.3, 2.0], paciencia=3) == 2
