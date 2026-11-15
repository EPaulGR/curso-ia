# Teoría — RAG y agentes

## 1. ¿Por qué RAG?
Los LLMs no conocen tus datos privados ni lo posterior a su corte de entrenamiento, y alucinan. RAG recupera fragmentos relevantes y los inyecta en el prompt: conocimiento actualizable sin reentrenar, con citas verificables.

## 2. Recuperación
- **Dispersa** (TF-IDF, BM25): coincidencia léxica, excelente con nombres propios y códigos.
- **Densa** (embeddings): captura sinónimos y paráfrasis. Se compara con coseno o producto punto.
- **Híbrida**: combina ambas (Reciprocal Rank Fusion). Casi siempre gana.
- **ANN**: HNSW construye un grafo navegable de varios niveles, búsqueda ~O(log n) con recall > 95 %.
- **Reranking**: un cross-encoder puntúa (consulta, documento) juntos; más preciso, más caro: se aplica a los top-50.
- **MMR**: equilibra relevancia y diversidad para no llenar el contexto de casi-duplicados.

## 3. Chunking
Demasiado pequeño → pierde contexto; demasiado grande → diluye la señal y gasta tokens. Ventanas de 200–800 tokens con 10–20 % de solape, o por estructura (párrafos, secciones, funciones de código). Guarda metadatos (fuente, sección, fecha) para filtrar y citar.

## 4. Generación
Instrucciones claras: usa solo el contexto, cita [n], admite ignorancia. Ordena los fragmentos (lo más relevante al inicio o al final: "lost in the middle").

## 5. Agentes
Un agente es un LLM en un bucle que decide qué herramienta llamar, observa el resultado y continúa hasta terminar. Claves de diseño:
- Herramientas pocas, bien descritas, con esquemas de entrada estrictos.
- Límite de pasos y de costo; manejo de errores devolviendo el error al modelo.
- Preferir flujos simples (cadenas de prompts, enrutadores) antes que agentes totalmente autónomos.
- MCP estandariza cómo exponer herramientas y datos a los modelos.

## 6. Evaluación
- Recuperación: precisión@k, recall@k, MRR, nDCG.
- Respuesta: exact match, F1, y para texto libre **LLM-as-judge** con rúbrica (validado contra juicios humanos).
- RAG: fidelidad (¿cada afirmación está respaldada?), relevancia del contexto, relevancia de la respuesta.
- Construye un **conjunto dorado** de 50–200 preguntas antes de optimizar nada.

## 7. Seguridad
Todo texto recuperado o devuelto por una herramienta es dato no confiable: puede contener inyecciones de prompt. Mitiga con permisos mínimos, confirmación humana para acciones irreversibles, separación de instrucciones y datos.
