# Week 2 Exercise: Pathfinding with Obstacles

## Learning Objectives

- ✅ Understand deliberative agent architecture
- ✅ Implement A* search algorithm from scratch
- ✅ Design effective heuristic functions
- ✅ Handle dynamic obstacles
- ✅ Compare different search strategies

## Background

Review [Example 02: Deliberative Agent](../../examples/02-deliberative-agent/) and [docs/02-agent-types.md](../../docs/02-agent-types.md).

## Problem Statement

Implement a **delivery robot agent** that:
1. Navigates a warehouse grid to deliver packages
2. Plans optimal routes using A* search
3. Avoids obstacles (shelves, other robots)
4. Re-plans when obstacles move

### Requirements

**Part 1: A* Implementation (50 points)**
- Implement A* search from scratch (don't use libraries)
- Support Manhattan and Euclidean heuristics
- Return optimal path from start to goal

**Part 2: Dynamic Re-planning (30 points)**
- Detect when current path is blocked
- Re-plan new path around obstacles
- Track total planning time and path changes

**Part 3: Multiple Goals (20 points)**
- Visit multiple delivery points
- Find efficient order to visit them
- Minimize total distance traveled

## Starter Code

```python
class DeliveryRobotAgent:
    def a_star_search(self, start, goal, grid):
        # Implement A* algorithm
        pass
    
    def plan_multi_delivery(self, start, goals, grid):
        # Plan route visiting all goals
        pass
    
    def execute_with_replanning(self, grid):
        # Execute plan, re-plan if needed
        pass
```

## Test Cases

1. 10x10 grid with 20% obstacles
2. Goal at opposite corner
3. Path gets blocked mid-execution
4. Three delivery points to visit

## Hints

- Use `heapq` for priority queue
- Remember: `f(n) = g(n) + h(n)`
- Admissible heuristic: Never overestimates
- For multiple goals: Try nearest neighbor heuristic

**Solution:** See [solution2.py](solution2.py)
