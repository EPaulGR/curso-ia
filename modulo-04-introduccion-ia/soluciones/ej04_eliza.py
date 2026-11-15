"""Ejercicio 04 — Mini-ELIZA: reglas de patrón-respuesta (IA simbólica, 1966)."""
import re

REFLEJOS = {"yo": "tú", "mi": "tu", "me": "te", "soy": "eres", "estoy": "estás", "tengo": "tienes"}

REGLAS = [
    (r"me siento (.*)", "¿Por qué te sientes {0}?"),
    (r"estoy (.*)", "¿Desde cuándo estás {0}?"),
    (r"necesito (.*)", "¿Qué significaría para ti obtener {0}?"),
    (r"(.*) madre(.*)", "Cuéntame más sobre tu familia."),
    (r"(.*)", "Entiendo. Continúa, por favor."),
]


def reflejar(fragmento):
    """Cambia la persona gramatical palabra por palabra usando REFLEJOS."""
    return " ".join(REFLEJOS.get(p, p) for p in fragmento.lower().split())


def responder(frase):
    """Primera regla que haga match (re.fullmatch, insensible a mayúsculas, sin puntuación final)."""
    frase = frase.strip().rstrip(".!?").lower()
    for patron, plantilla in REGLAS:
        m = re.fullmatch(patron, frase)
        if m:
            return plantilla.format(*[reflejar(g) for g in m.groups()])
