import numpy as np

DOCS = [
    "A estrella usa una heurística admisible para encontrar caminos óptimos",
    "La poda alfa beta reduce los nodos explorados por minimax",
    "Los algoritmos genéticos usan selección cruza y mutación",
]


def test_embeddings(cargar):
    m = cargar("ej01_embeddings")
    assert m.tokenizar("Hola, Mundo!") == ["hola", "mundo"]
    vocab, X = m.tf_idf(DOCS)
    assert X.shape == (3, len(vocab)) and np.allclose(np.linalg.norm(X, axis=1), 1)
    vocab, idf = m.calcular_idf(DOCS)
    q = m.vectorizar("poda alfa beta", vocab, idf)
    sims = [m.similitud_coseno(q, x) for x in X]
    assert int(np.argmax(sims)) == 1


def test_indice(cargar):
    m = cargar("ej02_indice_vectorial")
    ix = m.IndiceVectorial()
    ix.agregar("a", [1, 0]); ix.agregar("a2", [0.99, 0.05]); ix.agregar("b", [0.6, 0.8])
    assert ix.buscar([1, 0], 1)[0][0] == "a"
    sel = ix.buscar_mmr([1, 0.1], 2, lambda_=0.3)
    assert sel[0] in ("a", "a2") and sel[1] == "b"  # MMR evita el casi-duplicado


def test_chunking(cargar):
    m = cargar("ej03_chunking")
    t = " ".join(str(i) for i in range(10))
    c = m.chunks_fijos(t, 4, 1)
    assert c[0] == "0 1 2 3" and c[1] == "3 4 5 6" and c[-1].endswith("9")
    assert len(c) == 3
    txt = "a b c\n\nd e\n\nf g h i j"
    assert m.chunks_por_parrafo(txt, 5) == ["a b c\n\nd e", "f g h i j"]


def test_rag(cargar):
    m = cargar("ej04_rag")
    p = m.construir_prompt("¿x?", ["uno", "dos"])
    assert "[1] uno" in p and "[2] dos" in p and "¿x?" in p
    visto = {}
    def llm(prompt):
        visto["p"] = prompt
        return "respuesta [1]"
    r = m.rag("qué hace la poda alfa beta", DOCS, llm, k=1)
    assert r["fuentes"] == [1] and "minimax" in visto["p"]


def test_agente(cargar):
    m = cargar("ej05_agente")
    guion = iter([{"herramienta": "sumar", "args": {"a": 2, "b": 3}},
                  {"herramienta": "nope", "args": {}},
                  {"final": "5"}])
    r = m.ejecutar_agente(lambda msgs: next(guion), {"sumar": lambda a, b: a + b}, "suma")
    assert r["respuesta"] == "5" and r["pasos"] == 2
    assert r["mensajes"][1]["contenido"] == "5"
    assert r["mensajes"][2]["contenido"].startswith("ERROR")
    r2 = m.ejecutar_agente(lambda msgs: {"herramienta": "sumar", "args": {"a": 1, "b": 1}},
                           {"sumar": lambda a, b: a + b}, "x", max_pasos=3)
    assert r2["respuesta"] is None and r2["pasos"] == 3


def test_metricas(cargar):
    m = cargar("ej06_metricas")
    assert m.precision_en_k(["a", "b", "c"], {"a", "c"}, 2) == 0.5
    assert m.recall_en_k(["a", "b", "c"], {"a", "c"}, 3) == 1
    assert np.isclose(m.mrr([["x", "a"], ["a"]], [{"a"}, {"a"}]), 0.75)
    assert np.isclose(m.ndcg_en_k(["a", "b"], {"a": 3, "b": 1}, 2), 1)
    assert m.ndcg_en_k(["b", "a"], {"a": 3, "b": 1}, 2) < 1
    assert m.exact_match("El Gato.", "el gato")
    assert np.isclose(m.f1_tokens("el gato negro", "el gato"), 0.8)
