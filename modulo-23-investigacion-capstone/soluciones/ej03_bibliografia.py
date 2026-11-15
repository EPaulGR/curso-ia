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
        self.p[clave] = dict(titulo=titulo, autores=autores, anio=anio, etiquetas=set(etiquetas), citas=list(citas))

    def por_etiqueta(self, etiqueta):
        return sorted((k for k, v in self.p.items() if etiqueta in v["etiquetas"]), key=lambda k: self.p[k]["anio"])

    def ruta_lectura(self, clave):
        orden, visto = [], set()
        def visitar(k):
            if k in visto or k not in self.p:
                return
            visto.add(k)
            for c in sorted(self.p[k]["citas"], key=lambda c: self.p.get(c, {"anio": 0})["anio"]):
                visitar(c)
            orden.append(k)
        visitar(clave)
        return orden

    def bibtex(self, clave):
        v = self.p[clave]
        return (f"@article{{{clave},\n  title={{{v['titulo']}}},\n"
                f"  author={{{' and '.join(v['autores'])}}},\n  year={{{v['anio']}}}\n}}")
