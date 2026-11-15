# Módulo 15 — Modelos de secuencias y procesamiento de lenguaje natural

**Fase 4 · Deep Learning** · Duración: 4 semanas (~45 h) · Prerrequisitos: 02, 13

## Objetivos
- Representar texto: tokenización, BoW, TF-IDF, subpalabras (BPE).
- Construir modelos de lenguaje n-grama y medir perplejidad.
- Entrenar embeddings (word2vec skip-gram con negative sampling) desde cero.
- Implementar RNN y LSTM, entender BPTT y el gradiente que desaparece.
- Entrenar clasificadores de secuencias en PyTorch/MPS.

## Temario
1. Pipeline de NLP: normalización, tokenización, vocabulario, `<unk>`, `<pad>`.
2. Representaciones dispersas: bolsa de palabras, TF-IDF, n-gramas.
3. Modelos de lenguaje estadísticos, suavizado (Laplace, Kneser-Ney), perplejidad.
4. Semántica distribucional y embeddings: word2vec, GloVe, fastText.
5. RNN, BPTT, gradiente que desaparece/explota, clipping.
6. LSTM y GRU; bidireccionales; secuencia a secuencia con encoder–decoder.
7. Mecanismo de atención de Bahdanau (puente al módulo 16).
8. Tokenización por subpalabras: BPE, WordPiece, SentencePiece.
9. Tareas: clasificación, NER, traducción; métricas (F1, BLEU).

## Lecturas
- Jurafsky & Martin, *Speech and Language Processing* 3ª ed.: cap. 2 (tokenización), 3 (n-gramas), 6 (semántica vectorial), 8 (RNN/LSTM).
- Goodfellow et al., cap. 10 (Sequence Modeling).
- Prince, *UDL*, cap. 12 (sección de antecedentes).
- AIMA 4ª ed., cap. 23–24 (NLP y deep learning para NLP).
- Papers: Mikolov et al. 2013 (word2vec); Hochreiter & Schmidhuber 1997 (LSTM); Bahdanau et al. 2015; Sennrich et al. 2016 (BPE).
- Blog: Christopher Olah, *Understanding LSTM Networks*.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_tokenizacion.py | Tokenizar y construir vocabulario |
| 02 | ej02_tfidf.py | BoW y TF-IDF (validado contra scikit-learn) |
| 03 | ej03_ngramas.py | Bigramas, Laplace, perplejidad |
| 04 | ej04_skipgram.py | Word2vec SGNS desde cero |
| 05 | ej05_rnn_numpy.py | RNN forward y explosión del gradiente |
| 06 | ej06_lstm_celda.py | Celda LSTM (validada contra PyTorch) |
| 07 | ej07_clasificador_lstm.py | Clasificador LSTM en MPS |
| 08 | ej08_bpe.py | Byte Pair Encoding |

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
