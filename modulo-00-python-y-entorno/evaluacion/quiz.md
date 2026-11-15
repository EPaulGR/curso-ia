# Quiz — Módulo 00

1. ¿Por qué una lista no puede ser llave de un `dict`? ¿Qué usarías en su lugar para representar un estado?
2. ¿Qué estructura usarías para una cola FIFO eficiente y por qué no `list.pop(0)`?
3. ¿Qué complejidad tienen `heapq.heappush` y `heapq.heappop`?
4. Explica la diferencia entre una lista por comprensión y una expresión generadora. ¿Cuándo prefieres cada una?
5. ¿Qué imprime `list(zip([1,2,3], "ab"))`?
6. ¿Qué hace `functools.lru_cache` y en qué algoritmo de IA lo aplicarías?
7. Escribe un decorador que imprima el tiempo de ejecución de una función.
8. ¿Qué significa `frozen=True` en un `@dataclass` y por qué es útil para estados de búsqueda?
9. Dado `A.shape == (4, 1)` y `B.shape == (3,)`, ¿cuál es la forma de `A + B`? Explica la regla de broadcasting.
10. ¿Qué devuelve `X.mean(axis=0)` para `X` de forma (100, 5)?
11. ¿Por qué se resta el máximo al calcular softmax?
12. Deriva la identidad ‖x−y‖² = ‖x‖² + ‖y‖² − 2x·y y explica por qué permite calcular distancias sin bucles.
13. ¿Diferencia entre `a.copy()` y `a.view()` / slicing en NumPy? Da un ejemplo de bug por no copiar.
14. ¿Qué hace `df.groupby("c")["v"].agg(["mean","count"])`?
15. ¿Por qué se fijan semillas aleatorias en experimentos de IA?
16. ¿Qué ventaja tiene `uv` sobre instalar paquetes con `pip` global?
17. Opción múltiple: ¿cuál es O(1) promedio? (a) `x in lista` (b) `x in conjunto` (c) `lista.index(x)` (d) `sorted(lista)`
