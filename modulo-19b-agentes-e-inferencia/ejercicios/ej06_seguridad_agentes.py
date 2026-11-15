"""Ejercicio 06 — Seguridad de agentes.

1. detectar_inyeccion(texto) -> bool: heurística (no suficiente en producción)
   que marca contenido externo con frases típicas de prompt injection:
   "ignora las instrucciones", "ignore previous instructions", "system prompt",
   "eres ahora", "you are now", "envía", "send ... to" etc. Insensible a mayúsculas.
2. envolver_no_confiable(texto, fuente): "spotlighting": encierra el texto en
   <datos_no_confiables fuente="..."> ... </datos_no_confiables>, eliminando
   cualquier etiqueta de cierre falsa que venga dentro del texto.
3. PoliticaPermisos(permitidas, con_confirmacion).autorizar(nombre, confirmado=False)
   -> "permitir" | "confirmar" | "denegar" (denegar por defecto: allowlist).
4. ruta_segura(ruta, raiz) -> bool: True solo si la ruta resuelta queda dentro
   de raiz (evita ../ y rutas absolutas fuera del sandbox).
"""
import re
from pathlib import Path

PATRONES = [
    r"ignora (todas )?(las )?instrucciones", r"ignore (all )?(previous|prior) instructions",
    r"system prompt", r"prompt del sistema", r"eres ahora", r"you are now",
    r"env[ií]a .* a ", r"send .* to ", r"olvida (todo|lo anterior)",
]


def detectar_inyeccion(texto):
    raise NotImplementedError  # TODO


def envolver_no_confiable(texto, fuente):
    raise NotImplementedError  # TODO


class PoliticaPermisos:
    def __init__(self, permitidas, con_confirmacion=()):
        self.permitidas = set(permitidas)
        self.con_confirmacion = set(con_confirmacion)

    def autorizar(self, nombre, confirmado=False):
        raise NotImplementedError  # TODO


def ruta_segura(ruta, raiz):
    raise NotImplementedError  # TODO
