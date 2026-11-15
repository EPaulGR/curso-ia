import numpy as np


def test_bpe(cargar):
    m = cargar("ej01_bpe")
    assert m.contar_pares([1, 2, 1, 2])[(1, 2)] == 2
    assert m.fusionar([1, 2, 3, 1, 2], (1, 2), 9) == [9, 3, 9]
    texto = "el perro y el gato y el ratón"
    f = m.entrenar_bpe(texto, 10)
    assert len(f) == 10 and list(f.values())[0] == 256
    ids = m.codificar(texto, f)
    assert len(ids) < len(texto.encode())
    assert m.decodificar(ids, f) == texto


def test_muestreo(cargar):
    m = cargar("ej02_muestreo")
    l = np.array([1.0, 2.0, 3.0, 0.5])
    assert np.isclose(m.softmax_temperatura(l, 0.5).sum(), 1)
    assert m.softmax_temperatura(l, 0.1)[2] > 0.99
    pk = m.top_k(l, 2)
    assert (pk > 0).sum() == 2 and pk[2] > pk[1]
    pp = m.top_p(np.log([0.5, 0.3, 0.15, 0.05]), 0.75)
    assert (pp > 0).sum() == 2
    assert m.muestrear(np.array([0, 0, 1.0]), np.random.default_rng(0)) == 2


def test_cuantizacion(cargar):
    m = cargar("ej03_cuantizacion")
    w = np.random.default_rng(0).normal(size=256).astype(np.float32)
    q, e = m.cuantizar_int8(w)
    assert q.dtype == np.int8 and m.error_mse(w, m.decuantizar(q, e)) < 1e-3
    q4, es, ce = m.cuantizar_4bit_grupos(w, 32)
    assert q4.max() <= 15 and len(es) == 8
    assert m.error_mse(w, m.decuantizar_4bit(q4, es, ce, 32)) < 0.02


def test_lora(cargar):
    m = cargar("ej04_lora")
    rng = np.random.default_rng(1)
    W = rng.normal(size=(8, 16))
    capa = m.LoRALineal(W, r=2)
    x = rng.normal(size=(64, 16))
    assert np.allclose(capa.forward(x), x @ W.T)
    delta = rng.normal(size=(8, 2)) @ rng.normal(size=(2, 16))
    y = x @ (W + delta).T
    p0 = capa.paso_sgd(x, y, 0.05)
    for _ in range(300):
        p = capa.paso_sgd(x, y, 0.05)
    assert p < p0 * 0.5
    assert np.allclose(capa.W, W)
    assert np.allclose(capa.forward(x), x @ capa.fusionar().T)
    assert capa.n_parametros_entrenables() == 2 * 16 + 8 * 2


def test_memoria(cargar):
    m = cargar("ej05_memoria")
    assert np.isclose(m.memoria_pesos_gb(70e9, 4), 35)
    assert np.isclose(m.memoria_kv_cache_gb(32, 4096, 8192), 2 * 32 * 8192 * 4096 * 2 / 1e9)
    assert m.memoria_kv_cache_gb(32, 4096, 8192, n_kv_heads=8, n_heads=32) < m.memoria_kv_cache_gb(32, 4096, 8192)
    assert np.isclose(m.memoria_full_finetune_gb(7e9), 112)
    assert m.cabe(40, 128) and not m.cabe(120, 128)


def test_bigramas(cargar):
    m = cargar("ej06_bigramas")
    toks = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    P = m.entrenar_bigramas(toks, 3, 0.01)
    assert np.allclose(P.sum(1), 1)
    assert m.perplejidad(P, toks) < 1.1
    assert m.generar(P, 0, 3, np.random.default_rng(0)) == [1, 2, 0]
