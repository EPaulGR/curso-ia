# Respuestas — Quiz módulo 07
1. Guarda solo el estado actual (memoria O(1)), no garantiza optimalidad, sirve para espacios enormes/continuos y cuando importa la solución, no el camino.
2. Óptimo local: ningún vecino mejora. Meseta: región plana de igual f. Cresta: secuencia de óptimos locales difícil de recorrer con movimientos simples.
3. Promediado sobre todas las funciones, todos los algoritmos rinden igual → hay que incorporar conocimiento del problema.
4. Δ = d(a,c) + d(b,d) − d(a,b) − d(c,d), quitando (a,b) y (c,d).
5. e^{-2} ≈ 0.135; e^{-0.2} ≈ 0.819.
6. T0 pequeño ≈ hill climbing (se atasca). Enfriamiento rápido: se congela en un óptimo local ("templado").
7. Permite un movimiento tabú si produce una solución mejor que la mejor conocida.
8. Intensificar: explorar a fondo regiones prometedoras. Diversificar: llevar la búsqueda a regiones poco exploradas.
9. Ruleta depende de la escala de f (superindividuos dominan, o presión nula si f similares); torneo depende solo del orden y la presión se controla con k.
10. Produce repeticiones/omisiones de ciudades. OX: copiar un segmento del padre 1 y rellenar el resto con el orden relativo del padre 2.
11. m(H,t+1) ≥ m(H,t)·f(H)/f̄·[1 − p_c·δ(H)/(L−1) − o(H)·p_m].
12. Ver teoria §5. α pondera la feromona (experiencia colectiva) y β la heurística (codicia por distancia).
13. Estancamiento prematuro: acota τ en [τmin, τmax] e inicializa en τmax.
14. Los buenos anticuerpos se refinan (explotación) y los malos exploran más.
15. Lamarckiana: la mejora local se hereda (cambia el genotipo). Baldwiniana: solo cambia la aptitud usada para la selección.
16. F1 = {(1,5),(2,3),(4,1)}, F2 = {(3,4)}, F3 = {(5,5)}.
17. Solo halla puntos en la envolvente convexa del frente.
18. Mide qué tan aislado está un punto dentro de su frente (suma de distancias normalizadas a sus vecinos por objetivo); preferir mayor crowding mantiene diversidad a lo largo del frente.
