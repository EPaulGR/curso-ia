"""Ejercicio 3 — Gestor mínimo de lecturas (papers).

Clase `Biblioteca`:
- `agregar(clave, titulo, autores: list, anio, etiquetas: set, citas=())`: `citas` son claves
  de otros papers que este cita.
- `por_etiqueta(etiqueta)`: claves ordenadas por año.
- `ruta_lectura(clave)`: orden topológico de los ancestros (papers citados, recursivamente,
  que estén en la biblioteca) terminando en `clave`: lee primero lo que se cita. Desempate por año.
- `bibtex(clave)`: "@article{clave,\n  title={...},\n  author={A and B},\n  year={...}\n}".
"""


class Biblioteca:

    def __init__(self):
        self.p = {}

    def agregar(self, clave, titulo, autores, anio, etiquetas, citas=()):
        raise NotImplementedError  # TODO: implementa esta función

    def por_etiqueta(self, etiqueta):
        raise NotImplementedError  # TODO: implementa esta función

    def ruta_lectura(self, clave):
        raise NotImplementedError  # TODO: implementa esta función

    def bibtex(self, clave):
        raise NotImplementedError  # TODO: implementa esta función
