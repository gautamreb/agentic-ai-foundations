"""
Deliberative Agent: A* Pathfinding

This example demonstrates a goal-based deliberative agent that uses the A*
search algorithm to find optimal paths in a grid world with obstacles.

Key Concepts:
- Deliberative agent architecture (explicit goals, planning)
- A* search algorithm
- Heuristic functions
- Optimal pathfinding
- State space search

Author: Agentic AI Foundations
License: MIT
"""

import heapq
import time
from typing import List, Tuple, Optional, Set


class GridWorld:
    """
    A 2D grid environment with obstacles.
    
    The agent can move in 4 directions: up, down, left, right.
    Some cells are blocked (obstacles).
    """
    
    def __init__(self, width: int, height: int, obstacles: Set[Tuple[int, int]]):
        """
        Initialize the grid world.
        
        Args:
            width: Grid width
            height: Grid height
            obstacles: Set of (x, y) positions that are blocked
        """
        self.width = width
        self.height = height
        self.obstacles = obstacles
    
    def is_valid(self, x: int, y: int) -> bool:
        """
        Check if a position is valid (within bounds and not an obstacle).
        
        Args:
            x, y: Position to check
            
        Returns:
            bool: True if position is valid
        """
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                (x, y) not in self.obstacles)
    
    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Get valid neighboring positions (up, down, left, right).
        
        Args:
            x, y: Current position
            
        Returns:
            List of valid (x, y) neighbor positions
        """
        # Four possible moves: up, down, left, right
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        neighbors = []
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid(new_x, new_y):
                neighbors.append((new_x, new_y))
        
        return neighbors
    
    def display(self, path: Optional[List[Tuple[int, int]]] = None, 
                start: Optional[Tuple[int, int]] = None,
                goal: Optional[Tuple[int, int]] = None):
        """
        Display the grid world with obstacles and optional path.
        
        Args:
            path: Optional path to highlight
            start: Start position
            goal: Goal position
        """
        path_set = set(path) if path else set()
        
        print("\nGrid World:")
        print("  " + "".join([str(i % 10) for i in range(self.width)]))
        
        for y in range(self.height - 1, -1, -1):  # Display top to bottom
            row = f"{y} "
            for x in range(self.width):
                pos = (x, y)
                if pos == start:
                    row += "S"  # Start
                elif pos == goal:
                    row += "G"  # Goal
                elif pos in self.obstacles:
                    row += "#"  # Obstacle
                elif pos in path_set:
                    row += "·"  # Path
                else:
                    row += " "  # Empty
            print(row)
        print()


class AStarAgent:
    """
    Deliberative agent using A* search algorithm for pathfinding.
    
    This agent:
    1. Perceives the current state (position) and goal
    2. Plans an optimal path using A* search
    3. Executes the plan step by step
    
    Unlike reactive agents, this agent:
    - Has explicit goals
    - Plans entire path before moving
    - Considers future consequences of actions
    - Optimizes for shortest path
    """
    
    def __init__(self, grid: GridWorld):
        """
        Initialize the A* pathfinding agent.
        
        Args:
            grid: The GridWorld environment
        """
        self.grid = grid
        self.current_position = None
        self.goal_position = None
        self.planned_path = None
    
    def heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        """
        Heuristic function: Manhattan distance to goal.
        
        Manhattan distance is the sum of absolute differences in coordinates.
        It's admissible (never overestimates) for 4-directional movement.
        
        h(n) = |n.x - goal.x| + |n.y - goal.y|
        
        Args:
            pos: Current position (x, y)
            goal: Goal position (x, y)
            
        Returns:
            float: Estimated distance to goal
        """
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def search(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        A* search algorithm to find optimal path from start to goal.
        
        A* uses the evaluation function:
            f(n) = g(n) + h(n)
        where:
            g(n) = actual cost from start to n
            h(n) = estimated cost from n to goal (heuristic)
            f(n) = estimated total cost
        
        The algorithm explores nodes with lowest f(n) first.
        
        Args:
            start: Starting position (x, y)
            goal: Goal position (x, y)
            
        Returns:
            List of positions from start to goal, or None if no path exists
        """
        print(f"\n🔍 A* Search: Planning path from {start} to {goal}")
        print("-" * 60)
        
        # Priority queue: stores (f_score, counter, position)
        # Counter ensures consistent ordering when f_scores are equal
        open_set = []
        counter = 0
        
        # g_score: actual cost from start to each node
        g_score = {start: 0}
        
        # f_score: g_score + heuristic (estimated total cost)
        f_score = {start: self.heuristic(start, goal)}
        
        # Track where each node came from (for path reconstruction)
        came_from = {}
        
        # Nodes we've already explored
        closed_set = set()
        
        # Add start to open set
        heapq.heappush(open_set, (f_score[start], counter, start))
        counter += 1
        
        nodes_explored = 0
        
        # Main search loop
        while open_set:
            # Get node with lowest f_score
            current_f, _, current = heapq.heappop(open_set)
            nodes_explored += 1
            
            # Have we reached the goal?
            if current == goal:
                print(f"✅ Path found! Explored {nodes_explored} nodes")
                path = self._reconstruct_path(came_from, current)
                print(f"📏 Path length: {len(path)} steps")
                return path
            
            # Mark as explored
            closed_set.add(current)
            
            if nodes_explored % 10 == 0:
                print(f"   Exploring node {nodes_explored}: {current}, f={current_f:.1f}")
            
            # Explore neighbors
            for neighbor in self.grid.get_neighbors(current[0], current[1]):
                # Skip if already explored
                if neighbor in closed_set:
                    continue
                
                # Calculate tentative g_score
                # Cost of moving to neighbor is 1 (uniform cost)
                tentative_g = g_score[current] + 1
                
                # Is this a better path to neighbor?
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # Yes! Update the path
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    
                    # Add to open set (if not already there)
                    heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))
                    counter += 1
        
        # Open set is empty and we didn't find goal
        print(f"❌ No path found! Explored {nodes_explored} nodes")
        return None
    
    def _reconstruct_path(self, came_from: dict, current: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Reconstruct path from start to goal using came_from map.
        
        Args:
            came_from: Map of {node: previous_node}
            current: The goal node
            
        Returns:
            List of positions from start to goal
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()  # Start to goal
        return path
    
    def plan_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> bool:
        """
        Plan a path from start to goal.
        
        This is the DELIBERATION phase - the agent thinks ahead
        about the entire sequence of actions before taking any.
        
        Args:
            start: Starting position
            goal: Goal position
            
        Returns:
            bool: True if path found
        """
        self.current_position = start
        self.goal_position = goal
        self.planned_path = self.search(start, goal)
        
        return self.planned_path is not None
    
    def execute_path(self, step_delay: float = 0.5):
        """
        Execute the planned path step by step.
        
        This demonstrates the deliberative agent's approach:
        1. Plan entire path first (deliberation)
        2. Execute the plan (action)
        
        Args:
            step_delay: Delay between steps (seconds) for visualization
        """
        if not self.planned_path:
            print("❌ No path to execute!")
            return
        
        print("\n" + "=" * 60)
        print("EXECUTING PLANNED PATH")
        print("=" * 60)
        
        for i, position in enumerate(self.planned_path):
            self.current_position = position
            
            print(f"\nStep {i + 1}/{len(self.planned_path)}: Moving to {position}")
            
            # Display current state
            self.grid.display(
                path=self.planned_path[:i+1],
                start=self.planned_path[0],
                goal=self.goal_position
            )
            
            if step_delay > 0:
                time.sleep(step_delay)
        
        print("✅ Goal reached!")
        print("=" * 60)


def create_example_grid() -> GridWorld:
    """
    Create an example grid world with obstacles.
    
    Grid layout (10x8):
    - Several walls and obstacles
    - Multiple possible paths
    - Requires intelligent pathfinding
    """
    width, height = 10, 8
    
    # Define obstacles (walls)
    obstacles = {
        # Vertical walls
        (2, 1), (2, 2), (2, 3), (2, 4),
        (5, 2), (5, 3), (5, 4), (5, 5),
        (7, 1), (7, 2), (7, 3),
        
        # Horizontal wall
        (3, 5), (4, 5), (6, 5),
        
        # Random obstacles
        (1, 6), (8, 6), (4, 1)
    }
    
    return GridWorld(width, height, obstacles)


def main():
    """
    Demonstrate the A* deliberative agent.
    """
    print("=" * 60)
    print("DELIBERATIVE AGENT: A* PATHFINDING")
    print("=" * 60)
    
    # Create environment
    grid = create_example_grid()
    
    # Create agent
    agent = AStarAgent(grid)
    
    # Define start and goal
    start = (0, 0)  # Bottom-left corner
    goal = (9, 7)   # Top-right corner
    
    # Display initial grid
    print("\nInitial Grid:")
    grid.display(start=start, goal=goal)
    
    print("\nAgent initialized. Starting deliberation...")
    print(f"Start: {start}")
    print(f"Goal:  {goal}")
    
    # DELIBERATION PHASE: Plan the path
    success = agent.plan_path(start, goal)
    
    if success:
        # Display planned path
        print("\nPlanned path:")
        grid.display(path=agent.planned_path, start=start, goal=goal)
        
        # EXECUTION PHASE: Follow the plan
        agent.execute_path(step_delay=0.3)
        
        # Analysis
        print("\n📊 Path Analysis:")
        print(f"Total steps: {len(agent.planned_path)}")
        print(f"Optimal: Yes (A* guarantees optimality with admissible heuristic)")
        
    else:
        print("\n❌ Failed to find a path to the goal!")
        print("This could happen if:")
        print("- Goal is surrounded by obstacles")
        print("- No valid path exists")
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("✅ Deliberative agents plan before acting")
    print("✅ A* efficiently finds optimal paths")
    print("✅ Heuristics guide search toward goal")
    print("✅ Planning enables achieving complex goals")
    print("=" * 60)


if __name__ == "__main__":
    main()
