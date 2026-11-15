import numpy as np
import pytest

TEXTO = ("en un lugar de la mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo "
         "de los de lanza en astillero adarga antigua rocin flaco y galgo corredor ") * 20


def test_atencion(cargar):
    m = cargar("ej01_atencion")
    rng = np.random.default_rng(0)
    Q, K, V = rng.normal(size=(3, 4)), rng.normal(size=(5, 4)), rng.normal(size=(5, 2))
    out, p = m.atencion(Q, K, V)
    assert out.shape == (3, 2) and np.allclose(p.sum(1), 1)
    torch = pytest.importorskip("torch")
    ref = torch.nn.functional.scaled_dot_product_attention(*(torch.tensor(a) for a in (Q, K, V)))
    assert np.allclose(out, ref.numpy())
    mask = np.zeros((3, 5), bool); mask[:, 0] = True
    out2, _ = m.atencion(Q, K, V, mask)
    assert np.allclose(out2, V[0])


def test_mascaras(cargar):
    m = cargar("ej02_mascara_causal")
    c = m.mascara_causal(3)
    assert c.tolist() == [[True, False, False], [True, True, False], [True, True, True]]
    assert m.mascara_padding([2, 3], 4).tolist() == [[True, True, False, False], [True, True, True, False]]


def test_posicional(cargar):
    m = cargar("ej03_posicional")
    pe = m.codificacion_posicional(50, 16)
    assert pe.shape == (50, 16)
    assert np.allclose(pe[0, 0::2], 0) and np.allclose(pe[0, 1::2], 1)
    assert np.isclose(pe[3, 0], np.sin(3))


def test_normas(cargar):
    m = cargar("ej04_layernorm")
    torch = pytest.importorskip("torch")
    x = np.random.default_rng(0).normal(size=(2, 3, 8))
    g, b = np.full(8, 2.0), np.full(8, 0.5)
    ref = torch.nn.functional.layer_norm(torch.tensor(x), (8,), torch.tensor(g), torch.tensor(b)).numpy()
    assert np.allclose(m.layer_norm(x, g, b), ref)
    r = m.rms_norm(x, np.ones(8))
    assert np.allclose((r ** 2).mean(-1), 1, atol=1e-4)


def test_multihead_causal(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej05_multihead")
    torch.manual_seed(0)
    att = m.AtencionMultiCabeza(16, 4)
    x = torch.randn(2, 6, 16)
    y = att(x)
    assert y.shape == (2, 6, 16)
    x2 = x.clone(); x2[:, -1] += 10  # cambiar el futuro no debe afectar el pasado
    assert torch.allclose(att(x2)[:, :-1], y[:, :-1], atol=1e-5)


def test_bloque(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej06_bloque")
    b = m.Bloque(16, 2)
    assert b(torch.randn(1, 5, 16)).shape == (1, 5, 16)


def test_mini_gpt(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej07_mini_gpt")
    tok = m.TokenizadorCaracteres("hola")
    assert tok.decodificar(tok.codificar("hola")) == "hola"
    modelo, tok, hist = m.entrenar(TEXTO, pasos=250, dispositivo="cpu", d=48, n=2)
    assert hist[0] > 2.5 and np.mean(hist[-20:]) < 1.0
    salida = modelo.generar(torch.tensor([tok.codificar("en un ")]), 30)
    assert salida.shape == (1, 36)


def test_muestreo(cargar):
    m = cargar("ej08_muestreo")
    l = np.array([2.0, 1.0, 0.0, -1.0])
    assert m.con_temperatura(l, 0.01)[0] > 0.999
    assert np.allclose(m.con_temperatura(l, 1e6), 0.25, atol=1e-4)
    p = np.array([0.5, 0.3, 0.15, 0.05])
    assert np.allclose(m.top_k(p, 2), [0.625, 0.375, 0, 0])
    assert np.allclose(m.top_p(p, 0.75), [0.625, 0.375, 0, 0])
    assert np.allclose(m.top_p(p, 0.9), np.array([0.5, 0.3, 0.15, 0]) / 0.95)
