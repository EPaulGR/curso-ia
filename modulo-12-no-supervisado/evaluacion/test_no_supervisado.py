import numpy as np


def blobs(semilla=0):
    rng = np.random.default_rng(semilla)
    centros = np.array([[0, 0], [6, 6], [0, 6]])
    X = np.vstack([c + rng.normal(0, 0.5, (40, 2)) for c in centros])
    y = np.repeat([0, 1, 2], 40)
    return X, y


def misma_particion(a, b):
    from itertools import combinations
    return all((a[i] == a[j]) == (b[i] == b[j]) for i, j in combinations(range(0, len(a), 7), 2))


def test_kmeans(cargar):
    m = cargar("ej01_kmeans")
    X, y = blobs()
    C, et, inercia = m.kmeans(X, 3, semilla=1)
    assert C.shape == (3, 2) and inercia < 200
    assert misma_particion(et, y)


def test_kmeanspp(cargar):
    m = cargar("ej02_kmeanspp")
    X, _ = blobs()
    C = m.kmeanspp(X, 3)
    d = np.sqrt(((C[:, None] - C[None]) ** 2).sum(-1))
    assert C.shape == (3, 2) and d[np.triu_indices(3, 1)].min() > 2


def test_pca(cargar):
    m = cargar("ej03_pca")
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 1)) @ np.array([[3.0, 1.0, 0.5]]) + rng.normal(0, 0.05, (200, 3))
    Z, comp, ratio = m.pca(X, 1)
    assert Z.shape == (200, 1) and ratio[0] > 0.99
    assert np.isclose(np.linalg.norm(comp[0]), 1)
    Xr = m.reconstruir(Z, comp, X.mean(0))
    assert np.abs(Xr - X).max() < 0.5


def test_gmm(cargar):
    m = cargar("ej04_gmm_em")
    rng = np.random.default_rng(0)
    x = np.concatenate([rng.normal(-3, 1, 300), rng.normal(4, 0.5, 300)])
    pi, mu, var, ll = m.em_gmm_1d(x, 2)
    assert np.allclose(sorted(mu), [-3, 4], atol=0.3)
    assert np.isclose(pi.sum(), 1)


def test_dbscan(cargar):
    m = cargar("ej05_dbscan")
    X, y = blobs()
    X = np.vstack([X, [[20, 20]]])
    et = m.dbscan(X, 1.2, 4)
    assert et[-1] == -1
    assert len(set(et[:-1]) - {-1}) == 3


def test_jerarquico(cargar):
    m = cargar("ej06_jerarquico")
    X, y = blobs()
    X, y = X[::3], y[::3]
    et = m.aglomerativo_simple(X, 3)
    assert misma_particion(et, y)


def test_silueta(cargar):
    m = cargar("ej07_silhouette")
    X, y = blobs()
    s = m.silueta(X, y)
    from sklearn.metrics import silhouette_score
    assert np.isclose(s, silhouette_score(X, y), atol=1e-6)
