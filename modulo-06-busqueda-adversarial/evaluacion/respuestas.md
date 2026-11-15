# Respuestas — Quiz módulo 06
1. La suma de utilidades de los jugadores es constante en todo terminal. No suma cero: dilema del prisionero.
2. Ver teoria §2.
3. Tiempo O(b^m), espacio O(bm) (DFS).
4. Falso: el valor de la raíz es idéntico; solo puede elegir otra jugada igual de buena si hay empates y el desempate depende del orden.
5. α: mejor valor asegurado para MAX en el camino; β: para MIN. En un nodo MIN se poda cuando v ≤ α.
6. O(b^{m/2}); se puede buscar aproximadamente el doble de profundo con el mismo cómputo.
7. Valor 3. Primer MIN = 3. Segundo MIN: tras ver 2 (≤ α=3) se podan 4 y 6. Tercer MIN: 14, 5, 2 → se evalúan todos (2 ≤ 3 solo al final). Raíz = 3.
8. Ordena terminales como la utilidad; es eficiente; correlaciona con la probabilidad de ganar (y, para azar, es lineal en ella).
9. Una pérdida inevitable se retrasa más allá del corte y la búsqueda no la ve. Quiescencia: extender solo en posiciones "no quietas" (capturas, jaques) hasta estabilizar.
10. Se busca a d=1,2,… La mayor parte del costo está en la última iteración (serie geométrica ≈ b/(b−1) veces); además mejora el orden de jugadas y da respuesta en cualquier momento.
11. Caché de valores de posiciones ya evaluadas. Zobrist: XOR de números aleatorios por (pieza, casilla); actualización incremental O(1).
12. Q/N (explotación, tasa de victoria) + c·√(ln N_padre/N) (exploración, crece si el hijo se visita poco). c≈√2.
13. Selección (UCB1), expansión (añadir hijo), simulación (playout), retropropagación (actualizar N, Q).
14. Porque se calculan promedios; una transformación monótona no lineal puede cambiar qué jugada tiene mayor esperanza.
15. Sustituye playouts por una red de valor, usa la política de la red como prior (PUCT), y aprende solo por autojuego.
16. Ejemplo: diferencia de piezas, diferencia de damas (×1.5–3), piezas en el centro, piezas en la fila trasera (defensa), movilidad, piezas vulnerables.
