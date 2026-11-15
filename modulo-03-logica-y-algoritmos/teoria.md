# Teoría — Lógica y algoritmos

## 1. Lógica proposicional
Conectivos: ¬, ∧, ∨, →, ↔. $p\to q \equiv \neg p\lor q$.
- **Tautología:** verdadera en todo modelo. **Satisfacible:** verdadera en al menos uno. **Contradicción:** en ninguno.
- **Consecuencia lógica:** $KB\models\alpha$ ⇔ $KB\land\neg\alpha$ es insatisfacible.
- De Morgan: $\neg(p\land q)\equiv\neg p\lor\neg q$.
- **CNF:** conjunción de cláusulas (disyunciones de literales). Toda fórmula tiene CNF equivalente.
- **Resolución:** de $(a\lor p)$ y $(b\lor\neg p)$ se infiere $(a\lor b)$. Es completa para refutación.

### DPLL
```
DPLL(cláusulas, asignación):
  simplificar con asignación; si alguna cláusula vacía → FALSO; si no quedan → VERDADERO
  propagación unitaria: cláusula de un literal → asígnalo
  literal puro: aparece con una sola polaridad → asígnalo
  elegir variable x: DPLL(x=V) or DPLL(x=F)
```
Los SAT solvers modernos (CDCL) resuelven millones de variables; se usan en verificación y planificación.

## 2. Complejidad
- $f\in O(g)$ si ∃ c, n₀: $f(n)\le c\,g(n)$ ∀ n ≥ n₀.
- Teorema maestro para $T(n) = aT(n/b)+f(n)$: compara $f$ con $n^{\log_b a}$.
- **P:** resolubles en tiempo polinomial. **NP:** soluciones verificables en tiempo polinomial. **NP-completo:** en NP y todo NP se reduce a él (SAT — Cook-Levin, TSP de decisión, mochila, coloreo).
- Implicación para IA: muchos problemas de la Unidad 2 y 4 de la BUAP son NP-difíciles → búsqueda heurística y metaheurísticas.

## 3. Estructuras de datos
| Estructura | Operaciones | Uso |
|---|---|---|
| Pila (LIFO) | push/pop O(1) | DFS, backtracking |
| Cola (FIFO) | enqueue/dequeue O(1) | BFS |
| Heap binario | push/pop O(log n), peek O(1) | UCS, A*, Dijkstra |
| Hash | O(1) promedio | conjunto de visitados |
| Union-Find | casi O(1) amortizado | Kruskal, componentes |

Heap en arreglo: hijos de i en 2i+1, 2i+2; padre en (i−1)//2. *sift-up* al insertar, *sift-down* al extraer.

## 4. Grafos
- BFS: caminos mínimos en número de aristas, O(V+E).
- DFS: detección de ciclos, orden topológico (Kahn: ir quitando nodos con grado de entrada 0).
- **Dijkstra:** pesos no negativos, O((V+E) log V) con heap. A* (módulo 05) es Dijkstra + heurística.
- Kruskal: ordenar aristas, añadir si no forma ciclo (union-find).

## 5. Programación dinámica
Subestructura óptima + subproblemas solapados. Mochila 0/1: $V[i][w] = \max(V[i-1][w], v_i + V[i-1][w-w_i])$, O(nW) (pseudo-polinomial). Distancia de edición: $D[i][j] = \min(D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+[a_i\ne b_j])$.

## 6. Backtracking
Explorar asignaciones parciales y retroceder al violar restricciones. Base de la búsqueda en CSP (módulo 08).
