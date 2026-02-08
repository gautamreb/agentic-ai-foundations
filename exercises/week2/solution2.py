"""
Week 2 Exercise Solution: Delivery Robot with A* Pathfinding

Demonstrates deliberative agent using A* for warehouse navigation.

Author: Agentic AI Foundations
"""

import heapq
from typing import List, Tuple, Optional, Set


class DeliveryRobotAgent:
    """Deliberative agent for warehouse package delivery."""
    
    def __init__(self, grid_size: Tuple[int, int]):
        self.grid_width, self.grid_height = grid_size
        self.current_pos = None
        self.planned_path = None
    
    def heuristic_manhattan(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        """Manhattan distance heuristic."""
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def heuristic_euclidean(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        """Euclidean distance heuristic."""
        return ((pos[0] - goal[0])**2 + (pos[1] - goal[1])**2)**0.5
    
    def get_neighbors(self, pos: Tuple[int, int], obstacles: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions."""
        x, y = pos
        neighbors = []
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.grid_width and 
                0 <= new_y < self.grid_height and
                (new_x, new_y) not in obstacles):
                neighbors.append((new_x, new_y))
        return neighbors
    
    def a_star_search(self, start: Tuple[int, int], goal: Tuple[int, int], 
                     obstacles: Set[Tuple[int, int]], 
                     heuristic='manhattan') -> Optional[List[Tuple[int, int]]]:
        """
        A* pathfinding algorithm.
        
        Args:
            start: Starting position
            goal: Goal position
            obstacles: Set of blocked positions
            heuristic: 'manhattan' or 'euclidean'
        
        Returns:
            Path from start to goal, or None if no path exists
        """
        h_func = self.heuristic_manhattan if heuristic == 'manhattan' else self.heuristic_euclidean
        
        open_set = []
        heapq.heappush(open_set, (0, 0, start))  # (f_score, counter, position)
        counter = 1
        
        came_from = {}
        g_score = {start: 0}
        f_score = {start: h_func(start, goal)}
        
        while open_set:
            _, _, current = heapq.heappop(open_set)
            
            if current == goal:
                # Reconstruct path
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return list(reversed(path))
            
            for neighbor in self.get_neighbors(current, obstacles):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + h_func(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))
                    counter += 1
        
        return None  # No path found
    
    def plan_multi_delivery(self, start: Tuple[int, int], 
                          goals: List[Tuple[int, int]], 
                          obstacles: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """
        Plan route to visit multiple delivery points.
        Uses greedy nearest-neighbor heuristic.
        
        Returns:
            Complete path visiting all goals
        """
        complete_path = []
        current = start
        remaining_goals = goals.copy()
        
        while remaining_goals:
            # Find nearest goal
            nearest_goal = min(remaining_goals, 
                             key=lambda g: self.heuristic_manhattan(current, g))
            
            # Plan path to nearest goal
            path_segment = self.a_star_search(current, nearest_goal, obstacles)
            if path_segment:
                complete_path.extend(path_segment[1:] if complete_path else path_segment)
                current = nearest_goal
                remaining_goals.remove(nearest_goal)
            else:
                print(f"Warning: No path to {nearest_goal}")
                remaining_goals.remove(nearest_goal)
        
        return complete_path


def demonstrate():
    """Demonstrate the delivery robot agent."""
    print("=" * 60)
    print("WEEK 2 SOLUTION: DELIVERY ROBOT WITH A*")
    print("=" * 60)
    
    # Create 10x10 grid
    agent = DeliveryRobotAgent((10, 10))
    
    # Define obstacles (warehouse shelves)
    obstacles = {(2,i) for i in range(1, 8)} | {(5,i) for i in range(2, 9)} | {(7,i) for i in range(1, 6)}
    
    # Single delivery test
    start = (0, 0)
    goal = (9, 9)
    
    print(f"\nTest 1: Single delivery from {start} to {goal}")
    path = agent.a_star_search(start, goal, obstacles)
    if path:
        print(f"Path found! Length: {len(path)} steps")
        print(f"Path: {path[:5]}...{path[-5:]}")
    
    # Multiple delivery test
    goals = [(9, 9), (0, 9), (9, 0)]
    print(f"\nTest 2: Multiple deliveries to {goals}")
    multi_path = agent.plan_multi_delivery(start, goals, obstacles)
    print(f"Complete route length: {len(multi_path)} steps")
    
    print("\n" + "=" * 60)
    print("✅ Deliberative planning enables optimal pathfinding")
    print("✅ A* efficiently finds shortest paths")
    print("✅ Heuristics guide search toward goal")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate()
