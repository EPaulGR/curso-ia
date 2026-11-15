"""Ejercicio 04 — Mini-ELIZA: reglas de patrón-respuesta (IA simbólica, 1966)."""
import re
REFLEJOS = {'yo': 'tú', 'mi': 'tu', 'me': 'te', 'soy': 'eres', 'estoy': 'estás', 'tengo': 'tienes'}
REGLAS = [('me siento (.*)', '¿Por qué te sientes {0}?'), ('estoy (.*)', '¿Desde cuándo estás {0}?'), ('necesito (.*)', '¿Qué significaría para ti obtener {0}?'), ('(.*) madre(.*)', 'Cuéntame más sobre tu familia.'), ('(.*)', 'Entiendo. Continúa, por favor.')]

def reflejar(fragmento):
    """Cambia la persona gramatical palabra por palabra usando REFLEJOS."""
    raise NotImplementedError  # TODO

def responder(frase):
    """Primera regla que haga match (re.fullmatch, insensible a mayúsculas, sin puntuación final)."""
    raise NotImplementedError  # TODO
