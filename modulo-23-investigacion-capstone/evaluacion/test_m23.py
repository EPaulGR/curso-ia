import numpy as np


def test_estadistica(cargar):
    m = cargar("ej01_estadistica_experimentos")
    rng = np.random.default_rng(0)
    v = rng.normal(5, 1, 200)
    lo, hi = m.intervalo_bootstrap(v)
    assert lo < 5 < hi and hi - lo < 0.5
    assert m.prueba_permutacion(rng.normal(0, 1, 50), rng.normal(1, 1, 50), 2000) < 0.01
    assert m.prueba_permutacion(v[:50], v[50:100], 500) > 0.05
    y = np.array([1, 1, 1, 1, 0, 0])
    assert np.isclose(m.mcnemar(y, 1 - y, y), (6 - 1) ** 2 / 6)
    assert m.mcnemar(y, y, y) == 0
    assert m.bonferroni([0.01, 0.03], 0.05) == [True, False]


def test_semillas(cargar):
    m = cargar("ej02_semillas")
    h = m.fijar_semillas(1)
    a = np.random.rand()
    m.fijar_semillas(1)
    assert np.random.rand() == a and {"random", "numpy"} <= set(h)
    r = m.correr_semillas(lambda s: float(s), [1, 2, 3])
    assert r["media"] == 2 and np.isclose(r["std"], 1)
    assert m.formato_resultado(r) == "2.00 ± 1.00 (n=3)"


def test_bibliografia(cargar):
    m = cargar("ej03_bibliografia")
    b = m.Biblioteca()
    b.agregar("bahdanau14", "Attention", ["Bahdanau"], 2014, {"nlp"})
    b.agregar("vaswani17", "Attention is all you need", ["Vaswani", "Shazeer"], 2017, {"nlp", "transformer"}, ["bahdanau14", "externo"])
    b.agregar("gpt3", "Language models are few-shot learners", ["Brown"], 2020, {"llm"}, ["vaswani17"])
    assert b.por_etiqueta("nlp") == ["bahdanau14", "vaswani17"]
    assert b.ruta_lectura("gpt3") == ["bahdanau14", "vaswani17", "gpt3"]
    t = b.bibtex("vaswani17")
    assert t.startswith("@article{vaswani17,") and "author={Vaswani and Shazeer}" in t


def test_ablacion(cargar):
    m = cargar("ej04_ablacion")
    g = m.rejilla({"lr": [0.1, 0.01], "capas": [1, 2, 3]})
    assert len(g) == 6 and g[0] == {"lr": 0.1, "capas": 1}
    r = m.busqueda_aleatoria({"lr": lambda rng: 10 ** rng.uniform(-4, -1)}, 5)
    assert len(r) == 5 and all(1e-4 <= c["lr"] <= 0.1 for c in r)
    fn = lambda c: 0.5 + 0.2 * c["atencion"] + 0.05 * c["dropout"]
    res = m.ablacion(fn, {"atencion": True, "dropout": True}, ["atencion", "dropout"])
    assert np.isclose(res["base"], 0.75) and np.isclose(res["atencion"], -0.2)
