"""Tests del módulo 18b. Ejecuta:  pytest modulo-18b-arquitecturas-y-razonamiento"""
import numpy as np


def test_rope_relativa(cargar):
    m = cargar("ej01_rope")
    rng = np.random.default_rng(0)
    q, k = rng.standard_normal((1, 8)), rng.standard_normal((1, 8))
    a = m.aplicar_rope(q, [5]) @ m.aplicar_rope(k, [2]).T
    b = m.aplicar_rope(q, [13]) @ m.aplicar_rope(k, [10]).T
    assert np.allclose(a, b)
    assert np.allclose(np.linalg.norm(m.aplicar_rope(q, [7])), np.linalg.norm(q))
    assert np.allclose(m.aplicar_rope(q, [0]), q)


def test_rmsnorm_swiglu(cargar):
    m = cargar("ej02_rmsnorm_swiglu")
    x = np.array([[3.0, 4.0]])
    y = m.rmsnorm(x, np.ones(2), eps=0)
    assert np.allclose(np.mean(y ** 2), 1.0)
    assert np.isclose(m.silu(0.0), 0.0)
    rng = np.random.default_rng(1)
    X = rng.standard_normal((4, 6))
    W1, W3, W2 = rng.standard_normal((6, 10)), rng.standard_normal((6, 10)), rng.standard_normal((10, 6))
    assert m.swiglu(X, W1, W3, W2).shape == (4, 6)


def test_gqa_y_cache(cargar):
    m = cargar("ej03_gqa_kvcache")
    rng = np.random.default_rng(2)
    q = rng.standard_normal((4, 5, 8)); k = rng.standard_normal((2, 5, 8)); v = rng.standard_normal((2, 5, 8))
    full = m.atencion_gqa(q, k, v)
    assert full.shape == (4, 5, 8)
    # las cabezas 0 y 1 comparten K,V: con la misma q dan lo mismo
    q2 = q.copy(); q2[1] = q2[0]
    o = m.atencion_gqa(q2, k, v)
    assert np.allclose(o[0], o[1])
    # decodificación incremental con cache == atención completa causal
    c = m.KVCache()
    for t in range(5):
        kk, vv = c.agregar(k[:, t:t+1], v[:, t:t+1])
        paso = m.atencion_gqa(q[:, t:t+1], kk, vv)
        assert np.allclose(paso[:, 0], full[:, t])
    assert m.bytes_kv_cache(32, 8, 128, 1000) == 2 * 32 * 8 * 128 * 1000 * 2


def test_atencion_bloques(cargar):
    m = cargar("ej04_atencion_bloques")
    rng = np.random.default_rng(3)
    Q, K, V = rng.standard_normal((7, 4)), rng.standard_normal((13, 4)) * 5, rng.standard_normal((13, 3))
    assert np.allclose(m.atencion_por_bloques(Q, K, V, bloque=4), m.atencion_ingenua(Q, K, V))


def test_moe(cargar):
    m = cargar("ej05_moe")
    logits = np.array([[1.0, 3.0, 2.0], [5.0, 0.0, 0.0]])
    idx, w = m.router_topk(logits, 2)
    assert idx[0].tolist() == [1, 2] and np.allclose(w.sum(1), 1)
    expertos = [lambda x, s=s: x * s for s in (1.0, 2.0, 3.0)]
    x = np.array([[0.0, 0.0, 1.0], [1.0, 0.0, 0.0]])
    y = m.moe_forward(x, np.eye(3), expertos, k=1)
    assert np.allclose(y[0], x[0] * 3.0) and np.allclose(y[1], x[1] * 1.0)
    y2 = m.moe_forward(x, np.eye(3), expertos, k=3)
    assert y2.shape == (2, 3)
    uniforme = m.perdida_balanceo(np.zeros((8, 4)) + np.eye(4)[np.arange(8) % 4] * 10)
    sesgado = m.perdida_balanceo(np.tile([10.0, 0, 0, 0], (8, 1)))
    assert sesgado > uniforme


def test_ssm(cargar):
    m = cargar("ej06_ssm_scan")
    rng = np.random.default_rng(4)
    x = rng.standard_normal(20)
    a, b, c = np.array([0.9, 0.5, -0.3]), rng.standard_normal(3), rng.standard_normal(3)
    assert np.allclose(m.scan_lti(x, a, b, c), m.conv_causal(x, m.kernel_conv(a, b, c, 20)))
    A = -np.array([1.0, 2.0, 0.5])
    d = np.full(20, 0.1)
    y = m.scan_selectivo(x, A, b, c, d)
    assert np.allclose(y, m.scan_lti(x, np.exp(0.1 * A), 0.1 * b, c))


def test_escalamiento_destilacion(cargar):
    m = cargar("ej07_escalamiento_y_destilacion")
    N = np.array([1e6, 1e7, 1e8, 1e9])
    A, alpha = m.ajustar_ley_potencias(N, 50 * N ** -0.076)
    assert np.isclose(alpha, 0.076) and np.isclose(A, 50)
    n, d = m.chinchilla_optimo(6 * 70e9 * 1.4e12, tokens_por_parametro=20)
    assert abs(n / 70e9 - 1) < 0.01 and np.isclose(d, 20 * n)
    z = np.array([[1.0, 2.0, 0.5]])
    assert np.isclose(m.perdida_destilacion(z, z), 0, atol=1e-9)
    assert m.perdida_destilacion(-z, z) > 0


def test_inferencia(cargar):
    m = cargar("ej08_razonamiento_inferencia")
    assert m.voto_mayoria(["3", "5", "5", "3", "7"]) == "3"
    assert m.voto_mayoria(["1", "2", "2"]) == "2"
    assert m.best_of_n([3, 9, 4], lambda c: -abs(c - 5)) == 4
    assert np.isclose(m.pass_at_k(10, 1, 1), 0.1)
    assert m.pass_at_k(10, 3, 8) == 1.0
    assert np.isclose(m.pass_at_k(5, 2, 2), 1 - 3 / 10)
    assert m.extraer_respuesta("pienso... 2+2=4. Respuesta: 4") == "4"
    assert m.extraer_respuesta("sin marca") is None


def test_grpo(cargar):
    m = cargar("ej09_grpo")
    A = m.ventajas_grupo([1, 0, 0, 1])
    assert np.allclose(A, [1, -1, -1, 1])
    assert np.allclose(m.ventajas_grupo([1, 1, 1]), 0)
    assert m.recompensa_suma(2, 3, 5) == 1.0
    logits = m.entrenar_grpo(pasos=3000, G=8, lr=1.0, semilla=0)
    assert m.exactitud(logits) >= 0.9


def test_flow_matching(cargar):
    m = cargar("ej10_flow_matching")
    assert np.allclose(m.interpolar(np.zeros((1, 2)), np.ones((1, 2)), np.array([[0.25]])), 0.25)
    rng = np.random.default_rng(0)
    datos = rng.standard_normal((2000, 2)) * 0.3 + np.array([3.0, -2.0])
    W, b, beta = m.entrenar_campo(datos)
    x = m.generar(W, b, beta)
    assert np.linalg.norm(x.mean(0) - np.array([3.0, -2.0])) < 0.3
