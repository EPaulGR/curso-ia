import math
import numpy as np


def test_bayes(cargar):
    m = cargar("ej01_bayes")
    assert abs(m.posterior(0.01, 0.99, 0.95) - 0.1667) < 1e-3
    assert m.posterior_repetida(0.01, 0.99, 0.95, 2) > 0.79
    r = m.bayes_discreto({"a": 0.5, "b": 0.5}, {"a": 0.9, "b": 0.1})
    assert abs(r["a"] - 0.9) < 1e-9


def test_distribuciones(cargar):
    m = cargar("ej02_distribuciones")
    assert abs(sum(m.binomial_pmf(k, 10, 0.3) for k in range(11)) - 1) < 1e-12
    assert abs(m.poisson_pmf(2, 3) - 0.22404) < 1e-5
    assert abs(m.normal_pdf(0) - 1 / math.sqrt(2 * math.pi)) < 1e-12
    assert abs(m.normal_cdf(1.96) - 0.975) < 1e-3
    assert m.media_varianza([0, 1], [0.7, 0.3]) == (0.3, 0.21) or np.allclose(m.media_varianza([0, 1], [0.7, 0.3]), (0.3, 0.21))


def test_monte_carlo(cargar):
    m = cargar("ej03_monte_carlo")
    assert abs(m.estimar_pi(200_000) - math.pi) < 0.02
    assert abs(m.integral_mc(np.sin, 0, np.pi, 200_000) - 2) < 0.02
    s = m.muestreo_rechazo(lambda x: 2 * x, 0, 1, 2, 20000)
    assert len(s) == 20000 and abs(s.mean() - 2 / 3) < 0.01


def test_mle_map(cargar):
    m = cargar("ej04_mle_map")
    x = np.random.default_rng(0).normal(3, 2, 50000)
    mu, s2 = m.mle_normal(x)
    assert abs(mu - 3) < 0.05 and abs(s2 - 4) < 0.1
    assert m.log_verosimilitud_normal(x, mu, s2) > m.log_verosimilitud_normal(x, mu + 0.5, s2)
    assert m.map_bernoulli(3, 10, 1, 1) == 0.3 and m.map_bernoulli(0, 2, 2, 2) == 0.25
    assert m.posterior_beta(3, 10, 2, 2) == (5, 9)


def test_bootstrap(cargar):
    m = cargar("ej05_bootstrap")
    x = np.random.default_rng(1).normal(10, 1, 400)
    lo, hi = m.ic_bootstrap(x)
    assert lo < 10 < hi and hi - lo < 0.4
    rng = np.random.default_rng(2)
    assert m.prueba_permutacion(rng.normal(0, 1, 50), rng.normal(1, 1, 50), 2000) < 0.01
    assert m.prueba_permutacion(rng.normal(0, 1, 50), rng.normal(0, 1, 50), 2000) > 0.01


def test_informacion(cargar):
    m = cargar("ej06_informacion")
    assert abs(m.entropia([0.5, 0.5]) - 1) < 1e-12 and m.entropia([1, 0]) == 0
    assert abs(m.entropia_cruzada([1, 0], [0.5, 0.5]) - 1) < 1e-12
    assert m.kl([0.5, 0.5], [0.5, 0.5]) < 1e-12 and m.kl([0.9, 0.1], [0.5, 0.5]) > 0
    assert abs(m.informacion_mutua([[0.5, 0], [0, 0.5]]) - 1) < 1e-12
    assert abs(m.informacion_mutua([[0.25, 0.25], [0.25, 0.25]])) < 1e-12
    assert abs(m.perplejidad([0.25] * 4) - 4) < 1e-9


def test_metropolis(cargar):
    m = cargar("ej07_metropolis")
    s, tasa = m.metropolis(lambda x: -0.5 * (x - 2) ** 2, 0.0, 40000, 1.5)
    s = s[2000:]
    assert abs(s.mean() - 2) < 0.1 and abs(s.std() - 1) < 0.1 and 0.2 < tasa < 0.9
