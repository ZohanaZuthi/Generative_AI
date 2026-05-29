# LSA (Latent Semantic Analysis)

LSA is an older but very important NLP technique used to discover hidden relationships between words and documents.

It is also called:

```text id="bdctyh"
LSI = Latent Semantic Indexing
```

especially in search engines.

---

# Main Goal of LSA

LSA tries to answer:

```text id="v8v9q6"
Which words and documents are semantically related?
```

Even if exact words are different.

Example:

```text id="jtyr9u"
car
automobile
vehicle
```

LSA tries to understand they are related.

---

# Core Idea

LSA assumes:

```text id="7nk5wx"
Words appearing in similar contexts
usually have similar meanings.
```

---

# LSA Workflow

```text id="mhs1lq"
Documents
   ↓
CountVectorizer / TF-IDF
   ↓
Document-Term Matrix
   ↓
SVD (Matrix Decomposition)
   ↓
Hidden Semantic Topics
```

---

# Important Difference from LDA

| LSA            | LDA                          |
| -------------- | ---------------------------- |
| Linear Algebra | Probability                  |
| Uses SVD       | Uses Bayesian inference      |
| Deterministic  | Probabilistic                |
| Faster         | More interpretable           |
| Older approach | Modern classical topic model |

---

# Step-by-Step Example

Suppose documents:

```python id="tm2v6m"
documents = [
    "machine learning ai",
    "deep learning neural network",
    "football match goal",
    "player scored goal"
]
```

---

# Step 1 — Create Document-Term Matrix

Using:

scikit-learn `CountVectorizer`

or TF-IDF.

Example matrix:

| Word     | Doc1 | Doc2 | Doc3 | Doc4 |
| -------- | ---- | ---- | ---- | ---- |
| learning | 1    | 1    | 0    | 0    |
| neural   | 0    | 1    | 0    | 0    |
| football | 0    | 0    | 1    | 0    |
| goal     | 0    | 0    | 1    | 1    |

---

# Problem with Raw Matrix

The matrix is:

- huge
- sparse
- noisy

LSA reduces dimensions.

---

# Core Mathematics of LSA

LSA uses:

# Singular Value Decomposition (SVD)

This is the heart of LSA.

Mathematically:

A = U\Sigma V^T

---

# What is This?

Suppose:

```text id="x39q2n"
A = original document-term matrix
```

SVD breaks it into 3 smaller matrices:

| Matrix    | Meaning                      |
| --------- | ---------------------------- |
| U         | word-topic relationships     |
| Σ (Sigma) | topic importance             |
| Vᵀ        | topic-document relationships |

---

# Intuition of SVD

Think of SVD like:

```text id="9q1bho"
compressing information
while preserving important semantic structure
```

It removes noise.

---

# Example Intuition

Original matrix:

```text id="t8d5tt"
10000 words
```

LSA may reduce to:

```text id="8msd5s"
100 latent semantic dimensions
```

---

# Why Called "Latent"?

Because hidden semantic structures are discovered.

Example:

```text id="cn1o8g"
car
vehicle
automobile
```

may become close in latent space.

---

# LSA in sklearn

Example:

```python id="ppnxtg"
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

documents = [
    "machine learning ai",
    "deep learning neural network",
    "football goal match",
    "player scored goal"
]

# TF-IDF Matrix
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

# LSA using SVD
lsa = TruncatedSVD(n_components=2)

X_lsa = lsa.fit_transform(X)

print(X_lsa)
```

---

# Why `TruncatedSVD`?

Full SVD is expensive.

So LSA usually uses:

```text id="3e4t4j"
Truncated SVD
```

which keeps only important components.

---

# Meaning of `n_components`

Example:

```python id="bsg5nd"
n_components=2
```

means:

```text id="r4u3k5"
reduce data into 2 latent semantic dimensions/topics
```

---

# What Does LSA Learn?

LSA learns:

## Hidden semantic dimensions

NOT probability-based topics like LDA.

---

# Example Topic Interpretation

Possible latent dimension:

```text id="t6l42q"
AI dimension:
learning, neural, machine
```

Another:

```text id="plr92e"
Sports dimension:
goal, football, player
```

---

# Geometry Interpretation

LSA converts:

```text id="84hjq5"
words and documents
```

into vectors in semantic space.

Similar meaning:

```text id="ob25hs"
closer vectors
```

---

# Example

```text id="d5q4ob"
king
queen
prince
```

may appear close together.

---

# Why TF-IDF Often Used

Unlike LDA:

LSA often works better with:

- TF-IDF
- weighted importance

instead of raw counts.

---

# LSA vs LDA

| Feature               | LSA               | LDA                     |
| --------------------- | ----------------- | ----------------------- |
| Method                | Linear algebra    | Bayesian probability    |
| Core technique        | SVD               | Dirichlet distributions |
| Topics                | Latent dimensions | Probabilistic topics    |
| Word probabilities    | NO                | YES                     |
| Interpretability      | Medium            | Better                  |
| Speed                 | Faster            | Slower                  |
| Handles polysemy well | Medium            | Better                  |

---

# Advantages of LSA

## 1. Fast

SVD is efficient.

---

## 2. Captures Semantic Similarity

Understands related words.

---

## 3. Reduces Noise

Dimensionality reduction.

---

## 4. Good for Search Engines

Used in early semantic search.

---

# Limitations of LSA

## 1. Hard Topic Interpretation

Latent dimensions are not always human-readable.

---

## 2. No Probabilistic Meaning

Unlike LDA.

---

## 3. Struggles with Polysemy

Example:

```text id="j0u6g5"
bank
```

river bank vs finance bank.

---

## 4. Linear Method

Cannot capture deep contextual meaning like transformers.

---

# LSA vs Modern Embeddings

Traditional:

```text id="tfszbd"
TF-IDF + SVD
```

Modern:

```text id="4qyw0n"
Transformer embeddings
```

Example:

- BERT
- Sentence Transformers
- BERTopic

---

# Real-World Applications

## Search Engines

Semantic retrieval.

---

## Document Similarity

Finding related articles.

---

## Recommendation Systems

Content similarity.

---

## Topic Discovery

Basic topic modeling.

---

# Important Mathematical Insight

LSA does NOT model:

```text id="tjj7zh"
probability distributions
```

Instead it models:

```text id="9dql8w"
linear algebraic semantic structure
```

---

# Mental Model

Think of LSA like:

```text id="0gkq1u"
compressing a huge noisy word-document matrix
into smaller hidden semantic concepts
```

using SVD.

---

# Interview-Level Summary

## What approach does LSA follow?

LSA follows:

```text id="31xxr6"
Linear Algebra based dimensionality reduction
```

using:

A = U\Sigma V^T

through:

```text id="5jqbwh"
Singular Value Decomposition (SVD)
```

to discover hidden semantic relationships between words and documents.
