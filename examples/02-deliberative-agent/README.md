# Deliberative Agent: A* Pathfinding

## Overview

This example demonstrates a **goal-based deliberative agent** that uses planning and search to achieve objectives. Unlike reactive agents, deliberative agents think ahead before acting.

## What is a Deliberative Agent?

A deliberative agent:
- **Has explicit goals** (e.g., "reach destination")
- **Plans ahead** by searching through possible action sequences
- **Reasons about future states** (consequence of actions)
- **Optimizes** for cost, time, or other objectives
- **Considers multiple steps** before taking first action

### Structure

```
Current State + Goal
        ↓
    Search Algorithm (A*)
        ↓
    Complete Path Plan
        ↓
Execute First Action
        ↓
    Repeat (re-plan if needed)
```

## The A* Pathfinding Example

This example implements an agent that:
1. **Perceives:** Knows its position and the grid map
2. **Goal:** Wants to reach a target location
3. **Plans:** Uses A* search to find optimal path
4. **Acts:** Follows the planned path step-by-step

### Why A* Search?

A* is an informed search algorithm that:
- **Complete:** Guaranteed to find a path if one exists
- **Optimal:** Finds the shortest path (with admissible heuristic)
- **Efficient:** Uses heuristics to guide search

**Formula:** `f(n) = g(n) + h(n)`
- `g(n)`: Actual cost from start to node n
- `h(n)`: Estimated cost from n to goal (heuristic)
- `f(n)`: Total estimated cost

## Real-World Applications

Deliberative agents with A* are used in:
- **GPS navigation** (Google Maps, Waze)
- **Game AI** (NPC pathfinding)
- **Robot navigation** (warehouse robots, vacuum cleaners)
- **Network routing** (finding optimal packet routes)
- **Logistics** (delivery route planning)

## Running the Example

```bash
cd examples/02-deliberative-agent
python deliberative_agent.py
```

The simulation will:
1. Display the grid map (obstacles, start, goal)
2. Show A* search in progress
3. Display the discovered optimal path
4. Animate the agent following the path

## Key Concepts Demonstrated

### 1. State Space Representation
The grid represents all possible states (positions) the agent can be in.

### 2. Search Tree Exploration
A* systematically explores possible paths, prioritizing promising ones.

### 3. Heuristic Function
Manhattan distance guides search toward the goal efficiently.

### 4. Optimality
A* finds the shortest path when using an admissible heuristic.

### 5. Planning Before Acting
The agent computes the entire path before moving.

## A* Algorithm Explained

### Key Components

1. **Open Set (Frontier):** Nodes to be evaluated
2. **Closed Set (Explored):** Nodes already evaluated
3. **g-score:** Actual cost from start
4. **h-score:** Heuristic estimate to goal
5. **f-score:** g + h (priority for expansion)

### Algorithm Steps

```
1. Add start node to open set
2. While open set is not empty:
   a. Get node with lowest f-score
   b. If it's the goal, reconstruct path and return
   c. Mark node as explored
   d. For each neighbor:
      - Calculate tentative g-score
      - If better than previous, update and add to open set
3. If open set empty, no path exists
```

### Heuristics

**Manhattan Distance** (used in grid worlds):
```
h(n) = |n.x - goal.x| + |n.y - goal.y|
```

**Euclidean Distance** (for continuous spaces):
```
h(n) = sqrt((n.x - goal.x)² + (n.y - goal.y)²)
```

**Why it works:** A* is optimal when h(n) ≤ actual_distance(n, goal) (admissible).

## Comparison: Reactive vs. Deliberative

| Aspect | Reactive (Example 01) | Deliberative (Example 02) |
|--------|----------------------|--------------------------|
| **Planning** | None | Full path planning |
| **Future** | Doesn't consider | Reasons about consequences |
| **Goal** | Implicit in rules | Explicit (reach destination) |
| **Optimality** | No guarantee | Optimal with A* |
| **Speed** | Instant response | Requires search time |
| **Complexity** | Simple | More complex |
| **Use case** | Quick reactions | Complex goal achievement |

## Limitations

Even deliberative agents have limitations:

- ❌ **Assumes static environment:** If obstacles move, plan becomes invalid
- ❌ **Computation time:** Large spaces require long planning
- ❌ **Perfect knowledge:** Assumes complete map information
- ❌ **No learning:** Doesn't improve from experience

Solutions in advanced agents:
- **Re-planning:** Recompute path when environment changes
- **Hierarchical planning:** Plan at multiple abstraction levels
- **Partial planning:** Plan only next few steps
- **Learning agents** (Example 03): Learn from experience

## Exercises

Try modifying the code to:

1. **Dynamic obstacles:** Add obstacles that move, requiring re-planning

2. **Different heuristics:** Compare Manhattan vs. Euclidean vs. Diagonal distance

3. **Weighted A*:** Use `f(n) = g(n) + w * h(n)` where w > 1 for faster (but suboptimal) paths

4. **Multiple goals:** Find path visiting several waypoints

5. **Moving target:** Goal changes position during navigation

6. **Different costs:** Some terrain costs more to traverse (mud, stairs, etc.)

## Comparison of Search Algorithms

| Algorithm | Complete? | Optimal? | Time Complexity | Space Complexity |
|-----------|-----------|----------|----------------|------------------|
| BFS | Yes | Yes* | O(b^d) | O(b^d) |
| DFS | No | No | O(b^m) | O(bm) |
| Dijkstra | Yes | Yes | O(b^d) | O(b^d) |
| **A*** | Yes | Yes* | O(b^d) | O(b^d) |
| Greedy | No | No | O(b^m) | O(b^m) |

\* Optimal with appropriate cost function/heuristic

**Why A* is superior:**
- As optimal as Dijkstra but faster (guided by heuristic)
- As fast as Greedy but optimal (uses actual cost too)

## Further Reading

- Russell & Norvig, "AI: A Modern Approach" - Chapter 3 (Search) & Chapter 4 (Informed Search)
- Hart, Nilsson, Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths" (1968) - Original A* paper
- Steven LaValle, "Planning Algorithms" - Comprehensive planning textbook (free online)

## Visualization

The example includes ASCII visualization:
```
Grid:
# = Obstacle
S = Start
G = Goal
. = Path
  = Empty space

Example output:
# # # # # #
S . . . . #
# # # . # #
# . . . . #
# . # # # #
# . . . . G
```

---

**Next:** Continue to [Example 03: Learning Agent](../03-learning-agent/) to see how agents can improve through experience using reinforcement learning.
