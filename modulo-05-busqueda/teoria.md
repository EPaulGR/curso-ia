# Teoría — Problemas de búsqueda (Unidad 2)

## 1. Formulación de un problema
Un problema de búsqueda se define con:
1. **Estado inicial** $s_0$
2. **Acciones** $A(s)$
3. **Modelo de transición** $\text{RESULT}(s,a)$
4. **Prueba de meta**
5. **Costo de acción** $c(s,a,s')$

Una **solución** es una secuencia de acciones que lleva de $s_0$ a una meta; es **óptima** si tiene costo mínimo.

### Tipos de datos (2.1.1)
- *Confiables:* el modelo es exacto (puzzles) → búsqueda clásica.
- *No confiables:* percepciones con ruido → búsqueda en espacios de creencias, POMDP (módulo 10/20).
- *Variables en el tiempo:* entorno dinámico → replanificación, búsqueda en tiempo real (LRTA*, D* Lite).

### Nodo vs estado (2.1.2)
Un **nodo** contiene: estado, padre, acción, costo de camino g. Varios nodos pueden tener el mismo estado. **Frontera** = nodos generados sin expandir; **alcanzados/explorados** = conjunto para evitar repetidos (búsqueda en grafo).

### Complejidad (2.1.3)
b = factor de ramificación, d = profundidad de la solución más superficial, m = profundidad máxima.

| Algoritmo | Completo | Óptimo | Tiempo | Espacio |
|---|---|---|---|---|
| BFS | Sí (b finito) | Sí (costos iguales) | $O(b^d)$ | $O(b^d)$ |
| UCS | Sí (costos ≥ ε) | Sí | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | igual |
| DFS | No (espacios infinitos) | No | $O(b^m)$ | $O(bm)$ |
| DLS (límite ℓ) | No | No | $O(b^\ell)$ | $O(b\ell)$ |
| IDDFS | Sí | Sí (costos iguales) | $O(b^d)$ | $O(bd)$ |
| Bidireccional | Sí | Sí | $O(b^{d/2})$ | $O(b^{d/2})$ |
| Voraz | No | No | $O(b^m)$ | $O(b^m)$ |
| A* | Sí | Sí (h admisible/consistente) | exponencial en el peor caso | todo en memoria |
| IDA* | Sí | Sí (h admisible) | depende | $O(bd)$ |

Con b = 10 y d = 12, BFS genera ~10¹² nodos: el crecimiento exponencial es el enemigo central.

## 2. Algoritmo genérico (best-first)
```
BEST-FIRST(problema, f):
  nodo ← NODO(s0); frontera ← cola de prioridad por f con nodo
  alcanzados ← {s0: nodo}
  mientras frontera no vacía:
     nodo ← POP(frontera)
     si META(nodo.estado): devolver nodo
     para cada hijo en EXPANDIR(nodo):
        s ← hijo.estado
        si s ∉ alcanzados o hijo.g < alcanzados[s].g:
           alcanzados[s] ← hijo; PUSH(frontera, hijo)
  devolver FALLA
```
- f = g → **UCS**; f = h → **voraz**; f = g + h → **A***; f = g + w·h → **weighted A***; f = profundidad → BFS.

## 3. Funciones de evaluación (2.2)
- $g(n)$: costo real del camino desde el inicio.
- $h(n)$: estimación del costo hasta la meta.
- $f(n) = g(n) + h(n)$: costo estimado de la mejor solución que pasa por n.
- **Admisible:** $h(n)\le h^*(n)$ (nunca sobreestima). ⇒ A* en árbol es óptimo.
- **Consistente (monótona):** $h(n)\le c(n,a,n') + h(n')$. ⇒ f no decrece a lo largo de un camino; A* en grafo es óptimo sin reabrir nodos. Consistente ⇒ admisible.
- **Dominancia:** si $h_2(n)\ge h_1(n)$ ∀n (ambas admisibles), $h_2$ expande ≤ nodos.
- **Problemas relajados:** quitar restricciones da heurísticas admisibles. 8-puzzle: si una ficha puede moverse a cualquier casilla → *piezas fuera de lugar* $h_1$; si puede moverse a casilla adyacente aunque esté ocupada → *distancia Manhattan* $h_2$.
- **Conflicto lineal:** Manhattan + 2 por cada par de fichas en su fila/columna meta pero invertidas (sigue siendo admisible).
- **Bases de datos de patrones (conocimiento previo):** costo exacto de resolver un subconjunto de fichas, precalculado con BFS hacia atrás.
- $\max(h_1,h_2)$ de heurísticas admisibles es admisible.

### Factor de ramificación efectivo
Si A* genera N nodos con solución a profundidad d: $N + 1 = 1 + b^* + (b^*)^2 + \dots + (b^*)^d$. Cuanto más cercano a 1, mejor la heurística.

## 4. Estrategias (2.3)
### BFS
Frontera FIFO; prueba de meta al **generar** (detección temprana). Óptimo para costos unitarios.

### DFS, DLS, IDDFS
DFS: frontera LIFO. DLS: corta en profundidad ℓ (devuelve "corte" vs "falla"). IDDFS: DLS con ℓ = 0, 1, 2, …; regenera niveles superiores pero el costo es dominado por el último nivel: $\sum_{i=0}^d (d+1-i)b^i = O(b^d)$.

### UCS
Expande el nodo de menor g; prueba de meta al **extraer** (si no, no es óptimo).

### A*
Óptimo y *óptimamente eficiente* entre algoritmos que usan la misma h consistente: expande todos los nodos con $f < C^*$ y ninguno con $f > C^*$.

**Prueba de optimalidad (idea):** sea $n$ un nodo en el camino óptimo en la frontera; $f(n) = g(n) + h(n)\le g(n) + h^*(n) = C^*$. Una meta subóptima G₂ tiene $f(G_2) = g(G_2) > C^*$, así que $n$ se expande antes que G₂.

### IDA*
```
IDA*(raíz):
  umbral ← h(raíz)
  repetir:
    t ← BUSCAR(raíz, 0, umbral)
    si t = ENCONTRADO: devolver camino
    si t = ∞: devolver FALLA
    umbral ← t           # mínimo f que excedió el umbral
BUSCAR(n, g, umbral):
  f ← g + h(n); si f > umbral: devolver f
  si META(n): devolver ENCONTRADO
  min ← ∞
  para cada hijo s (evitando ciclos en el camino actual):
     t ← BUSCAR(s, g + c(n,s), umbral)
     si t = ENCONTRADO: devolver ENCONTRADO
     min ← mín(min, t)
  devolver min
```
Memoria lineal; ideal para el 15-puzzle.

### 2.3.5 Nuevas técnicas
- **Bidireccional:** dos frentes (desde inicio y meta); se detiene cuando se tocan. $O(b^{d/2})$.
- **Weighted A*:** $f = g + w h$, $w>1$; solución con costo ≤ $w\cdot C^*$, mucho más rápido.
- **Beam search:** conserva solo los k mejores nodos por nivel (usado en decodificación de LLMs).
- **RBFS / SMA*:** A* con memoria acotada.
- **Jump Point Search:** poda simetrías en cuadrículas uniformes.
- **LRTA*:** búsqueda en tiempo real que aprende h al moverse.

## 5. Reducción del espacio (2.4)
- Conjunto de alcanzados (búsqueda en grafo vs árbol).
- Evitar ciclos en el camino actual (DFS/IDA*).
- **Paridad:** un estado del 8-puzzle es resoluble si el número de inversiones (ignorando el 0) es par → solo la mitad de las 9! permutaciones es alcanzable.
- Simetrías, macro-operadores, abstracción jerárquica.

## 6. Calidad de resultados (2.5)
Heurísticas más informadas (dominancia), combinación por máximo, refinamiento anytime (ARA*: weighted A* con w decreciente).

## 7. Aplicaciones (2.6)
GPS y mapas (A* con distancia geodésica, Contraction Hierarchies), videojuegos (A*/JPS en cuadrículas, navmesh), robótica (A*, RRT), plegado de proteínas, diseño de chips, decodificación de secuencias (beam search).
