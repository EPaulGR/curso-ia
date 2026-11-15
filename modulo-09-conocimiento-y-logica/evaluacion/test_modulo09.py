"""Tests del módulo 09."""

# Mundo de wumpus simplificado (AIMA 7.4.3)
KB = ("y", ("no", "P11"), ("y", ("sii", "B11", ("o", "P12", "P21")),
      ("y", ("sii", "B21", ("o", "P11", ("o", "P22", "P31"))), ("y", ("no", "B11"), "B21"))))


def test_semantica(cargar):
    m = cargar("ej01_logica_proposicional")
    assert m.evaluar(("implica", "p", "q"), {"p": False, "q": False})
    assert m.simbolos(KB) == {"P11", "B11", "P12", "P21", "B21", "P22", "P31"}
    assert m.tt_implica(KB, ("no", "P12")) and not m.tt_implica(KB, "P22")
    assert m.es_tautologia(("o", "p", ("no", "p")))
    assert not m.es_satisfacible(("y", "p", ("no", "p")))


def test_fnc_resolucion(cargar):
    m = cargar("ej02_fnc_resolucion")
    cl = m.a_clausulas(("sii", "B11", ("o", "P12", "P21")))
    assert cl == {frozenset({"-B11", "P12", "P21"}), frozenset({"-P12", "B11"}), frozenset({"-P21", "B11"})}
    assert m.resolver(frozenset({"p", "q"}), frozenset({"-p", "r"})) == {frozenset({"q", "r"})}
    assert m.resolucion(KB, ("no", "P12"))
    assert not m.resolucion(KB, "P22")


def test_dpll(cargar):
    d = cargar("ej03_dpll").dpll
    cls = [[1, 2], [-1, 3], [-2, -3], [2, 3]]
    mod = d(cls)
    assert all(any(mod[abs(l)] == (l > 0) for l in c) for c in cls)
    assert d([[1], [-1]]) is None
    # palomar: 3 palomas en 2 agujeros (insatisfacible). x_{p,h} = 2p+h+1
    v = lambda p, h: 2 * p + h + 1
    ph = [[v(p, 0), v(p, 1)] for p in range(3)]
    ph += [[-v(p, h), -v(q, h)] for h in range(2) for p in range(3) for q in range(p + 1, 3)]
    assert d(ph) is None


def test_encadenamiento(cargar):
    m = cargar("ej04_encadenamiento")
    # AIMA fig. 7.16
    R = [(["P"], "Q"), (["L", "M"], "P"), (["B", "L"], "M"), (["A", "P"], "L"),
         (["A", "B"], "L"), ([], "A"), ([], "B")]
    ok, inf = m.encadenamiento_adelante(R, "Q")
    assert ok and inf == {"A", "B", "L", "M", "P", "Q"}
    assert m.encadenamiento_atras(R, "Q") and not m.encadenamiento_atras(R, "Z")


def test_unificacion(cargar):
    m = cargar("ej05_unificacion")
    th = m.unificar(("conoce", "juan", "?x"), ("conoce", "?y", ("madre", "?y")))
    assert m.sustituir("?x", th) == ("madre", "juan") and m.sustituir("?y", th) == "juan"
    assert m.unificar(("conoce", "juan", "?x"), ("conoce", "?x", "isabel")) is None
    assert m.unificar("?x", ("f", "?x")) is None
    assert m.unificar(("p", "?x", "?x"), ("p", "a", "?z")) is not None


def test_sistema_experto(cargar):
    m = cargar("ej06_sistema_experto")
    H = {("padre", "ana", "luis"), ("padre", "luis", "eva"), ("padre", "eva", "teo")}
    R = [([("padre", "?x", "?y")], ("ancestro", "?x", "?y")),
         ([("padre", "?x", "?y"), ("ancestro", "?y", "?z")], ("ancestro", "?x", "?z"))]
    todos = m.encadenamiento_adelante_fol(H, R)
    assert ("ancestro", "ana", "teo") in todos and len([h for h in todos if h[0] == "ancestro"]) == 6
    resp = sorted(r["?q"] for r in m.consultar(("ancestro", "ana", "?q"), H, R))
    assert resp == ["eva", "luis", "teo"]
    pasos = m.explicar(("ancestro", "luis", "teo"), H, R)
    assert pasos[-1][1] == ("ancestro", "luis", "teo")
