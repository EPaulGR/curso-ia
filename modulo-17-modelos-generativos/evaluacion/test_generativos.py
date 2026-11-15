import numpy as np
import pytest


def test_vae_mat(cargar):
    m = cargar("ej01_vae_matematicas")
    assert np.allclose(m.reparametrizar(np.array([1.0]), np.array([np.log(4.0)]), np.array([0.5])), 2.0)
    assert np.allclose(m.kl_normal_estandar(np.zeros((2, 3)), np.zeros((2, 3))), 0)
    assert np.isclose(m.kl_normal_estandar(np.array([1.0]), np.array([0.0])), 0.5)
    assert m.elbo(-3.0, 0.5) == -3.5


def test_vae(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej02_vae")
    torch.manual_seed(0)
    t = torch.rand(256, 1) * 6
    X = torch.cat([t.cos(), t.sin(), 0.1 * t], 1)
    modelo, hist = m.entrenar(X, pasos=400, dispositivo="cpu")
    assert np.mean(hist[-20:]) < hist[0]
    with torch.no_grad():
        _, mu, _ = modelo(X)
        err = ((modelo.dec(mu) - X) ** 2).sum(1).mean()
    assert err < 0.3 * X.var(0).sum()
    xr, mu, lv = modelo(X[:4])
    assert xr.shape == (4, 3) and mu.shape == (4, 2)


def test_gan_perdidas(cargar):
    m = cargar("ej03_gan_perdidas")
    half = np.full(10, 0.5)
    assert np.isclose(m.perdida_discriminador(half, half), 2 * np.log(2))
    assert m.perdida_generador_nosaturante(np.full(5, 0.9)) < m.perdida_generador_nosaturante(np.full(5, 0.1))
    assert m.d_optimo(0.3, 0.3) == 0.5


def test_gan_2d(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej04_gan_2d")
    centro = torch.tensor([3.0, -2.0])
    G = m.entrenar_gan(lambda n: centro + 0.5 * torch.randn(n, 2), pasos=1200, dispositivo="cpu")
    with torch.no_grad():
        s = G(torch.randn(2000, 4))
    assert torch.allclose(s.mean(0), centro, atol=0.4)
    assert 0.2 < s.std(0).mean() < 1.0


def test_difusion_directa(cargar):
    m = cargar("ej05_difusion_directa")
    b, a, ab = m.calendario_lineal(1000)
    assert ab[0] > 0.999 and ab[-1] < 1e-4
    x0 = np.ones(10000) * 2
    xt = m.q_muestra(x0, 999, ab, np.random.default_rng(0).normal(size=10000))
    assert abs(xt.mean()) < 0.05 and abs(xt.std() - 1) < 0.05
    assert np.all(np.diff(m.snr(ab)) < 0)


def test_ddpm(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej06_ddpm")
    torch.manual_seed(1)
    centros = torch.tensor([[-2.0, 0.0], [2.0, 0.0]])
    X = centros[torch.randint(2, (2000,))] + 0.2 * torch.randn(2000, 2)
    modelo, betas, ab = m.entrenar_ddpm(X, pasos=1500, dispositivo="cpu")
    s = m.muestrear(modelo, betas, ab, 1000, dispositivo="cpu")
    cerca = torch.cdist(s, centros).min(1).values
    assert (cerca < 0.8).float().mean() > 0.8
    assert ((s[:, 0] > 0).float().mean() - 0.5).abs() < 0.15


def test_fid(cargar):
    m = cargar("ej07_fid")
    I = np.eye(3)
    assert np.isclose(m.frechet(np.zeros(3), I, np.zeros(3), I), 0, atol=1e-8)
    assert np.isclose(m.frechet(np.zeros(3), I, np.ones(3), I), 3)
    rng = np.random.default_rng(0)
    A, B = rng.normal(size=(500, 4)), rng.normal(1, 1, size=(500, 4))
    assert m.fid_desde_features(A, B) > m.fid_desde_features(A, rng.normal(size=(500, 4)))
