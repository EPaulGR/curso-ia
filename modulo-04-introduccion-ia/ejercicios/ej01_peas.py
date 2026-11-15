"""Ejercicio 01 — Clasificación de entornos (AIMA cap. 2).
Cada entorno se describe con un dict de propiedades booleanas:
observable, determinista, episodico, estatico, discreto, multiagente."""
PROPIEDADES = ('observable', 'determinista', 'episodico', 'estatico', 'discreto', 'multiagente')

def clasificar(nombre):
    """Devuelve el dict de propiedades para: 'ajedrez_con_reloj', 'taxi', 'crucigrama', 'clasificacion_imagenes'.
Usa la clasificación de AIMA (ajedrez con reloj: semidinámico -> estatico=False)."""
    raise NotImplementedError  # TODO

def dificultad(props):
    """Puntaje 0-6: número de propiedades 'difíciles' (lo contrario de cada propiedad fácil; multiagente=True es difícil)."""
    raise NotImplementedError  # TODO
