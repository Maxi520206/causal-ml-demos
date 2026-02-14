#!/usr/bin/env python3

"""
A tiny A* demo on a small graph.

- Fixed world: A* returns an optimal path (given an admissible heuristic).
- Mechanism shift: if edge costs / transitions change after planning,
  the previously optimal plan can become suboptimal or infeasible.

Run:
  python astar_demo.py
  python astar_demo.py --shift
"""

from __future__ import annotations
import argparse
import heapq
from typing import Dict, List, Tuple, Optional


# -------------------------
# Problem setup (fixed world)
# -------------------------
# Directed weighted graph: GRAPH[u] = list of (v, cost)
GRAPH: Dict[str, List[Tuple[str, int]]] = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2), ("D", 5)],
    "B": [("D", 1), ("E", 3)],
    "C": [("G", 5)],
    "D": [("G", 2)],
    "E": [("G", 2)],
    "G": [],
}

START = "S"
GOAL = "G"

# Admissible heuristic h(n): never overestimates true remaining cost to G
# (These values are chosen to be <= true shortest-to-go.)
H: Dict[str, int] = {
    "S": 3,  # true optimal remaining from S is 5, so 3 is OK
    "A": 3,  # true remaining from A is 4, so 3 is OK
    "B": 2,  # true remaining from B is 3, so 2 is OK
    "C": 5,  # true remaining from C is 5
    "D": 2,  # true remaining from D is 2
    "E": 2,  # true remaining from E is 2
    "G": 0,
}


def astar(graph: Dict[str, List[Tuple[str, int]]], h: Dict[str, int], start: str, goal: str):
    """
    Standard A* graph search.

    Returns:
      path: List[str]
      cost: int
      expanded: List[str] (order of node expansions)
    """
    # priority queue items: (f, g, node)
    open_pq: List[Tuple[int, int, str]] = []
    heapq.heappush(open_pq, (h[start], 0, start))

    came_from: Dict[str, Optional[str]] = {start: None}
    best_g: Dict[str, int] = {start: 0}

    expanded: List[str] = []

    while open_pq:
        f, g, u = heapq.heappop(open_pq)

        # Skip stale entries
        if g != best_g.get(u, None):
            continue

        expanded.append(u)

        if u == goal:
            # reconstruct
            path = []
            cur = u
            while cur is not None:
                path.append(cur)
                cur = came_from[cur]
            path.reverse()
            return path, g, expanded

        for v, w in graph[u]:
            ng = g + w
            if ng < best_g.get(v, 10**18):
                best_g[v] = ng
                came_from[v] = u
                nf = ng + h[v]
                heapq.heappush(open_pq, (nf, ng, v))

    return None, None, expanded


def path_cost(graph: Dict[str, List[Tuple[str, int]]], path: List[str]) -> int:
    cost = 0
    for u, v in zip(path[:-1], path[1:]):
        for vv, w in graph[u]:
            if vv == v:
                cost += w
                break
        else:
            raise ValueError(f"Edge {u}->{v} not found")
    return cost


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shift", action="store_true", help="simulate a mechanism shift after planning")
    args = ap.parse_args()

    # 1) Plan in the fixed world
    path, cost, expanded = astar(GRAPH, H, START, GOAL)
    print("== Fixed world planning (A*) ==")
    print("Expanded order:", " -> ".join(expanded))
    print("Best path:", " -> ".join(path))
    print("Total cost:", cost)

    # One-sentence causal comment (the assignment requirement)
    print("\nCausal comment (1 sentence):")
    print("A*’s optimality relies on a fixed transition-and-cost mechanism; if that mechanism shifts, the computed plan may no longer be optimal (or even feasible).")

    # 2) Optional: simulate mechanism shift (cost changes after planning)
    if args.shift:
        shifted = {u: list(edges) for u, edges in GRAPH.items()}
        # Mechanism shift: increase the cost of D->G (e.g., traffic jam / new rule)
        shifted["D"] = [("G", 10)]
        print("\n== After mechanism shift (edge cost changes) ==")
        print("Shift: cost(D->G) becomes 10 (was 2).")

        new_cost = path_cost(shifted, path)
        print("Old planned path cost under new mechanism:", new_cost)

        new_path, new_best, new_expanded = astar(shifted, H, START, GOAL)
        print("Replan expanded order:", " -> ".join(new_expanded))
        print("Replanned best path:", " -> ".join(new_path))
        print("Replanned total cost:", new_best)

        if new_best < new_cost:
            print("\nObservation: the old plan is now suboptimal due to the mechanism shift.")
        else:
            print("\nObservation: the old plan remained optimal in this particular shift (not guaranteed in general).")


if __name__ == "__main__":
    main()
