# Teoría — CSP y planificación

## 1. Problemas de satisfacción de restricciones
CSP = ⟨X, D, C⟩. Una **asignación** es consistente si no viola restricciones y completa si asigna todas las variables; una solución es consistente y completa. Ventaja frente a búsqueda genérica: el estado tiene estructura factorizada, así que se podan grandes regiones al detectar una violación parcial.

Ejemplos: coloreo de mapas, n-reinas, sudoku, horarios (*timetabling*), asignación de frecuencias, criptoaritmética (SEND+MORE=MONEY), configuración de productos.

Tipos de restricciones: unarias (`SA ≠ verde`), binarias (`SA ≠ WA`), de orden superior, **globales** (`AllDiff`, `Atmost`), preferencias (CSP con costos → COP).

## 2. Propagación de restricciones
- **Consistencia de nodo:** todo valor satisface las restricciones unarias.
- **Consistencia de arco:** ∀x∈Di ∃y∈Dj con (x,y) permitido.
```
REVISAR(Xi, Xj): para cada x en Di: si ningún y en Dj satisface C(x,y): borrar x
AC-3: cola de arcos; al revisar (Xi,Xj) con cambios, reencolar (Xk,Xi) ∀Xk vecino
```
Costo O(c·d³). AC-3 sola **no** garantiza solución (Australia con 2 colores queda arco-consistente).
- **Consistencia de camino** y **k-consistencia**: un CSP fuertemente n-consistente se resuelve sin retroceso.
- AllDiff: si m variables tienen en total menos de m valores distintos → inconsistente.

## 3. Backtracking
```
BT(asig):
    si completa: devolver asig
    var ← SELECCIONAR-VARIABLE()          # MRV, desempate por grado
    para valor en ORDENAR-VALORES(var):   # LCV
        si consistente:
            asig[var] ← valor
            inferencias ← INFERENCIA()     # forward checking o MAC (AC-3 incremental)
            si no falla: r ← BT(asig); si r: devolver r
            deshacer
    devolver falla
```
- **MRV** ("falla primero"): variable con menos valores legales. **Grado:** más restricciones con variables libres.
- **LCV** ("tiene éxito primero"): valor que deja más opciones a los vecinos.
- **Forward checking** detecta fallas un paso antes; **MAC** propaga por completo.
- **Backjumping dirigido por conflictos** y **aprendizaje de restricciones** (no-goods): base de los SAT solvers CDCL modernos.

## 4. Búsqueda local para CSP
Min-conflictos: asignación completa y reparar la variable conflictiva con el valor que minimiza conflictos. n-reinas con n=10⁶ en ~50 pasos. Mejoras: tabú, ponderación de restricciones (*breakout*).

## 5. Estructura del problema
- Componentes independientes → resolver por separado.
- **CSP con grafo árbol:** ordenar topológicamente, hacer arco-consistente de hojas a raíz, asignar de raíz a hojas: O(n·d²).
- **Conjunto de corte de ciclo:** asignar un conjunto S que deje un árbol → O(d^|S|·(n−|S|)·d²).
- **Descomposición en árbol** con ancho w → O(n·d^{w+1}).

## 6. Planificación clásica
Entorno determinista, totalmente observable, estático. **STRIPS/PDDL:**
```
Acción: Mover(b, x, y)
  PRE:   Sobre(b,x) ∧ Libre(b) ∧ Libre(y)
  EFECTO: Sobre(b,y) ∧ Libre(x) ∧ ¬Sobre(b,x) ∧ ¬Libre(y)
```
Supuesto de mundo cerrado: lo no mencionado es falso. RESULTADO(s,a) = (s − DEL(a)) ∪ ADD(a).

Búsqueda **hacia adelante** (progresión) y **hacia atrás** (regresión: `g' = (g − ADD(a)) ∪ PRE(a)`, solo acciones relevantes y consistentes).

**Anomalía de Sussman**: resolver las submetas de forma independiente y en secuencia falla; muestra que las metas interactúan.

## 7. Heurísticas para planificación
Se obtienen de problemas **relajados**:
- *Ignorar precondiciones* → cubrimiento de conjuntos.
- *Ignorar listas de borrado* → el problema relajado es monótono; `h+` óptimo es NP-duro, pero aproximaciones `h_max` (admisible), `h_add`, `h_FF` (plan relajado extraído) funcionan muy bien.
- **GraphPlan:** capas alternas de literales y acciones con exclusiones mutuas (mutex); el nivel donde aparecen todas las metas sin mutex es una cota inferior.
- Planificadores modernos: Fast Downward (LAMA, landmarks), SATPlan.

## 8. Más allá
HTN (jerárquica), planificación temporal y con recursos, planificación no determinista/condicional, programación entera mixta para scheduling, y uso de LLMs como generadores de planes verificados por un planificador clásico (LLM+P).
