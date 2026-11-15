def test_peas(cargar):
    m = cargar("ej01_peas")
    t = m.clasificar("taxi")
    assert not t["observable"] and not t["determinista"] and t["multiagente"]
    assert m.clasificar("crucigrama")["estatico"] and not m.clasificar("ajedrez_con_reloj")["estatico"]
    assert m.clasificar("clasificacion_imagenes")["episodico"]
    assert m.dificultad(t) == 6 and m.dificultad(m.clasificar("crucigrama")) == 1


def test_reactivo(cargar):
    m = cargar("ej02_agente_reactivo")
    assert m.agente_reactivo(("A", "Sucio")) == "Aspirar"
    assert m.agente_reactivo(("A", "Limpio")) == "Derecha"
    assert m.agente_reactivo(("B", "Limpio")) == "Izquierda"
    assert m.simular(m.agente_reactivo, {"A": "Sucio", "B": "Sucio"}, "A", 4) == 1 + 1 + 2 + 2


def test_modelo(cargar):
    m = cargar("ej03_agente_modelo")
    a = m.AgenteModelo()
    acciones = [a(("A", "Sucio")), a(("A", "Limpio")), a(("B", "Limpio")), a(("B", "Limpio"))]
    assert acciones == ["Aspirar", "Derecha", "NoOp", "NoOp"]


def test_eliza(cargar):
    m = cargar("ej04_eliza")
    assert m.responder("Me siento triste por mi trabajo.") == "¿Por qué te sientes triste por tu trabajo?"
    assert m.responder("Necesito vacaciones") == "¿Qué significaría para ti obtener vacaciones?"
    assert m.responder("Hola") == "Entiendo. Continúa, por favor."


def test_perceptron(cargar):
    m = cargar("ej05_perceptron_rosenblatt")
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    w, b, ok = m.entrenar_perceptron(X, [0, 0, 0, 1])
    assert ok and m.predecir(w, b, X).tolist() == [0, 0, 0, 1]
    assert m.entrenar_perceptron(X, [0, 1, 1, 0])[2] is False


def test_evolutivo(cargar):
    m = cargar("ej06_evolutivo_minimo")
    mejor, g = m.uno_mas_uno(30)
    assert m.onemax(mejor) == 30 and g is not None and g < 5000
