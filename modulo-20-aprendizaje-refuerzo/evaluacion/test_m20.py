import numpy as np


def _grid(cargar):
    return cargar("ej01_mdp").crear_gridworld(3, 4, meta=3, trampas={7})


def test_valor(cargar):
    m = cargar("ej01_mdp")
    P = m.crear_gridworld(3, 4, meta=3, trampas={7})
    assert P[0][0] == [(1.0, 0, -0.04, False)]
    assert P[2][1][0][1:] == (3, 1.0, True)
    V, pol = m.iteracion_valor(P, 0.99)
    assert pol[2] == 1 and V[2] > V[0] > 0
    Ps = m.crear_gridworld(3, 4, 3, {7}, deslizamiento=0.2)
    assert np.isclose(sum(p for p, *_ in Ps[0][1]), 1)


def test_politica(cargar):
    P = _grid(cargar)
    V1, p1 = cargar("ej01_mdp").iteracion_valor(P, 0.9)
    V2, p2, it = cargar("ej02_iteracion_politica").iteracion_politica(P, 0.9)
    assert np.allclose(V1, V2, atol=1e-6) and it >= 2


def test_td(cargar):
    m = cargar("ej03_qlearning_sarsa")
    P = _grid(cargar)
    rng = np.random.default_rng(0)
    for algo in (m.q_learning, m.sarsa):
        env = m.EntornoMDP(P, 8, np.random.default_rng(1))
        Q = algo(env, 12, 4, 400, 0.5, 0.95, 0.2, rng)
        s, pasos = 8, 0
        while s != 3 and pasos < 10:
            s = P[s][int(np.argmax(Q[s]))][0][1]
            pasos += 1
        assert s == 3


def test_dqn(cargar):
    m = cargar("ej04_dqn_componentes")
    b = m.BufferRepeticion(3)
    for i in range(5):
        b.agregar([i], i % 2, 1.0, [i + 1], False)
    assert len(b) == 3
    S, A, R, S2, T = b.muestrear(2)
    assert S.shape == (2, 1)
    Rr, Tt = np.array([1.0, 1.0]), np.array([0.0, 1.0])
    Qs = np.array([[1.0, 3.0], [5.0, 2.0]])
    assert np.allclose(m.objetivos_dqn(Rr, Qs, Tt, 0.9), [3.7, 1.0])
    Qt = np.array([[10.0, 0.0], [0.0, 0.0]])
    assert np.allclose(m.objetivos_double_dqn(Rr, Qs, Qt, Tt, 0.5), [1.0, 1.0])
    out = m.actualizacion_suave({"w": np.zeros(2)}, {"w": np.ones(2)}, 0.1)
    assert np.allclose(out["w"], 0.1)


def test_reinforce(cargar):
    m = cargar("ej05_reinforce")
    assert np.allclose(m.retornos([1, 1, 1], 0.5), [1.75, 1.5, 1])
    g = m.grad_log_softmax(np.zeros(2), 0)
    assert np.allclose(g, [0.5, -0.5])
    th = m.reinforce_bandido([0.0, 1.0, 0.2], 2000, 0.05, np.random.default_rng(0))
    assert int(np.argmax(th)) == 1


def test_dpo(cargar):
    m = cargar("ej06_dpo")
    assert np.isclose(m.prob_bradley_terry(1, 1), 0.5)
    assert m.perdida_modelo_recompensa([2.0], [0.0]) < m.perdida_modelo_recompensa([0.0], [2.0])
    assert np.isclose(m.perdida_dpo([0.0], [0.0], [0.0], [0.0]), np.log(2))
    assert m.perdida_dpo([-1.0], [-5.0], [-2.0], [-2.0]) < np.log(2)
