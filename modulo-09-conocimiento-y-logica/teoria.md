# Teoría — Conocimiento y lógica

## 1. Agentes basados en conocimiento
Una **base de conocimiento** (KB) es un conjunto de oraciones en un lenguaje formal. Interfaz: `TELL(KB, oración)`, `ASK(KB, consulta)`. Enfoque **declarativo**: decir al agente lo que necesita saber y que deduzca qué hacer.

## 2. Lógica proposicional
- Sintaxis: átomos, ¬, ∧, ∨, ⇒, ⇔.
- Semántica: un **modelo** asigna verdadero/falso a cada átomo.
- **Consecuencia lógica:** KB ⊨ α si α es verdadera en todos los modelos de KB.
- **Válida** (tautología): verdadera en todos los modelos. **Satisfacible:** en alguno.
- Teorema de la deducción: KB ⊨ α ⇔ (KB ⇒ α) es válida ⇔ KB ∧ ¬α es insatisfacible.
- Equivalencias: De Morgan, contraposición, distributividad, `α⇒β ≡ ¬α∨β`.

## 3. Inferencia
Un algoritmo es **sólido** si solo deriva consecuencias, **completo** si deriva todas.
- **Verificación de modelos** (TT-ENTAILS): O(2ⁿ), sólido y completo.
- **Resolución:** de `(ℓ ∨ A)` y `(¬ℓ ∨ B)` se deriva `(A ∨ B)`. Con FNC y refutación es completa (teorema de resolución básica).

Conversión a FNC: eliminar ⇔ → eliminar ⇒ → mover ¬ (De Morgan) → distribuir ∨ sobre ∧.

## 4. SAT
SAT fue el primer problema NP-completo (Cook 1971).
- **DPLL:** terminación temprana, **literales puros**, **propagación unitaria**, división.
- **CDCL** (solvers modernos: MiniSat, Kissat): aprendizaje de cláusulas de conflicto, backjumping no cronológico, reinicios, heurística VSIDS, *watched literals*. Resuelven instancias industriales con millones de variables.
- **WalkSAT:** búsqueda local, con probabilidad p voltea una variable aleatoria de una cláusula falsa, si no la que minimiza cláusulas falsas.
- Transición de fase en 3-SAT aleatorio: m/n ≈ 4.26.

## 5. Cláusulas de Horn
Disyunción con a lo más un literal positivo: `(A ∧ B ∧ C) ⇒ D`. Inferencia en **tiempo lineal**:
- **Encadenamiento hacia adelante:** dirigido por datos, hasta punto fijo; sólido y completo para Horn.
- **Encadenamiento hacia atrás:** dirigido por metas; base de Prolog.

## 6. Lógica de primer orden (LPO)
Objetos, relaciones, funciones. Términos, átomos, ∀, ∃, igualdad. `∀x Rey(x) ∧ Codicioso(x) ⇒ Malvado(x)`. `¬∀x P ≡ ∃x ¬P`.
**Ingeniería del conocimiento:** identificar la tarea, reunir conocimiento, decidir vocabulario (ontología), codificar axiomas generales y la instancia, consultar, depurar.

## 7. Inferencia en LPO
- **Instanciación universal/existencial** (constantes de Skolem) → proposicionalización (semidecidible).
- **Unificación:** encontrar θ tal que `SUBST(θ,p) = SUBST(θ,q)`; el **MGU** es único salvo renombramiento. *Occurs check*: `?x` no unifica con `f(?x)`.
- **Modus Ponens generalizado:** de `p1', …, pn'` y `(p1 ∧ … ∧ pn ⇒ q)` con `SUBST(θ,pi') = SUBST(θ,pi)` se deriva `SUBST(θ,q)`.
- **Resolución de primer orden:** FNC con skolemización (`∀x ∃y P(x,y)` → `∀x P(x, F(x))`); completa por refutación.
- La LPO es **semidecidible** (Gödel, Turing, Church).

## 8. Prolog
```prolog
padre(ana, luis).  padre(luis, eva).
ancestro(X, Y) :- padre(X, Y).
ancestro(X, Z) :- padre(X, Y), ancestro(Y, Z).
?- ancestro(ana, Q).
```
Resolución SLD en profundidad, izquierda a derecha; sin occurs check por defecto; **negación como falla** (`\+`) bajo mundo cerrado; el corte `!` poda alternativas. Cuidado con la recursión por la izquierda (bucle infinito).

## 9. Sistemas expertos
Arquitectura: **base de conocimiento** (reglas SI–ENTONCES), **memoria de trabajo** (hechos), **motor de inferencia** (adelante/atrás, resolución de conflictos: especificidad, recencia, prioridad), **subsistema de explicación** ("¿por qué?", "¿cómo?"), interfaz, adquisición de conocimiento (cuello de botella). Ejemplos históricos: DENDRAL, **MYCIN** (factores de certeza `CF = MB − MD`, combinación `CF1 + CF2(1 − CF1)`), XCON/R1. Herramientas: CLIPS, Drools, Prolog.

## 10. Otras representaciones
- **Redes semánticas** y **marcos** (Minsky): herencia con excepciones.
- **Lógicas descriptivas** (OWL): clasificación y subsunción decidibles; ontologías (SNOMED, Gene Ontology).
- **Grafos de conocimiento** (Wikidata, Google KG): tripletas sujeto–predicado–objeto; consultas SPARQL.
- **Razonamiento no monótono**, circunscripción, lógica por defecto.
- **Neurosimbólico:** LLMs que generan programas lógicos verificados por un solver; demostradores automáticos guiados por redes (AlphaProof, Lean).
