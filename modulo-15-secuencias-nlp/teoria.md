# Teoría — Secuencias y NLP

## 1. Del texto a números
Tokenizar decide la unidad: palabra (vocabulario enorme, problema de palabras desconocidas), carácter (secuencias largas) o **subpalabra** (el estándar actual). Se asigna un id a cada token; `<pad>` rellena secuencias y `<unk>` cubre lo desconocido.

## 2. Representaciones dispersas
- **BoW**: conteos por documento; pierde el orden.
- **TF-IDF**: tf(t,d)·idf(t), idf = log(N/df). Penaliza palabras comunes. Con similitud coseno sigue siendo una línea base fuerte para búsqueda y clasificación (y es la base de BM25, usado en RAG híbrido, módulo 19).

## 3. Modelos de lenguaje n-grama
P(w₁…wₙ) = Π P(wᵢ | w_{i−n+1…i−1}) (supuesto de Markov). Estimación por conteos; el suavizado evita probabilidades 0: Laplace (+1), Kneser-Ney (el mejor clásico).
**Perplejidad** PP = exp(−(1/N) Σ log P(wᵢ|contexto)): el "número efectivo de opciones" por paso. Menor es mejor. Es la misma métrica que se usa para LLMs.

## 4. Embeddings
Hipótesis distribucional (Firth): "conocerás una palabra por sus compañías". **Skip-gram** predice el contexto a partir del centro. Con negative sampling la pérdida por par es
L = −log σ(u_o·v_c) − Σ_k log σ(−u_k·v_c).
Los vectores capturan analogías (rey − hombre + mujer ≈ reina) y también los sesgos del corpus (módulo 22). GloVe factoriza co-ocurrencias; fastText usa n-gramas de caracteres.

## 5. RNN
h_t = tanh(x_t W_x + h_{t−1} W_h + b). Los mismos pesos en cada paso. Se entrena con **BPTT** (desenrollar en el tiempo). El gradiente incluye productos de W_h repetidos: si su radio espectral < 1 desaparece, si > 1 explota. Soluciones: gradient clipping (explosión), arquitecturas con compuertas (desaparición).

## 6. LSTM y GRU
LSTM añade una celda c_t con flujo aditivo:
- i = σ(·), f = σ(·), g = tanh(·), o = σ(·)
- c_t = f ⊙ c_{t−1} + i ⊙ g
- h_t = o ⊙ tanh(c_t)
La suma en c_t permite que el gradiente fluya muchos pasos (idea parecida a las conexiones residuales). GRU simplifica a dos compuertas.

## 7. Seq2seq y atención
Encoder resume la entrada en un vector; decoder genera la salida. El cuello de botella del vector único lo resolvió la **atención** (Bahdanau 2015): en cada paso el decoder hace un promedio ponderado de todos los estados del encoder. El Transformer (módulo 16) elimina la recurrencia y deja solo la atención.

## 8. Subpalabras
**BPE**: empieza con caracteres y fusiona repetidamente el par más frecuente. Resultado: palabras comunes como un token, raras como varias piezas; no existe `<unk>` (con BPE a nivel de bytes). WordPiece (BERT) y Unigram/SentencePiece (T5, Llama) son variantes. La tokenización afecta costo, multilingüismo y la aritmética de los LLMs.

## 9. Evaluación
Clasificación: exactitud, F1 macro. Secuencias: F1 por entidad (NER), BLEU/chrF (traducción), perplejidad (modelado de lenguaje).
