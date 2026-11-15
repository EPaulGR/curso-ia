# Respuestas — Quiz módulo 09
1. ⊨ es semántica (verdad en modelos); ⊢ es sintáctica (derivación con reglas). Solidez: ⊢ ⇒ ⊨; completitud: ⊨ ⇒ ⊢.
2. α válida ⇔ ¬α insatisfacible. KB ⊨ α ⇔ (KB⇒α) válida ⇔ KB∧¬α insatisfacible.
3. (A∨B∨C)… paso a paso: ((¬A∨B)⇒C) ∧ (C⇒(¬A∨B)) → ((A∧¬B)∨C) ∧ (¬C∨¬A∨B) → (A∨C) ∧ (¬B∨C) ∧ (¬A∨B∨¬C).
4. Cláusulas: ¬P∨Q, ¬Q∨R, P, ¬R. P con ¬P∨Q → Q; Q con ¬Q∨R → R; R con ¬R → □.
5. Solo hay un número finito de cláusulas distintas sobre un conjunto finito de símbolos.
6. A lo más un literal positivo. Cada regla se dispara una vez y cada premisa se decrementa una vez (contadores).
7. Unitaria: una cláusula con un solo literal fuerza su valor. Puro: literal que aparece con un solo signo se puede hacer verdadero sin perder soluciones.
8. Aprendizaje de cláusulas de conflicto, backjumping no cronológico, reinicios, VSIDS, watched literals.
9. ∀e [Estudiante(e) ∧ En(e,BUAP) ∧ Aprueba(e,IA) ⇒ ∃p (Profesor(p) ∧ Enseñó(p,e) ∧ Conoce(e,p))].
10. "No todos cumplen P" equivale a "existe alguno que no la cumple" (De Morgan generalizado).
11. {y/Juan, x/Madre(Juan)}.
12. Evita unificar x con f(x) (términos infinitos, inferencias no sólidas). Prolog lo omite por eficiencia (hace la unificación lineal).
13. ∀x Ama(F(x), x), con F función de Skolem.
14. Si KB ⊨ α, un procedimiento completo lo demuestra en tiempo finito; si no, puede no terminar nunca.
15. `\+ p` tiene éxito si p no se puede probar (supuesto de mundo cerrado); no es negación lógica.
16. Base de conocimiento, memoria de trabajo, motor de inferencia, explicación, interfaz, adquisición de conocimiento.
17. 0.6 + 0.5·(1 − 0.6) = 0.8.
18. Ventajas: explicables, sin datos, conocimiento experto explícito. Límites: adquisición costosa, frágiles fuera de su dominio, no aprenden, manejo limitado de incertidumbre.
