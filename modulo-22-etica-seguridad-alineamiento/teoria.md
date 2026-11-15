# Teoría — Ética, seguridad y alineamiento

## 1. Por qué es parte de ser experto
Un sistema técnicamente brillante que discrimina, filtra datos o se deja manipular es un mal sistema. La seguridad y la ética son requisitos de ingeniería, medibles, no adornos.

## 2. Equidad
Con predicción ŷ, etiqueta y y atributo sensible A:
- **Paridad demográfica**: P(ŷ=1|A=a) igual para todos.
- **Igualdad de oportunidades**: TPR igual entre grupos.
- **Odds igualados**: TPR y FPR iguales.
- **Calibración por grupo**: P(y=1|score=s, A=a) = s.
Teorema de imposibilidad (Kleinberg; Chouldechova): si las tasas base difieren, no se pueden cumplir calibración y odds igualados a la vez. Elegir una métrica es una decisión de valores, no solo técnica. Mitigación: preprocesamiento (reponderar), en el entrenamiento (restricciones), posprocesamiento (umbrales por grupo).

## 3. Interpretabilidad
- **Shapley**: única atribución que cumple eficiencia, simetría, dummy y aditividad. SHAP la aproxima.
- **Saliencia / Grad×Input / Gradientes Integrados**: atribuciones basadas en gradiente; IG cumple completitud.
- **Interpretabilidad mecanicista**: entender los circuitos internos (cabezas de inducción, superposición, autoencoders dispersos que extraen "features" monosemánticas).
Cuidado: las explicaciones pueden ser plausibles pero infieles al modelo.

## 4. Robustez adversarial
Pequeñas perturbaciones casi imperceptibles cambian la predicción. FGSM: un paso en el signo del gradiente; PGD: varios pasos proyectados (ataque más fuerte). Entrenamiento adversarial = min_θ E[max_{||δ||≤ε} L(x+δ)].

## 5. Seguridad de LLMs
- **Jailbreaks**: role-play, ofuscación, ataques de muchos ejemplos (many-shot), sufijos optimizados (GCG).
- **Inyección indirecta**: instrucciones escondidas en documentos, webs o resultados de herramientas que el agente procesa. Las defensas por palabras clave son débiles; se combinan con separación de privilegios, confirmación humana y modelos clasificadores.
- **Red teaming**: conjuntos de casos (deben rechazarse / no deben) para medir rechazo correcto y **sobre-rechazo** (ser inútilmente restrictivo también es un fallo).

## 6. Calibración
Una red moderna suele estar sobreconfiada. ECE mide la brecha confianza–exactitud. El escalado de temperatura (un solo parámetro en validación) corrige mucho sin cambiar la exactitud. Conformal prediction da conjuntos con cobertura garantizada.

## 7. Alineamiento
Problema: lograr que sistemas cada vez más capaces persigan los objetivos que de verdad queremos. Fenómenos: especificación incorrecta, **reward hacking**, generalización errónea de objetivos, comportamiento engañoso. Técnicas: RLHF, Constitutional AI (retroalimentación de IA guiada por principios), supervisión escalable (debate, amplificación), interpretabilidad para auditar, evaluaciones de capacidades peligrosas y políticas de escalamiento responsable.

## 8. Regulación
EU AI Act (enfoque por riesgo), NIST AI RMF, ISO/IEC 42001; en México, iniciativas en discusión y la Ley Federal de Protección de Datos Personales para el tratamiento de datos.
