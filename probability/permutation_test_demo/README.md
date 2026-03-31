# Permutation Test Demo

## Overview

This demo implements a **permutation test** for comparing two independent samples.

The goal is to test whether the two samples come from the same distribution, without making parametric assumptions (e.g., normality).

---

## Hypothesis

* **Null hypothesis (H0):**
  The two samples are drawn from the same distribution.

* **Alternative hypothesis (H1):**
  The two samples come from different distributions.

---

## Method

The permutation test works as follows:

1. Compute the observed test statistic (difference in sample means).
2. Pool the two samples together.
3. Randomly shuffle (permute) the combined data.
4. Split into two new groups of the same size.
5. Recompute the test statistic.
6. Repeat many times to construct an empirical null distribution.
7. Compute the p-value as the proportion of permuted statistics more extreme than the observed one.

---

## Key Idea (Non-parametric Intuition)

* The test does **not assume any specific distribution** (e.g., Gaussian).
* It relies on **exchangeability under H0**:
  if H0 is true, group labels can be arbitrarily reassigned.
* The null distribution is constructed **directly from the data** via resampling.

---

## Connection to Causal Thinking

Permutation tests are closely related to **randomization tests** in causal inference:

* Shuffling labels ≈ simulating random treatment assignment
* The null distribution ≈ counterfactual world under no effect

This makes permutation tests conceptually aligned with causal reasoning.

---

## Usage

Run the script:

```bash
python permutation_test_demo.py
```

Example output:

```text
Observed statistic: -0.48
p-value: 0.03
```

---

## File Structure

```text
permutation_test_demo.py   # main implementation
```

---

## Notes

* The test statistic used here is the **difference in means**.
* The implementation uses a **finite-sample correction** for p-value computation.
* Increasing the number of permutations improves estimation accuracy.

---
