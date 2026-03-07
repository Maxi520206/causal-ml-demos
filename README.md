# Causal ML Demos

This repository contains small demos illustrating fundamental concepts behind
causal machine learning and statistical learning.

This repository is part of an ongoing exploration of **causal machine learning
and causal NLP**, focusing on how models behave under **distribution shift**
and **spurious correlations**. 

The goal of this repository is to build intuition through **minimal runnable
experiments** that connect:

- probability theory
- statistical inference
- causal reasoning
- distribution shift
- representation learning

Each demo focuses on a **single core concept** and provides a small
reproducible example.

---

# Demos

## Search

### toy_search
[`search/toy_search`](search/toy_search)
A small A* search demo illustrating planning under fixed world assumptions and
how such systems may fail under mechanism shift.

---

## Probability

### Law of Large Numbers
[`probability/lln_demo`](probability/lln_demo)
A simulation illustrating how empirical averages converge to the true
expectation as the number of samples increases.

This principle underlies:

- statistical estimation
- empirical risk minimization
- machine learning training procedures

---

# Repository Structure
```
causal-ml-demos
│
├── search
│   └── toy_search
│
├── probability
│   └── lln_demo
│
└── README.md
```

---

# Why this repository

Modern machine learning systems often rely on **statistical correlations**
learned from data.

However, robust generalization under **distribution shift** requires
understanding the underlying **causal mechanisms** that generate data.

These demos aim to explore the conceptual foundations behind:

- causality
- invariance
- mechanism shift
- shortcut learning

through simple and reproducible experiments.
