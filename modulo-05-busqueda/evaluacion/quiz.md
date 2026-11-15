# Quiz — Módulo 05 (Unidad 2 BUAP)

1. Enumera los 5 componentes de la formulación de un problema y aplícalos al problema de los misioneros y caníbales.
2. ¿Diferencia entre nodo y estado? ¿Entre búsqueda en árbol y en grafo?
3. ¿Cómo afectan los datos no confiables y variables en el tiempo a la elección de la estrategia de búsqueda?
4. ¿Cuántos estados alcanzables tiene el 8-puzzle y por qué es 9!/2?
5. Con b = 10, d = 8, 1 µs por nodo y 1 KB por nodo, estima tiempo y memoria de BFS.
6. ¿Por qué BFS hace la prueba de meta al generar y UCS al extraer?
7. Demuestra que IDDFS tiene complejidad temporal $O(b^d)$ pese a regenerar nodos.
8. ¿En qué casos DFS es preferible a BFS?
9. Define heurística admisible y consistente. Demuestra que consistente ⇒ admisible.
10. Demuestra que A* con h admisible (búsqueda en árbol) es óptimo.
11. ¿Qué pasa si h sobreestima? ¿Qué garantiza weighted A* con w = 1.5?
12. Deriva h1 (fuera de lugar) y h2 (Manhattan) como problemas relajados. ¿Por qué h2 domina a h1?
13. ¿Por qué max(h1, h2) es admisible? ¿Y h1 + h2?
14. Calcula el factor de ramificación efectivo si A* genera 52 nodos y la solución está a profundidad 5.
15. Explica IDA*: ¿cómo se actualiza el umbral y por qué usa memoria lineal?
16. ¿Por qué la búsqueda bidireccional reduce el costo a $O(b^{d/2})$? ¿Qué requisitos tiene?
17. ¿Qué es una base de datos de patrones? ¿Por qué es "conocimiento previo" (2.2.2)?
18. Traza A* desde Arad a Bucharest con la distancia en línea recta. ¿Qué nodo se expande en cada paso?
19. Compara beam search con A*: ¿qué se gana y qué se pierde?
20. Menciona tres aplicaciones prácticas de búsqueda (2.6) y qué algoritmo usarías en cada una.
