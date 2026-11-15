# Teoría — Python para IA

## 1. Por qué Python domina la IA
Python es lento como intérprete, pero en IA casi todo el cómputo ocurre dentro de librerías escritas en C/C++/Metal (NumPy, PyTorch, MLX). Python es el "pegamento". Regla: **si escribes un bucle `for` sobre millones de números en Python puro, lo estás haciendo mal** — vectoriza.

## 2. Estructuras de datos clave
| Estructura | Uso en IA | Complejidad |
|---|---|---|
| `list` | secuencias, pilas (`append/pop`) | acceso O(1), `insert(0)` O(n) |
| `collections.deque` | colas FIFO (BFS) | `append/popleft` O(1) |
| `heapq` | cola de prioridad (UCS, A*) | `push/pop` O(log n) |
| `dict` / `set` | conjuntos de visitados, tablas hash | O(1) promedio |
| `Counter` | frecuencias de palabras, conteos | O(n) construir |

Los estados que se meten en `set` o como llaves de `dict` deben ser **inmutables (hashables)**: usa `tuple`, `frozenset`, no `list`.

## 3. Comprensiones y funciones de orden superior
```python
cuadrados = [x*x for x in range(10) if x % 2 == 0]
indice = {palabra: i for i, palabra in enumerate(vocab)}
sorted(personas, key=lambda p: p.edad)
```

## 4. Generadores
Un generador produce valores perezosamente: memoria O(1). Ideal para leer datasets enormes o generar sucesores en búsqueda.
```python
def lotes(datos, n):
    for i in range(0, len(datos), n):
        yield datos[i:i+n]
```

## 5. Decoradores
Un decorador es una función que recibe una función y devuelve otra. Se usa en caché (`functools.lru_cache`, clave en programación dinámica y búsqueda), medición de tiempo, registro.

## 6. NumPy
- `a.shape`, `a.dtype`, `a.ndim`. Un vector de *n* es `(n,)`; una matriz *m×n* es `(m, n)`.
- **Broadcasting**: se alinean las dimensiones desde la derecha; dos dimensiones son compatibles si son iguales o una vale 1.
  - `(m, n) + (n,)` → suma el vector a cada fila.
  - `(m, 1) - (1, k)` → matriz `(m, k)` de todas las diferencias.
- `axis=0` reduce filas (resultado por columna); `axis=1` reduce columnas (por fila).
- Distancia euclidiana entre todos los pares (X: m×d, Y: k×d):
  $$\|x-y\|^2 = \|x\|^2 + \|y\|^2 - 2x\cdot y$$
- Softmax numéricamente estable: $\text{softmax}(z)_i = \frac{e^{z_i - \max z}}{\sum_j e^{z_j - \max z}}$ (restar el máximo evita overflow).

## 7. pandas
```python
df = pd.read_csv("datos.csv")
df["edad"].fillna(df["edad"].median())
df.groupby("ciudad")["ingreso"].agg(["mean", "count"])
```

## 8. Buenas prácticas
- Funciones pequeñas, puras y probadas.
- Fija semillas (`np.random.default_rng(42)`) para reproducibilidad.
- Mide antes de optimizar (`%timeit`).
