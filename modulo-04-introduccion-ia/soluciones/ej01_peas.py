"""Ejercicio 01 — Clasificación de entornos (AIMA cap. 2).
Cada entorno se describe con un dict de propiedades booleanas:
observable, determinista, episodico, estatico, discreto, multiagente."""

PROPIEDADES = ("observable", "determinista", "episodico", "estatico", "discreto", "multiagente")


def clasificar(nombre):
    """Devuelve el dict de propiedades para: 'ajedrez_con_reloj', 'taxi', 'crucigrama', 'clasificacion_imagenes'.
    Usa la clasificación de AIMA (ajedrez con reloj: semidinámico -> estatico=False)."""
    tabla = {
        "crucigrama": (True, True, False, True, True, False),
        "ajedrez_con_reloj": (True, True, False, False, True, True),
        "taxi": (False, False, False, False, False, True),
        "clasificacion_imagenes": (True, True, True, True, False, False),
    }
    return dict(zip(PROPIEDADES, tabla[nombre]))


def dificultad(props):
    """Puntaje 0-6: número de propiedades 'difíciles' (lo contrario de cada propiedad fácil; multiagente=True es difícil)."""
    faciles = {k: True for k in PROPIEDADES[:-1]}
    return sum(props[k] != v for k, v in faciles.items()) + int(props["multiagente"])
