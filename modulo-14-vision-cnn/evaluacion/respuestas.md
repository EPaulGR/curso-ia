# Respuestas — Módulo 14

1. Localidad y estacionariedad estadística (pesos compartidos).
2. Equivarianza: desplazar la entrada desplaza la salida (convolución). Invariancia: la salida no cambia (pooling/global pooling aproximan invariancia).
3. ⌊(64 + 4 − 4 − 1)/2⌋ + 1 = 32.
4. 128·64·9 + 128 = 73 856.
5. Mismo campo receptivo (7), menos parámetros (27C² vs 49C²) y tres no linealidades.
6. Reordena los parches en columnas para que la convolución sea una multiplicación de matrices optimizada (BLAS/GPU).
7. Mezclar/reducir canales sin mirar vecindad espacial (bottlenecks).
8. El atajo identidad da un camino directo al gradiente y hace fácil representar la identidad; la red aprende el residuo F(x).
9. En train usa media/varianza del batch y actualiza medias móviles; en eval usa las medias móviles fijas.
10. Congelar el backbone y entrenar la cabeza nueva; luego descongelar y afinar todo con lr bajo (y quizá lr discriminativo por capa).
11. Región de la entrada que influye en una unidad; cada stride multiplica el incremento aportado por las capas siguientes.
12. Intersección 4, unión 16+16−4 = 28 → 1/7 ≈ 0.143.
13. Elimina detecciones duplicadas que se solapan sobre el mismo objeto, conservando la de mayor puntaje.
14. Dos etapas: propone regiones y luego clasifica (más precisas, más lentas). Una etapa: predice cajas y clases densamente en una pasada (rápidas).
15. Divide en parches, los proyecta linealmente como tokens, añade embeddings de posición y un token [CLS], y los pasa por capas de autoatención.
16. Un espacio común de embeddings imagen–texto entrenado contrastivamente; permite clasificar con prompts de texto de clases nunca vistas en entrenamiento.
17. Esperado: división estratificada por paciente, transfer learning (ResNet/ConvNeXt/ViT preentrenado), augmentation adecuada al dominio, métricas por clase (sensibilidad, AUC), validación cruzada, calibración, interpretabilidad (Grad-CAM), revisión de sesgos.
