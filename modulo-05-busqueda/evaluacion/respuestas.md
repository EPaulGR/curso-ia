# Respuestas — Módulo 05

1. Estado (M, C, bote) en la orilla izquierda; inicial (3,3,1); acciones: mover 1–2 personas en el bote; transición: actualizar conteos; meta (0,0,0); costo 1 por viaje; restricción: nunca más caníbales que misioneros en una orilla con misioneros.
2. Nodo = estructura de datos (estado, padre, acción, g); estado = configuración del mundo. Árbol: puede repetir estados; grafo: guarda alcanzados para no repetir.
3. No confiables: se requiere búsqueda en estados de creencia o métodos probabilísticos. Variables: replanificación o búsqueda en tiempo real (LRTA*, D* Lite).
4. 181 440. Solo la mitad de las 9! permutaciones tiene la paridad de inversiones de la meta.
5. ~10⁸ nodos ≈ 100 s y ≈ 100 GB de memoria. La memoria es el cuello de botella.
6. Con costos unitarios, la primera meta generada ya está a la menor profundidad. En UCS un camino más barato podría descubrirse después, así que se espera a que tenga el menor g.
7. $N = \sum_{i=0}^{d}(d+1-i)b^i = b^d(1 + 2/b + 3/b^2 + \dots) \le b^d\,(b/(b-1))^2$.
8. Memoria limitada, muchas soluciones profundas, espacio finito, o cuando no importa la optimalidad.
9. Admisible: $h\le h^*$. Consistente: $h(n)\le c(n,n')+h(n')$. Inducción sobre la longitud del camino óptimo a la meta: $h(n)\le c(n,n_1)+h(n_1)\le\dots\le h^*(n)$.
10. Ver teoría §4: todo nodo n del camino óptimo cumple $f(n)\le C^*$ < $f(G_2)$ para una meta subóptima, así que n se expande antes.
11. Puede devolver soluciones subóptimas. Con w = 1.5: costo ≤ 1.5·C*.
12. h1: la ficha puede saltar a cualquier casilla. h2: puede moverse a una adyacente aunque esté ocupada. Para cada ficha la distancia Manhattan es ≥ 1 si está fuera de lugar.
13. Cada una ≤ h*, así que su máximo también. La suma puede sobreestimar, no es admisible en general.
14. b* ≈ 1.92.
15. Umbral inicial h(raíz); en cada iteración DFS acotado por f ≤ umbral; el nuevo umbral es el mínimo f que lo excedió. Solo guarda el camino actual: O(bd).
16. Dos búsquedas de profundidad d/2: $2b^{d/2}\ll b^d$. Requiere meta explícita y acciones invertibles (predecesores calculables).
17. Tabla con el costo exacto de resolver un subproblema (p. ej. fichas 1–4), precalculada con BFS desde la meta. Es conocimiento previo porque se calcula antes y se consulta.
18. Arad(366) → Sibiu(393) → Rimnicu Vilcea(413) → Fagaras(415) → Pitesti(417) → Bucharest(418).
19. Beam: memoria y tiempo acotados (k nodos por nivel), pero pierde completitud y optimalidad.
20. GPS: A* / contraction hierarchies; videojuego en cuadrícula: A* o JPS; 15-puzzle: IDA* con bases de datos de patrones.
