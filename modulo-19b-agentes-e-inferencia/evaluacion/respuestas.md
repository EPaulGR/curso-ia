# Respuestas — Quiz módulo 19b

1. En un *workflow* el código predefine los pasos (encadenar, enrutar, paralelizar). En un agente el LLM decide dinámicamente qué hacer y cuándo terminar.
2. *Tools* (funciones invocables), *resources* (datos legibles) y *prompts* (plantillas).
3. Porque es un aviso unidireccional. Se reconoce porque no tiene campo `id`.
4. Con un resultado `isError: true`, porque es un error de ejecución que el LLM debe ver para corregirse. `error` se reserva para fallos del protocolo.
5. *stdio* para servidores locales lanzados como subproceso; *Streamable HTTP* para servidores remotos o compartidos.
6. Se guardan observaciones en un almacén externo y se recuperan las relevantes para la situación actual. *Generative Agents* combina recencia, importancia y relevancia.
7. Ventaja: paralelismo y contextos aislados (cada trabajador se enfoca). Costo: muchos más tokens, coordinación más difícil y errores que se propagan.
8. Porque los tests dan una recompensa verificable y automática (pasa o no pasa), sin necesidad de un humano.
9. pass@1 = 3/10 = 0.3. pass^2 = C(3,2)/C(10,2) = 3/45 ≈ 0.067.
10. Porque un usuario espera que funcione siempre, no "alguna vez". pass^k cae rápido si el agente es inconsistente.
11. Acceso a datos privados + exposición a contenido no confiable + capacidad de comunicarse hacia fuera.
12. Incluir instrucciones maliciosas en la descripción o los metadatos de una herramienta MCP. El modelo las lee como contexto y puede obedecerlas.
13. Mínimo privilegio y *allowlist*, confirmación humana, sandbox sin red, *spotlighting*, detectores, separación privilegiado/cuarentena, auditoría. Ninguna basta sola porque el modelo no separa de forma confiable datos de instrucciones, y los detectores tienen falsos negativos.
14. En cada token hay que leer todos los pesos de memoria y se hacen pocas operaciones por byte leído, así que el cuello de botella es la transferencia, no los FLOPs.
15. De norm(max(0, p − q)). La probabilidad total de emitir x es q(x)·min(1, p/q) + (1 − β)·residual(x) = min(p, q) + max(0, p − q) = p(x).
16. Σ min(p, q) = 0.2 + 0.3 + 0.2 = 0.7.
17. La fragmentación y el desperdicio del KV cache por reservar memoria contigua del tamaño máximo. Usa la analogía de la memoria virtual con páginas y tabla de páginas.
18. Porque las solicitudes cortas no esperan a que termine la más larga del lote: entran y salen en cada iteración.
19. Ambas son cuantizaciones por bloques o grupos con escalas (y a veces un mínimo o sesgo) por grupo, para acotar el error local.
20. Corta la imagen en parches, el codificador visual produce embeddings y un proyector MLP los mapea al espacio de embeddings del LLM, que los procesa como tokens. CLIP maximiza la similitud de los pares imagen-texto correctos (la diagonal) frente a los incorrectos del lote, con InfoNCE simétrica.

**Bonus (criterios):** debe incluir confirmación antes de enviar, *spotlighting* del contenido de los correos, separar la lectura del envío (un agente en cuarentena resume y uno privilegiado actúa sin ver texto crudo), límite de destinatarios a una *allowlist*, registro y auditoría, y pruebas de red teaming.
