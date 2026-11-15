import numpy as np
import pytest


def test_tokenizacion(cargar):
    m = cargar("ej01_tokenizacion")
    assert m.tokenizar("¡Hola, Mundo! Año 2026.") == ["¡", "hola", ",", "mundo", "!", "año", "2026", "."]
    v = m.construir_vocab(["a b b", "b c"])
    assert v["<pad>"] == 0 and v["<unk>"] == 1 and v["b"] == 2
    assert m.codificar("b zzz", v) == [2, 1]


def test_tfidf(cargar):
    m = cargar("ej02_tfidf")
    from sklearn.feature_extraction.text import TfidfVectorizer
    docs = ["el gato come", "el perro come carne", "gato gato perro"]
    tv = TfidfVectorizer(sublinear_tf=False, norm="l2")
    ref = tv.fit_transform(docs).toarray()
    vocab = tv.vocabulary_
    C = m.bolsa_palabras([d.split() for d in docs], vocab)
    assert np.allclose(m.tfidf(C), ref)
    assert np.isclose(m.coseno(np.array([1, 0]), np.array([1, 1])), 1 / np.sqrt(2))


def test_bigramas(cargar):
    m = cargar("ej03_ngramas")
    lm = m.Bigramas([["el", "gato"], ["el", "perro"]])
    assert np.isclose(lm.prob("<s>", "el"), 3 / 7)
    assert lm.perplejidad([["el", "gato"]]) < lm.perplejidad([["gato", "el"]])


def test_skipgram(cargar):
    m = cargar("ej04_skipgram")
    assert m.pares_skipgram([0, 1, 2], 1) == [(0, 1), (1, 0), (1, 2), (2, 1)]
    rng = np.random.default_rng(0)
    # dos "temas" que nunca se mezclan: {0..4} y {5..9}
    ids = []
    for _ in range(300):
        base = 0 if rng.random() < 0.5 else 5
        ids += list(base + rng.integers(0, 5, 6))
    E = m.entrenar_sgns(m.pares_skipgram(ids, 2), 10, epocas=2)
    vec = m.mas_similares(E, 0, 3)
    assert all(v < 5 for v in vec)


def test_rnn(cargar):
    m = cargar("ej05_rnn_numpy")
    torch = pytest.importorskip("torch")
    rnn = torch.nn.RNN(3, 4, batch_first=True).double()
    X = torch.randn(1, 5, 3, dtype=torch.float64)
    ref, _ = rnn(X)
    Wx = rnn.weight_ih_l0.detach().numpy().T; Wh = rnn.weight_hh_l0.detach().numpy().T
    b = (rnn.bias_ih_l0 + rnn.bias_hh_l0).detach().numpy()
    assert np.allclose(m.rnn_forward(X[0].numpy(), np.zeros(4), Wx, Wh, b), ref[0].detach().numpy())
    assert m.norma_gradiente_bptt(0.5 * np.eye(3), 20) < 1e-5
    assert m.norma_gradiente_bptt(1.5 * np.eye(3), 20) > 1e3


def test_lstm(cargar):
    m = cargar("ej06_lstm_celda")
    torch = pytest.importorskip("torch")
    cell = torch.nn.LSTMCell(3, 4).double()
    x = torch.randn(3, dtype=torch.float64); h = torch.randn(4, dtype=torch.float64); c = torch.randn(4, dtype=torch.float64)
    h2, c2 = cell(x[None], (h[None], c[None]))
    p = [t.detach().numpy() for t in (cell.weight_ih, cell.weight_hh, cell.bias_ih, cell.bias_hh)]
    hn, cn = m.lstm_paso(x.numpy(), h.numpy(), c.numpy(), *p)
    assert np.allclose(hn, h2[0].detach().numpy()) and np.allclose(cn, c2[0].detach().numpy())


def test_clasificador(cargar):
    torch = pytest.importorskip("torch")
    m = cargar("ej07_clasificador_lstm")
    g = torch.Generator().manual_seed(0)
    X = torch.randint(2, 10, (200, 8), generator=g)
    y = (X == 3).any(1).long()  # ¿aparece el token 3?
    _, acc = m.entrenar(X, y, 10, 2, epocas=60, dispositivo="cpu")
    assert acc > 0.9


def test_bpe(cargar):
    m = cargar("ej08_bpe")
    f = m.entrenar_bpe(["baja", "bajo", "bajar", "baja"], 3)
    assert f[0] == ("a", "j") or f[0] == ("b", "a")
    toks = m.aplicar_bpe("bajo", f)
    assert "".join(toks) == "bajo</w>" and len(toks) < 5
