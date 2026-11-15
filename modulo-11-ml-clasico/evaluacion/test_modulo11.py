"""Tests del módulo 11 (datos sintéticos y conjuntos de scikit-learn)."""
import numpy as np
import pytest

sk = pytest.importorskip("sklearn")
from sklearn.datasets import load_breast_cancer, load_iris, make_moons  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402


@pytest.fixture
def lineal():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 3))
    y = 4 + X @ np.array([2.0, -1.0, 0.5]) + rng.normal(0, 0.1, 200)
    return X, y


@pytest.fixture
def cancer():
    X, y = load_breast_cancer(return_X_y=True)
    return StandardScaler().fit_transform(X), y


def test_regresion_lineal(cargar, lineal):
    m = cargar("ej01_regresion_lineal")
    X, y = lineal
    th = m.ecuacion_normal(X, y)
    assert th == pytest.approx([4, 2, -1, 0.5], abs=0.05)
    th_gd, hist = m.descenso_gradiente(X, y, lr=0.1, epocas=500)
    assert th_gd == pytest.approx(th, abs=1e-3) and hist[-1] < hist[0]
    assert np.abs(m.ridge(X, y, 1000.0)[1:]).sum() < np.abs(th[1:]).sum()
    assert m.r2(y, m.predecir(th, X)) > 0.99


def test_logistica(cargar, cancer):
    m = cargar("ej02_regresion_logistica")
    assert m.sigmoide(0) == pytest.approx(0.5) and np.isfinite(m.sigmoide(np.array([-1000, 1000]))).all()
    X, y = cancer
    w, b = m.entrenar_logistica(X, y, lr=0.5, epocas=1000)
    p = m.predecir_proba(w, b, X)
    assert np.mean((p > 0.5) == y) > 0.97 and m.entropia_cruzada(y, p) < 0.1


def test_knn_nb(cargar):
    m = cargar("ej03_knn_naive_bayes")
    from sklearn.naive_bayes import GaussianNB
    X, y = load_iris(return_X_y=True)
    assert np.mean(m.knn_predecir(X[::2], y[::2], X[1::2], k=5) == y[1::2]) > 0.93
    nb = m.NaiveBayesGaussiano().fit(X, y)
    assert (nb.predict(X) == GaussianNB().fit(X, y).predict(X)).all()


def test_arbol(cargar):
    m = cargar("ej04_arbol_decision")
    assert m.gini([0, 0, 1, 1]) == pytest.approx(0.5) and m.entropia([0, 1]) == pytest.approx(1.0)
    X, y = load_iris(return_X_y=True)
    j, u, g = m.mejor_division(X, y)
    assert j in (2, 3) and g == pytest.approx(1 / 3, abs=1e-6)
    a = m.ArbolDecision().fit(X, y)
    assert np.mean(a.predict(X) == y) == 1.0
    assert m.ArbolDecision(profundidad_max=2).fit(X, y).profundidad() == 2


def test_metricas(cargar):
    m = cargar("ej05_metricas_validacion")
    y, yp = np.array([1, 1, 1, 0, 0, 0]), np.array([1, 1, 0, 1, 0, 0])
    assert m.matriz_confusion(y, yp).tolist() == [[2, 1], [1, 2]]
    assert m.precision_recall_f1(y, yp) == pytest.approx((2 / 3, 2 / 3, 2 / 3))
    assert m.auc([0, 0, 1, 1], [0.1, 0.4, 0.35, 0.8]) == pytest.approx(0.75)
    folds = m.k_fold_indices(10, 3)
    assert sorted(np.concatenate([v for _, v in folds]).tolist()) == list(range(10))
    arbol = cargar("ej04_arbol_decision")
    X, yy = load_iris(return_X_y=True)
    acc = m.validacion_cruzada(lambda: arbol.ArbolDecision(profundidad_max=3), X, yy, k=5)
    assert len(acc) == 5 and acc.mean() > 0.9


def test_adaboost(cargar):
    m = cargar("ej06_ensembles")
    X, y = make_moons(300, noise=0.2, random_state=0)
    y2 = np.where(y == 1, 1, -1)
    ada = m.AdaBoost(40).fit(X, y2)
    assert np.mean(ada.predict(X) == y2) > 0.93
    r = m.comparar_sklearn(X, y)
    assert set(r) == {"arbol", "bosque", "gboost"} and r["bosque"] > 0.9


def test_svm(cargar, cancer):
    m = cargar("ej07_svm_pipeline")
    X, y = cancer
    y2 = np.where(y == 1, 1, -1)
    w = m.pegasos(X, y2, lam=0.01, iteraciones=20000)
    assert np.mean(m.predecir_svm(w, X) == y2) > 0.96
    Xm, ym = make_moons(200, noise=0.2, random_state=0)
    params, score = m.busqueda_svm_rbf(Xm, ym)
    assert "svc__C" in params and score > 0.9
