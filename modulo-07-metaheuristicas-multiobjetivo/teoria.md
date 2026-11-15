# Teoría — Búsqueda local, metaheurísticas y multiobjetivo

## 0. Optimización y espacios de búsqueda
Problema: `min_{x ∈ X} f(x)` (o max). En búsqueda local solo importa el estado actual, no el camino. Conceptos: **vecindario** N(x), **óptimo local** (ningún vecino mejora), **paisaje de aptitud**, **exploración vs. explotación**. El TSP tiene (n−1)!/2 rutas: para n=20 ≈ 6·10^16. Teorema *No Free Lunch* (Wolpert & Macready 1997): promediado sobre todos los problemas, ningún algoritmo supera a otro → hay que explotar la estructura del problema.

## 1. Ascenso de colinas (hill climbing)
```
x ← aleatorio
repetir:
    y ← mejor vecino de x
    si f(y) no mejora a f(x): devolver x
    x ← y
```
Variantes: mejor mejora vs. primera mejora, estocástico, **reinicios aleatorios** (con probabilidad p de éxito por intento, se esperan 1/p reinicios). Problemas: óptimos locales, mesetas, crestas.

Vecindarios TSP: intercambio de dos ciudades, inserción, **2-opt** (quitar dos aristas y reconectar invirtiendo el segmento; Δ = d(a,c)+d(b,d)−d(a,b)−d(c,d), calculable en O(1)), 3-opt, Lin–Kernighan.

## 2. Recocido simulado
Inspirado en el enfriamiento de metales. Acepta un peor vecino con probabilidad `P = exp(−Δ/T)` (criterio de Metropolis).
```
T ← T0
para k = 1..K:
    y ← vecino aleatorio de x;  Δ ← f(y) − f(x)
    si Δ < 0 o rand() < exp(−Δ/T): x ← y
    T ← α·T            # enfriamiento geométrico, α ∈ [0.8, 0.999]
```
Con enfriamiento logarítmico `T_k = c/log(k)` converge al óptimo global con probabilidad 1 (pero demasiado lento en la práctica). Elegir T0 de modo que al inicio se acepte ~80 % de movimientos peores.

## 3. Búsqueda tabú (Glover)
Memoria adaptativa para escapar de óptimos locales:
- **Memoria de corto plazo (lista tabú):** atributos de movimientos recientes prohibidos durante `tenencia` iteraciones → evita ciclos.
- **Aspiración:** se ignora lo tabú si el movimiento da una nueva mejor solución.
- Siempre se toma el **mejor vecino admisible**, aunque empeore.
- **Memoria de largo plazo:** frecuencias → *intensificación* (regiones buenas) y *diversificación* (regiones poco visitadas).

## 4. Algoritmos genéticos (Holland 1975)
```
P ← población inicial; evaluar
mientras no termine:
    padres ← SELECCIÓN(P)
    hijos  ← MUTACIÓN(CRUCE(padres))
    evaluar(hijos)
    P ← REEMPLAZO(P, hijos)      # con elitismo
```
- **Representación:** binaria, entera, real, permutación, árbol (programación genética).
- **Selección:** ruleta (proporcional `p_i = f_i/Σf`), ranking, **torneo** de tamaño k (presión selectiva ajustable).
- **Cruce:** un punto, dos puntos, uniforme; en reales: aritmético, BLX-α, SBX; en permutaciones: **OX**, PMX, ciclo.
- **Mutación:** inversión de bit con p ≈ 1/L; gaussiana en reales; intercambio/inversión en permutaciones.
- **Reemplazo:** generacional, estado estable, (μ+λ), (μ,λ).
- **Restricciones:** penalización, reparación, decodificadores.
- **Teorema de los esquemas:** esquemas cortos, de bajo orden y aptitud superior a la media crecen exponencialmente (hipótesis de bloques constructores).
- Otros AE: estrategias evolutivas (CMA-ES), evolución diferencial `v = x_r1 + F(x_r2 − x_r3)`, PSO `v ← ωv + c1r1(pbest−x) + c2r2(gbest−x)`.

## 5. Colonia de hormigas (ACO)
Las hormigas construyen soluciones guiadas por feromona τ y heurística η:

`p_ij = τ_ij^α η_ij^β / Σ_{k∈N_i} τ_ik^α η_ik^β`, con η = 1/d.

Actualización: `τ ← (1−ρ)τ + Σ_h Δτ^h`, `Δτ_ij^h = Q/L_h` si h usó (i,j). Variantes: Elitist AS, Rank-based AS, **MAX–MIN AS** (cotas a τ, solo la mejor deposita), **Ant Colony System** (regla pseudo-aleatoria proporcional, actualización local).

## 6. Sistemas inmunes artificiales y algoritmos meméticos
**CLONALG** (selección clonal): los anticuerpos con mayor afinidad se clonan más (`N_c = round(βN/r)`) y mutan menos (hipermutación `σ ∝ exp(−ρ·afinidad)`); los peores se reemplazan por aleatorios (edición del receptor). Otros: selección negativa (detección de anomalías), redes inmunes (aiNet).

**Meméticos:** AE + búsqueda local por individuo. *Lamarckiano* (se escribe la mejora en el genotipo) vs. *baldwiniano* (solo cambia la aptitud). En TSP, GA+2-opt / GA+Lin–Kernighan está entre los mejores métodos.

## 7. Optimización multiobjetivo
`min F(x) = (f1(x), …, fm(x))`. Los objetivos están en conflicto (costo vs. calidad).
- **Dominancia de Pareto:** a ≺ b si a no es peor en ningún objetivo y es mejor en al menos uno.
- **Conjunto de Pareto** (espacio de decisión) y **frente de Pareto** (espacio objetivo).
- Enfoques clásicos: suma ponderada `Σ w_i f_i` (no encuentra regiones no convexas del frente), ε-restricción.
- **NSGA-II:** (1) ordenamiento no dominado rápido O(MN²); (2) distancia de crowding = suma de lados normalizados del cuboide entre vecinos (extremos = ∞); (3) torneo por (rango menor, crowding mayor); (4) elitismo: unir padres e hijos (2N) y quedarse con los N mejores frentes, rompiendo el último por crowding.
- Otros: SPEA2, MOEA/D (descomposición), NSGA-III (muchos objetivos, puntos de referencia).
- **Métricas:** hipervolumen, IGD, espaciamiento.
- Benchmarks: Schaffer (`x²`, `(x−2)²`), ZDT1–6, DTLZ.

## 8. Metodología experimental
Las metaheurísticas son estocásticas: reporta media, desviación y mediana de ≥ 30 corridas independientes con semillas distintas; usa pruebas no paramétricas (Wilcoxon, Friedman); compara con el mismo número de evaluaciones de f; ajusta parámetros con irace/optuna; usa instancias estándar (TSPLIB, OR-Library).
