# Teoría — Razonamiento bajo incertidumbre

## 1. Por qué probabilidad
La lógica falla con: pereza (demasiadas reglas), ignorancia teórica y práctica. La probabilidad resume la incertidumbre. Axiomas: `0 ≤ P(ω) ≤ 1`, `Σ P(ω) = 1`, `P(a ∨ b) = P(a) + P(b) − P(a ∧ b)`. Los argumentos de De Finetti muestran que un agente con creencias incoherentes puede ser explotado (apuestas holandesas).

**Regla de Bayes:** `P(H|e) = P(e|H)P(H)/P(e)`. Ejemplo: prevalencia 1 %, sensibilidad 90 %, especificidad 95 % → P(enfermo|+) ≈ 15 %. (¡Falacia de la tasa base!)

**Independencia condicional:** `P(X,Y|Z) = P(X|Z)P(Y|Z)`. **Naive Bayes:** `P(C|e1..en) ∝ P(C) Π P(ei|C)`.

## 2. Redes bayesianas
DAG donde cada nodo tiene `P(Xi | Padres(Xi))`. Conjunta: `P(x1..xn) = Π P(xi | padres(Xi))`. Con n variables booleanas y ≤ k padres: O(n·2ᵏ) parámetros en vez de 2ⁿ.
- Cada nodo es condicionalmente independiente de sus no descendientes dados sus padres.
- **Manta de Markov:** padres, hijos y padres de los hijos; dado esto, el nodo es independiente del resto.
- **d-separación:** cadenas `A→B→C` y bifurcaciones `A←B→C` se bloquean observando B; colisionadores `A→B←C` se bloquean si NO se observa B ni sus descendientes (explicación alternativa, *explaining away*).
- CPTs canónicas: deterministas, **noisy-OR**, nodos continuos (lineal-gaussiano).

## 3. Inferencia exacta
**Enumeración:** `P(X|e) = α Σ_y P(X,e,y)`, O(2ⁿ) tiempo. Ejemplo AIMA: `P(Robo | Juan, María) ≈ ⟨0.284, 0.716⟩`.
**Eliminación de variables:** factores, producto punto a punto y suma, eliminando variables en un orden; evita recalcular. Lineal en poliárboles; NP-duro en general (#P-duro). **Árbol de uniones** para muchas consultas.

## 4. Inferencia aproximada
- **Muestreo previo** y **rechazo:** desperdicia muestras cuando la evidencia es improbable.
- **Ponderación por verosimilitud:** fija la evidencia y pondera `w = Π P(ei | padres)`; degrada con evidencia "río abajo" o muy improbable (varianza alta).
- **Gibbs:** cadena de Markov; cada paso muestrea `Xi ~ P(Xi | manta de Markov)` ∝ `P(xi|padres) Π_hijos P(yj|padres(Yj))`. Converge a la posterior (cadena ergódica). Quemado (*burn-in*) y autocorrelación.
- Metropolis–Hastings, HMC/NUTS (Stan, PyMC), inferencia variacional.

## 5. Causalidad (Pearl)
Escalera: asociación `P(y|x)` → intervención `P(y|do(x))` → contrafactuales. `do(x)` corta las aristas entrantes a X. Criterio de puerta trasera: `P(y|do(x)) = Σ_z P(y|x,z)P(z)`.

## 6. Razonamiento temporal
Supuestos: Markov de primer orden `P(Xt|X0:t−1) = P(Xt|Xt−1)`, sensor `P(Et|X0:t,E1:t−1) = P(Et|Xt)`, estacionariedad.
- **Filtrado:** `P(Xt+1|e1:t+1) = α P(et+1|Xt+1) Σ_xt P(Xt+1|xt) P(xt|e1:t)`.
- **Predicción**, **suavizado** (forward–backward: `P(Xk|e1:t) = α f1:k × bk+1:t`), **explicación más probable** (Viterbi, O(T·S²)).
- **HMM** en forma matricial: `f ← α O_{t+1} Tᵀ f`. Aprendizaje: Baum–Welch (EM).
- **Kalman:** modelos lineales gaussianos, la creencia sigue siendo gaussiana; EKF/UKF para no lineales. Ganancia K equilibra predicción y medición.
- **Filtro de partículas:** propagar N muestras, ponderar por la evidencia y re-muestrear; localización de robots (SLAM).
- **Redes bayesianas dinámicas** generalizan HMM y Kalman.

## 7. Teoría de la decisión
Principio de **máxima utilidad esperada**: `a* = argmax_a Σ_s P(s|a,e) U(s)`. Axiomas de von Neumann–Morgenstern. Aversión al riesgo (utilidad cóncava del dinero). **Valor de la información:** `VPI(Ej) = Σ_k P(ej,k) EU(α_ejk | ej,k) − EU(α)` ≥ 0. Redes de decisión (nodos de azar, decisión y utilidad). Puente directo a los MDP del módulo 20.

## 8. Lógica difusa (Zadeh 1965)
Modela **vaguedad** (no aleatoriedad): "alto" con grado μ ∈ [0,1].
- Pertenencias: triangular, trapezoidal, gaussiana, sigmoide.
- Operadores (normas): `A∧B = min`, `A∨B = max`, `¬A = 1−μ`; alternativas: producto, suma probabilística.
- **Mamdani:** fusificar → evaluar reglas → implicación (recorte min) → agregación (max) → defusificar (centroide `z* = ∫μ(z)z dz / ∫μ(z)dz`, bisector, media de máximos).
- **Sugeno:** consecuentes funcionales `z = ax + by + c`; salida = promedio ponderado; base de ANFIS (neurodifuso).
- Aplicaciones: control de lavadoras, trenes (Sendai), frenos ABS, cámaras.

**Probabilidad vs. difusa:** la probabilidad mide incertidumbre sobre hechos nítidos; la difusa, el grado en que un hecho vago es verdadero.
