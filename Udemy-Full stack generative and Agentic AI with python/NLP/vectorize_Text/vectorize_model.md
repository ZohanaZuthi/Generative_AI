# Difference Between Bag of Words and TF-IDF

Both are techniques to convert text into numbers for NLP and Machine Learning.

Both create:

```text id="ppghgj"
Document-Term Matrix
```

But they calculate values differently.

---

# 1. Bag of Words (BoW)

Bag of Words simply counts:

```text id="a98vgx"
How many times each word appears
```

Uses raw frequency.

---

# Example

Documents:

```python id="7isxj3"
docs = [
    "I love AI",
    "I love machine learning"
]
```

Vocabulary:

```text id="5qymhf"
['ai', 'learning', 'love', 'machine']
```

BoW matrix:

| Document | ai  | learning | love | machine |
| -------- | --- | -------- | ---- | ------- |
| Doc1     | 1   | 0        | 1    | 0       |
| Doc2     | 0   | 1        | 1    | 1       |

---

# BoW Formula

Very simple:

BoW(word)=\text{count of word in document}

---

# Problem with Bag of Words

Common words dominate.

Example:

```text id="x0hj7q"
the
is
good
```

appear everywhere.

But they may not be important semantically.

---

# 2. TF-IDF

TF-IDF tries to measure:

```text id="0rb3ml"
How important a word is
```

instead of just counting frequency.

---

# TF-IDF Full Form

```text id="m1ddpn"
Term Frequency - Inverse Document Frequency
```

---

# Main Idea

A word is important if:

- appears frequently in one document
- appears rarely across all documents

---

# Example Intuition

Suppose:

```text id="5v6m4g"
"football"
```

appears mostly in sports articles.

Very informative.

But:

```text id="1pdjlwm"
"the"
```

appears everywhere.

Not informative.

TF-IDF reduces importance of common words.

---

# TF-IDF Formula

TF-IDF =

TF\times IDF

---

# 1. TF (Term Frequency)

Measures:

```text id="lct7u9"
How frequent word is inside document
```

Formula:

TF(t,d)=\frac{\text{count of term }t\text{ in document }d}{\text{total words in document}}

---

# 2. IDF (Inverse Document Frequency)

Measures:

```text id="zfcvff"
How rare word is across all documents
```

Formula:

IDF(t)=\log\left(\frac{N}{df(t)}\right)

Where:

| Symbol | Meaning                     |
| ------ | --------------------------- |
| N      | total documents             |
| df(t)  | documents containing term t |

---

# Important Intuition

## High TF-IDF

Means:

```text id="jd3hhp"
important and unique word
```

---

## Low TF-IDF

Means:

```text id="cnl6yf"
common word appearing everywhere
```

---

# Example

Documents:

```text id="67jlwm"
Doc1: football goal match
Doc2: football player goal
Doc3: machine learning AI
```

Word:

```text id="q69fsd"
football
```

appears in many sports docs.

Moderate importance.

Word:

```text id="8hzbjw"
AI
```

appears only once.

Very informative.

So TF-IDF gives:

```text id="0fjlwm"
AI -> higher weight
football -> lower weight
```

---

# sklearn Example

## Bag of Words

```python id="c70p0v"
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

X = cv.fit_transform(docs)
```

---

## TF-IDF

```python id="cykpnl"
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

X = tfidf.fit_transform(docs)
```

---

# Output Difference

## Bag of Words

Raw counts:

```text id="jlwmn7"
love -> 2
```

---

## TF-IDF

Weighted importance:

```text id="s5wzce"
love -> 0.41
```

floating-point scores.

---

# Visualization

# Bag of Words

```text id="kgd0vq"
Word count only
```

---

# TF-IDF

```text id="uxpbqc"
Word importance score
```

---

# Key Difference

| Feature                        | Bag of Words   | TF-IDF                 |
| ------------------------------ | -------------- | ---------------------- |
| Uses raw count                 | YES            | Partly                 |
| Reduces common word importance | NO             | YES                    |
| Output                         | Integer counts | Float weights          |
| Semantic importance            | Weak           | Better                 |
| Simpler                        | YES            | More advanced          |
| Good for LDA                   | YES            | Usually less preferred |
| Good for classification/search | Medium         | Better                 |

---

# Why LDA Often Uses BoW

Gensim and LDA assume:

```text id="h6ehww"
documents are generated from word frequencies
```

So raw counts work better.

---

# Why TF-IDF Good for LSA

LSA uses:

```text id="0q87sj"
matrix decomposition
```

So weighted importance helps more.

---

# Sparse Matrix in Both

Both produce:

```text id="u1gr8d"
sparse matrices
```

because most words are absent in most documents.

---

# Mental Model

# Bag of Words

```text id="gq1u4x"
"How many times did this word appear?"
```

---

# TF-IDF

```text id="emjlwm"
"How important is this word in this document?"
```

---

# Real-World Usage

| Task                | Better Choice    |
| ------------------- | ---------------- |
| LDA Topic Modeling  | BoW              |
| Search Engines      | TF-IDF           |
| Document Similarity | TF-IDF           |
| Simple NLP baseline | BoW              |
| Semantic retrieval  | TF-IDF           |
| Modern transformers | Neither directly |

---

# Interview Summary

## Bag of Words

Counts word frequency only.

---

## TF-IDF

Weights words by:

- frequency inside document
- rarity across documents

to reduce importance of common words and highlight informative words.
