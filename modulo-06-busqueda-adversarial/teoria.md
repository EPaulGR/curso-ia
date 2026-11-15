# Teoría — Búsqueda con adversarios

## 1. Juegos como problemas de búsqueda
Un juego determinista, de dos jugadores, por turnos, de suma cero e información perfecta se define con:
- `S0` estado inicial; `JUGADOR(s)`; `ACCIONES(s)`; `RESULTADO(s,a)`; `TERMINAL(s)`; `UTILIDAD(s,p)`.

"Suma cero": lo que gana uno lo pierde el otro, `U(s,MAX) = −U(s,MIN)`. El **árbol de juego** tiene factor de ramificación `b` y profundidad `m`: gato ≈ 9! = 362 880 hojas; ajedrez ≈ 35^80 ≈ 10^123 → imposible explorar completo.

## 2. MINIMAX
El valor minimax de un estado es la utilidad que obtiene MAX si ambos juegan óptimamente:

```
MINIMAX(s) = UTILIDAD(s, MAX)                        si TERMINAL(s)
           = max_a MINIMAX(RESULTADO(s,a))           si JUGADOR(s)=MAX
           = min_a MINIMAX(RESULTADO(s,a))           si JUGADOR(s)=MIN
```
Recorrido en profundidad: tiempo `O(b^m)`, espacio `O(bm)`. Es óptimo contra un rival óptimo; contra uno subóptimo puede no maximizar la ganancia esperada.

**Multijugador:** cada nodo tiene un vector de utilidades y cada jugador maximiza su componente.

## 3. Poda alfa-beta
Se mantienen dos cotas a lo largo del camino:
- `α`: mejor valor ya asegurado para MAX (cota inferior).
- `β`: mejor valor ya asegurado para MIN (cota superior).

```
función MAX-VALOR(s, α, β):
    si TERMINAL(s): devolver UTILIDAD(s)
    v ← −∞
    para cada a en ACCIONES(s):
        v ← max(v, MIN-VALOR(RESULTADO(s,a), α, β))
        si v ≥ β: devolver v          # poda: MIN nunca permitirá llegar aquí
        α ← max(α, v)
    devolver v
```
(MIN-VALOR es simétrico con `v ≤ α`.)

**Propiedades:** el valor de la raíz es idéntico al de minimax. Con ordenamiento perfecto, tiempo `O(b^{m/2})` → duplica la profundidad alcanzable; con orden aleatorio ≈ `O(b^{3m/4})`.

## 4. Funciones de evaluación (BUAP 3.2)
Con corte a profundidad `d` se sustituye `UTILIDAD` por `EVAL(s)`. Requisitos: (1) ordenar estados terminales igual que la utilidad, (2) rápida, (3) fuertemente correlacionada con la probabilidad de ganar. Forma típica, lineal ponderada:

`EVAL(s) = w1·f1(s) + w2·f2(s) + … + wn·fn(s)`

Ejemplos: ajedrez — material (peón 1, caballo/alfil 3, torre 5, dama 9), movilidad, estructura de peones. Conecta-4 — ventanas de 4 con 2–3 fichas propias, control del centro. Los pesos pueden aprenderse (regresión, TD-learning, redes neuronales).

**Efecto horizonte:** una amenaza inevitable se "empuja" más allá de la profundidad. Mitigación: **búsqueda de quiescencia** (seguir buscando solo capturas/jugadas forzadas hasta un estado "quieto") y **extensiones singulares**.

## 5. Reducción del espacio y mejora de calidad (BUAP 3.5–3.6)
- **Ordenamiento de jugadas:** capturas primero, *killer moves* (jugadas que podaron en el mismo nivel), heurística de historia.
- **Profundización iterativa:** buscar d=1,2,3… La mejor jugada de la iteración d se explora primero en d+1; permite control de tiempo (anytime).
- **Tablas de transposición:** hash (Zobrist) de estados ya evaluados → evita recalcular posiciones alcanzadas por distintos órdenes.
- **Poda hacia adelante / beam search:** considerar solo las k mejores jugadas (riesgo de perder la óptima).
- **Búsqueda con ventana nula / PVS / MTD(f)**: variantes de alfa-beta más eficientes.
- **Bases de datos de aperturas y finales** (tablebases).

## 6. Juegos estocásticos e información imperfecta
**Expectiminimax** añade nodos de azar: `Σ_r P(r)·EXPECTIMINIMAX(RESULTADO(s,r))`. Las evaluaciones deben ser transformaciones lineales positivas de la probabilidad de ganar (no basta el orden). Información imperfecta (póker): conjuntos de información, CFR (*counterfactual regret minimization*).

## 7. Monte Carlo Tree Search
Útil cuando `b` es enorme (Go, b≈250) o no hay buena EVAL. Cuatro fases por iteración:
1. **Selección** desde la raíz con UCB1: `Q/N + c·√(ln N_padre / N)` (balance explotación/exploración).
2. **Expansión** de un hijo no probado.
3. **Simulación** (playout) hasta terminal con política por defecto (aleatoria o ligera).
4. **Retropropagación** del resultado actualizando N y Q.
Se elige la jugada de la raíz más visitada. **AlphaZero** reemplaza el playout por una red `(p, v) = f_θ(s)` y usa PUCT: `Q + c·P(s,a)·√N_padre/(1+N)`.

## 8. Estado del arte
Deep Blue (1997): alfa-beta masivo + EVAL experta. AlphaGo (2016), AlphaZero (2017), MuZero (2020, aprende el modelo del juego). Libratus/Pluribus (póker, CFR). Stockfish NNUE: alfa-beta con evaluación por red neuronal eficiente en CPU.
