Toy Search Demo (A*) — fixed world vs. mechanism shift
=======================================================

1) What: a tiny A* search on a 6-node weighted directed graph.
2) Goal: show A* finds the lowest-cost path when the world (edges/costs) is fixed.
3) Run: `python astar_demo.py`
4) Output: prints the optimal path, total cost, and expansion order.
5) Graph: hard-coded in `GRAPH` and `H` (heuristic).
6) Assumption: edge costs and transitions do not change during/after planning.
7) Mechanism shift note: if the cost/transition mechanism changes, A*’s optimality guarantee no longer applies.
8) Try shift: run with `--shift` to simulate a changed edge cost after planning.
9) Expected: the previously “optimal” plan can become suboptimal under the new mechanism.
10) Files: `astar_demo.py`, this README.
