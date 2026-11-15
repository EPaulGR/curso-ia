# Respuestas — Módulo 00

1. Las listas son mutables y no hashables; su hash podría cambiar. Usa `tuple` o `frozenset`.
2. `collections.deque`: `popleft` es O(1); `list.pop(0)` es O(n) porque desplaza todos los elementos.
3. O(log n) ambas.
4. La comprensión crea toda la lista en memoria; el generador produce valores bajo demanda (O(1) memoria). Generador para flujos grandes o cuando solo iteras una vez.
5. `[(1, 'a'), (2, 'b')]` — zip se corta en el más corto.
6. Memoriza resultados por argumentos; programación dinámica, heurísticas costosas, tablas de transposición en juegos.
7. `def tiempo(f):\n  @wraps(f)\n  def g(*a, **k):\n    t=time.perf_counter(); r=f(*a, **k); print(time.perf_counter()-t); return r\n  return g`
8. Hace la instancia inmutable y genera `__hash__`; así se puede meter en `set` de visitados.
9. (4, 3). Se alinean dimensiones desde la derecha: 1 vs 3 → 3; 4 vs (ausente→1) → 4.
10. Un vector (5,) con la media de cada columna.
11. Para evitar overflow de `exp`; el resultado no cambia porque el factor e^{-max} se cancela.
12. ‖x−y‖² = (x−y)·(x−y) = x·x − 2x·y + y·y. Los términos ‖x‖² y ‖y‖² se calculan por fila y x·y es un producto matricial `X @ Y.T`.
13. Slicing devuelve una vista que comparte memoria; modificarla altera el original. `b = a[:2]; b[0]=99` cambia `a`.
14. Agrupa por `c` y calcula media y número de valores no nulos de `v` por grupo.
15. Reproducibilidad: poder comparar experimentos y depurar.
16. Entornos aislados por proyecto, resolución de dependencias rápida y reproducible.
17. (b).
