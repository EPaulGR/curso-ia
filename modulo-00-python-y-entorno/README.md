# Módulo 00 — Python para IA y entorno Mac

**Duración:** 2–3 semanas (25–35 h) · **Fase 0: Fundamentos** · Prerrequisito de todo el curso

## Objetivos
- Dominar Python idiomático: tipos, comprensiones, funciones de orden superior, generadores, clases, `dataclasses`, typing.
- Programar con NumPy de forma vectorizada (sin bucles) y entender *broadcasting*.
- Manipular datos tabulares con pandas.
- Trabajar con el entorno del curso: `uv`, Jupyter, git, pytest.

## Temario
1. Entorno: `uv`, entornos virtuales, Jupyter, VS Code, git básico.
2. Python esencial: estructuras de datos (`list`, `dict`, `set`, `tuple`, `deque`, `heapq`, `Counter`).
3. Funciones: argumentos, `lambda`, `map/filter`, clausuras, decoradores.
4. Iteradores y generadores (`yield`), `itertools`.
5. POO: clases, herencia, métodos especiales, `@dataclass`.
6. NumPy: `ndarray`, `dtype`, `shape`, indexado, slicing, máscaras booleanas, broadcasting, `axis`, álgebra (`@`).
7. pandas: `Series`, `DataFrame`, `groupby`, `merge`, limpieza de datos faltantes.
8. Visualización con matplotlib.
9. Pruebas con pytest y medición de tiempo (`timeit`).

## Lecturas
- *Python Data Science Handbook* (J. VanderPlas, 🆓 jakevdp.github.io/PythonDataScienceHandbook) — caps. 1–4.
- Documentación oficial NumPy: "NumPy: the absolute basics for beginners" y "Broadcasting".
- Géron, *Hands-On ML* — Cap. 2 (proyecto de ML de punta a punta, como motivación).

## Ejercicios
| Archivo | Tema |
|---|---|
| ej01_estructuras.py | dict, Counter, comprensiones |
| ej02_generadores.py | generadores e itertools |
| ej03_decoradores.py | decoradores y clausuras |
| ej04_clases.py | dataclasses y métodos especiales |
| ej05_numpy_basico.py | indexado, máscaras, broadcasting |
| ej06_numpy_vectorizado.py | distancias y softmax sin bucles |
| ej07_pandas.py | groupby, limpieza |

## Evaluación
- Tests: `pytest modulo-00-python-y-entorno`
- Quiz: `evaluacion/quiz.md`
- Proyecto: `proyecto/README.md`
- Criterio de aprobación: ≥ 8/10 ponderado (ver README raíz).
