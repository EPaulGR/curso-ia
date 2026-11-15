"""Tests del módulo 07. Instancias pequeñas con óptimo conocido."""
import itertools
import math

import numpy as np
import pytest

# 8 ciudades sobre un círculo: el óptimo es el polígono, longitud = 16·sin(π/8)
COORDS = [(math.cos(2 * math.pi * k / 8), math.sin(2 * math.pi * k / 8)) for k in (0, 3, 6, 1, 4, 7, 2, 5)]
OPT = 16 * math.sin(math.pi / 8)
PESOS = [12, 7, 11, 8, 9, 6, 5, 14, 3, 10]
VALORES = [24, 13, 23, 15, 16, 11, 9, 25, 4, 19]
CAP = 40


def opt_mochila():
    return max(sum(v for v, b in zip(VALORES, x) if b) for x in itertools.product([0, 1], repeat=10)
               if sum(w for w, b in zip(PESOS, x) if b) <= CAP)


@pytest.fixture
def D(cargar):
    return cargar("ej01_problemas").matriz_distancias(COORDS)


def test_problemas(cargar, D):
    m = cargar("ej01_problemas")
    assert m.longitud_ruta([0, 3, 6, 1, 4, 7, 2, 5], D) == pytest.approx(OPT)
    assert m.dos_opt([0, 1, 2, 3, 4], 1, 3) == [0, 3, 2, 1, 4]
    assert m.valor_mochila([1, 1, 0, 0, 0, 0, 0, 0, 0, 0], PESOS, VALORES, CAP) == 37
    assert m.valor_mochila([1] * 10, PESOS, VALORES, CAP) < 0


def test_hill_climbing_y_recocido(cargar, D):
    m = cargar("ej02_hill_climbing_recocido")
    assert m.hill_climbing_tsp(D, reinicios=5, semilla=0)[1] == pytest.approx(OPT)
    r, l = m.recocido_simulado_tsp(D, iteraciones=5000, semilla=0)
    assert sorted(r) == list(range(8)) and l == pytest.approx(OPT)


def test_tabu(cargar):
    _, v = cargar("ej03_tabu").busqueda_tabu_mochila(PESOS, VALORES, CAP, iteraciones=200, semilla=0)
    assert v == opt_mochila()


def test_genetico(cargar):
    import random
    m = cargar("ej04_genetico")
    rng = random.Random(0)
    h = m.cruce_ox(list(range(10)), list(range(9, -1, -1)), rng)
    assert sorted(h) == list(range(10))
    a, b = m.cruce_un_punto([0] * 6, [1] * 6, rng)
    assert sum(a) + sum(b) == 6
    _, v = m.algoritmo_genetico_mochila(PESOS, VALORES, CAP, semilla=0)
    assert v >= 0.97 * opt_mochila()


def test_aco(cargar, D):
    _, l = cargar("ej05_aco").aco_tsp(D, iteraciones=30, semilla=0)
    assert l == pytest.approx(OPT, rel=1e-6)


def test_clonalg(cargar):
    esfera = lambda x: float(np.sum(x ** 2))
    _, f = cargar("ej06_clonalg").clonalg(esfera, 3, -5.0, 5.0, generaciones=60, semilla=0)
    assert f < 1e-2


def test_memetico(cargar, D):
    _, l = cargar("ej07_memetico").memetico_tsp(D, generaciones=5, semilla=0)
    assert l == pytest.approx(OPT)


def test_pareto(cargar):
    m = cargar("ej08_nsga2")
    P = [(1, 5), (2, 3), (3, 4), (4, 1), (5, 5)]
    assert m.domina((1, 1), (2, 1)) and not m.domina((1, 2), (2, 1))
    assert m.frente_pareto(P) == [0, 1, 3]
    assert m.ordenamiento_no_dominado(P) == [[0, 1, 3], [2], [4]]
    d = m.distancia_crowding(np.array([(1, 5), (2, 3), (4, 1)], float))
    assert np.isinf(d[0]) and np.isinf(d[2]) and d[1] == pytest.approx(2.0)


def test_nsga2_schaffer(cargar):
    m = cargar("ej08_nsga2")
    X, F = m.nsga2(lambda x: (x[0] ** 2, (x[0] - 2) ** 2), 1, -10.0, 10.0, generaciones=40, semilla=0)
    assert np.mean((X[:, 0] >= -0.1) & (X[:, 0] <= 2.1)) > 0.9   # conjunto de Pareto = [0, 2]
    assert np.ptp(X[:, 0]) > 1.0                                  # diversidad
