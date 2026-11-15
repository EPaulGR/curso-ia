# Respuestas — Módulo 03

1. Solo es falsa con p=V, q=F. Con p falsa la implicación se cumple "vacuamente": no hay promesa rota.
2. $p\to q \equiv \neg p\lor q \equiv q\lor\neg p \equiv \neg(\neg q)\lor\neg p \equiv \neg q\to\neg p$.
3. Válida: verdadera en todo modelo. Satisfacible: en al menos uno.
4. Mostrando que $KB\land\neg\alpha$ es insatisfacible (p. ej. derivando la cláusula vacía por resolución).
5. $\neg(p\land q)\lor r \equiv \neg p\lor\neg q\lor r$.
6. $(a\lor c)$.
7. Una cláusula con un solo literal obliga su valor; un literal que solo aparece con una polaridad puede ponerse verdadero sin perder soluciones.
8. Fue el primer problema probado NP-completo (Cook–Levin); todo NP se reduce a SAT.
9. P: decidibles en tiempo polinomial; NP: verificables en tiempo polinomial; NP-completo: en NP y NP-difícil. El crecimiento exponencial supera cualquier mejora constante de hardware.
10. $a=2,b=2$, $n^{\log_2 2}=n = f(n)$ ⇒ $\Theta(n\log n)$.
11. BFS expande por niveles (FIFO): completo y óptimo con costos unitarios. DFS va a profundidad (LIFO): no completo en espacios infinitos, no óptimo, pero memoria lineal.
12. Asume que una vez extraído un nodo su distancia es final; una arista negativa posterior podría mejorarla.
13. O((V+E) log V).
14. Compresión de caminos y unión por rango/tamaño.
15. W no es polinomial en el tamaño de la entrada (se codifica con log W bits): es pseudo-polinomial.
16. Subestructura óptima y subproblemas solapados.
17. Backtracking poda ramas en cuanto una asignación parcial viola restricciones.
18. TSP, mochila, coloreo de grafos, planificación de horarios, 8-puzzle generalizado (n²−1).
