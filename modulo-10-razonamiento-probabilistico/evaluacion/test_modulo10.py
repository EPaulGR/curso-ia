"""Tests del módulo 10."""
import numpy as np
import pytest

# Paraguas (AIMA 14.3): estados 0=lluvia, 1=no lluvia; obs 0=paraguas, 1=sin paraguas
PI = np.array([0.5, 0.5])
A = np.array([[0.7, 0.3], [0.3, 0.7]])
B = np.array([[0.9, 0.1], [0.2, 0.8]])


def test_bayes(cargar):
    m = cargar("ej01_bayes")
    assert m.prueba_medica(0.01, 0.9, 0.95) == pytest.approx(0.009 / (0.009 + 0.0495))
    h = m.actualizacion_secuencial({"a": 0.5, "b": 0.5}, [{"a": 0.8, "b": 0.2}] * 2)
    assert h[-1]["a"] == pytest.approx(0.64 / 0.68)


def test_enumeracion(cargar):
    m = cargar("ej02_red_bayesiana")
    red = m.red_alarma()
    a = {"Robo": False, "Sismo": False, "Alarma": True, "Juan": True, "Maria": True}
    assert m.prob_conjunta(red, a) == pytest.approx(0.90 * 0.70 * 0.001 * 0.999 * 0.998)
    assert m.enumeracion(red, "Robo", {"Juan": True, "Maria": True})[True] == pytest.approx(0.284, abs=1e-3)


def test_muestreo(cargar):
    red = cargar("ej02_red_bayesiana").red_alarma()
    s = cargar("ej03_muestreo")
    e = {"Alarma": True}
    exacto = cargar("ej02_red_bayesiana").enumeracion(red, "Robo", e)[True]   # ≈ 0.374
    lw = s.ponderacion_verosimilitud(red, "Alarma", {"Juan": True}, n=20000)
    assert lw == pytest.approx(cargar("ej02_red_bayesiana").enumeracion(red, "Alarma", {"Juan": True})[True], abs=0.015)
    assert s.gibbs(red, "Robo", e, n=8000) == pytest.approx(exacto, abs=0.06)
    assert s.muestreo_rechazo(red, "Sismo", {}, n=20000) == pytest.approx(0.002, abs=0.002)


def test_hmm(cargar):
    m = cargar("ej04_hmm")
    F = m.filtrado(PI, A, B, [0, 0])
    assert F[0, 0] == pytest.approx(0.818, abs=1e-3) and F[1, 0] == pytest.approx(0.883, abs=1e-3)
    S = m.suavizado(PI, A, B, [0, 0])
    assert S[0, 0] == pytest.approx(0.883, abs=1e-3)
    assert m.viterbi(PI, A, B, [0, 0, 1, 0, 0]) == [0, 0, 1, 0, 0]


def test_kalman(cargar):
    m = cargar("ej05_kalman")
    rng = np.random.default_rng(0)
    verdad = 5.0
    z = verdad + rng.normal(0, 1, (200, 1))
    X, P = m.kalman(z, np.eye(1), np.eye(1), np.eye(1) * 1e-6, np.eye(1), [0.0], np.eye(1) * 100)
    assert abs(X[-1, 0] - verdad) < 0.2 and P[-1, 0, 0] < 0.01


def test_difusa(cargar):
    m = cargar("ej06_logica_difusa")
    assert m.triangular(5, 0, 5, 10) == pytest.approx(1) and m.triangular(2.5, 0, 5, 10) == pytest.approx(0.5)
    assert m.trapezoidal(3, 0, 2, 4, 6) == pytest.approx(1) and m.trapezoidal(5, 0, 2, 4, 6) == pytest.approx(0.5)
    baja, alta = m.sistema_propina(1, 1), m.sistema_propina(9.5, 9.5)
    assert baja < 9 and alta > 16 and baja < m.sistema_propina(5, 5) < alta
