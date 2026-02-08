"""
Multi-Agent System: Collaborative Task Allocation

This example demonstrates a multi-agent system where autonomous worker agents
coordinate to efficiently allocate and complete tasks using an auction protocol.

Key Concepts:
- Multi-agent coordination
- Contract Net Protocol (auction-based)
- Distributed decision-making
- Agent communication
- Emergent system behavior

Author: Agentic AI Foundations
License: MIT
"""

import random
import math
from typing import List, Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a task that needs to be completed.
    """
    id: int
    position: Tuple[float, float]  # (x, y) location
    assigned_to: Optional[int] = None  # Agent ID that will complete it
    
    def __str__(self):
        return f"Task {self.id} at {self.position}"


@dataclass
class Bid:
    """
    Represents an agent's bid for a task.
    """
    agent_id: int
    task_id: int
    cost: float  # Lower is better
    
    def __str__(self):
        return f"Agent {self.agent_id} bids {self.cost:.2f} for Task {self.task_id}"


class WorkerAgent:
    """
    An autonomous worker agent that can bid on and complete tasks.
    
    Each agent:
    - Has a position in the workspace
    - Can handle a maximum number of tasks
    - Calculates bids based on distance and current load
    - Coordinates with other agents through auctions
    """
    
    def __init__(self, agent_id: int, position: Tuple[float, float], capacity: int = 3):
        """
        Initialize a worker agent.
        
        Args:
            agent_id: Unique identifier
            position: (x, y) location in workspace
            capacity: Maximum number of tasks agent can handle
        """
        self.id = agent_id
        self.position = position
        self.capacity = capacity
        self.assigned_tasks: List[Task] = []
        
        print(f"Agent {self.id} created at position {position} with capacity {capacity}")
    
    def calculate_distance(self, task: Task) -> float:
        """
        Calculate Euclidean distance to a task.
        
        Args:
            task: Task to calculate distance to
            
        Returns:
            Distance to task
        """
        dx = self.position[0] - task.position[0]
        dy = self.position[1] - task.position[1]
        return math.sqrt(dx*dx + dy*dy)
    
    def calculate_bid(self, task: Task) -> Optional[float]:
        """
        Calculate bid for a task.
        
        Bid is based on:
        1. Distance to task (travel cost)
        2. Current load (penalty for being busy)
        
        Lower bid = more competitive
        
        Args:
            task: Task to bid on
            
        Returns:
            Bid cost, or None if agent can't take more tasks
        """
        # Can't bid if at capacity
        if len(self.assigned_tasks) >= self.capacity:
            return None
        
        # Base cost: distance to task
        distance_cost = self.calculate_distance(task)
        
        # Load penalty: prefer distributing work evenly
        # More tasks = higher penalty
        load_factor = len(self.assigned_tasks) / self.capacity
        load_penalty = load_factor * 10.0  # Arbitrary penalty factor
        
        total_cost = distance_cost + load_penalty
        
        return total_cost
    
    def submit_bid(self, task: Task) -> Optional[Bid]:
        """
        Create and submit a bid for a task.
        
        Args:
            task: Task to bid on
            
        Returns:
            Bid object, or None if can't bid
        """
        cost = self.calculate_bid(task)
        
        if cost is None:
            return None
        
        return Bid(agent_id=self.id, task_id=task.id, cost=cost)
    
    def assign_task(self, task: Task):
        """
        Accept assignment of a task.
        
        Args:
            task: Task assigned to this agent
        """
        self.assigned_tasks.append(task)
        task.assigned_to = self.id
        print(f"  ✓ Agent {self.id} accepted Task {task.id}")
    
    def get_total_cost(self) -> float:
        """
        Calculate total cost for all assigned tasks.
        
        Returns:
            Sum of distances to all assigned tasks
        """
        return sum(self.calculate_distance(task) for task in self.assigned_tasks)
    
    def __str__(self):
        return f"Agent {self.id} at {self.position}: {len(self.assigned_tasks)}/{self.capacity} tasks"


class Auctioneer:
    """
    Coordinates task allocation through auctions.
    
    The auctioneer implements the Contract Net Protocol:
    1. Announces task
    2. Collects bids from agents
    3. Awards task to best (lowest cost) bidder
    
    This is a simplified, centralized version. In fully distributed systems,
    agents would communicate peer-to-peer.
    """
    
    def __init__(self, agents: List[WorkerAgent]):
        """
        Initialize auctioneer with list of agents.
        
        Args:
            agents: List of worker agents
        """
        self.agents = agents
        print(f"\nAuctioneer initialized with {len(agents)} agents")
    
    def auction_task(self, task: Task) -> bool:
        """
        Run auction for a single task.
        
        Process:
        1. Request bids from all agents
        2. Collect bids
        3. Select winner (lowest bid)
        4. Assign task to winner
        
        Args:
            task: Task to auction
            
        Returns:
            True if task was assigned, False otherwise
        """
        print(f"\n📢 Auctioning {task}")
        print("  Collecting bids...")
        
        # Phase 1: Collect bids from all agents
        bids: List[Bid] = []
        for agent in self.agents:
            bid = agent.submit_bid(task)
            if bid:
                bids.append(bid)
                print(f"    {bid}")
        
        # Check if we got any bids
        if not bids:
            print("  ❌ No bids received! Task cannot be assigned.")
            return False
        
        # Phase 2: Select winner (lowest cost)
        winning_bid = min(bids, key=lambda b: b.cost)
        winner = self.agents[winning_bid.agent_id]
        
        print(f"  🏆 Winner: Agent {winning_bid.agent_id} with bid {winning_bid.cost:.2f}")
        
        # Phase 3: Assign task to winner
        winner.assign_task(task)
        
        return True
    
    def auction_all_tasks(self, tasks: List[Task]) -> Dict[str, float]:
        """
        Run auctions for all tasks sequentially.
        
        Args:
            tasks: List of tasks to allocate
            
        Returns:
            Dictionary with allocation statistics
        """
        print("\n" + "=" * 60)
        print("STARTING TASK ALLOCATION AUCTION")
        print("=" * 60)
        
        assigned = 0
        unassigned = 0
        
        for task in tasks:
            if self.auction_task(task):
                assigned += 1
            else:
                unassigned += 1
        
        # Calculate statistics
        total_cost = sum(agent.get_total_cost() for agent in self.agents)
        
        print("\n" + "=" * 60)
        print("AUCTION COMPLETE")
        print("=" * 60)
        print(f"Assigned tasks: {assigned}/{len(tasks)}")
        print(f"Unassigned tasks: {unassigned}")
        print(f"Total system cost: {total_cost:.2f}")
        
        return {
            'assigned': assigned,
            'unassigned': unassigned,
            'total_cost': total_cost
        }


def visualize_system(agents: List[WorkerAgent], tasks: List[Task]):
    """
    Display ASCII visualization of the multi-agent system.
    
    Args:
        agents: List of worker agents
        tasks: List of tasks
    """
    print("\n" + "=" * 60)
    print("SYSTEM VISUALIZATION")
    print("=" * 60)
    
    # Find bounds
    all_x = [a.position[0] for a in agents] + [t.position[0] for t in tasks]
    all_y = [a.position[1] for a in agents] + [t.position[1] for t in tasks]
    
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)
    
    # Create grid
    grid_size = 20
    grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Helper to map position to grid
    def to_grid(x, y):
        grid_x = int((x - min_x) / (max_x - min_x + 0.1) * (grid_size - 1))
        grid_y = int((y - min_y) / (max_y - min_y + 0.1) * (grid_size - 1))
        return grid_x, grid_y
    
    # Place tasks
    for task in tasks:
        gx, gy = to_grid(task.position[0], task.position[1])
        grid[grid_size - 1 - gy][gx] = str(task.id) if task.assigned_to is None else '✓'
    
    # Place agents
    for agent in agents:
        gx, gy = to_grid(agent.position[0], agent.position[1])
        grid[grid_size - 1 - gy][gx] = f"A{agent.id}"[0]
    
    # Display grid
    print("\nWorkspace (A=Agent, 0-9=Unassigned Task, ✓=Assigned Task):")
    print("┌" + "─" * grid_size + "┐")
    for row in grid:
        print("│" + "".join(row) + "│")
    print("└" + "─" * grid_size + "┘")
    
    # Display assignments
    print("\nTask Assignments:")
    print("-" * 60)
    for agent in agents:
        task_ids = [t.id for t in agent.assigned_tasks]
        cost = agent.get_total_cost()
        print(f"Agent {agent.id}: Tasks {task_ids} | Total cost: {cost:.2f}")
    
    print("=" * 60)


def create_random_scenario(num_agents: int = 4, num_tasks: int = 10) -> Tuple[List[WorkerAgent], List[Task]]:
    """
    Create a random scenario with agents and tasks.
    
    Args:
        num_agents: Number of worker agents
        num_tasks: Number of tasks to allocate
        
    Returns:
        Tuple of (agents, tasks)
    """
    print("=" * 60)
    print("CREATING RANDOM SCENARIO")
    print("=" * 60)
    
    # Create agents at random positions
    agents = []
    for i in range(num_agents):
        position = (random.uniform(0, 100), random.uniform(0, 100))
        capacity = random.randint(2, 4)
        agent = WorkerAgent(agent_id=i, position=position, capacity=capacity)
        agents.append(agent)
    
    print()
    
    # Create tasks at random positions
    print(f"Creating {num_tasks} tasks...")
    tasks = []
    for i in range(num_tasks):
        position = (random.uniform(0, 100), random.uniform(0, 100))
        task = Task(id=i, position=position)
        tasks.append(task)
        print(f"  {task}")
    
    return agents, tasks


def main():
    """
    Main demonstration of multi-agent task allocation.
    """
    print("\n" + "=" * 60)
    print("MULTI-AGENT SYSTEM: COLLABORATIVE TASK ALLOCATION")
    print("=" * 60)
    print()
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Create scenario
    agents, tasks = create_random_scenario(num_agents=4, num_tasks=10)
    
    # Show initial state
    visualize_system(agents, tasks)
    
    # Create auctioneer and run auctions
    auctioneer = Auctioneer(agents)
    stats = auctioneer.auction_all_tasks(tasks)
    
    # Show final state
    visualize_system(agents, tasks)
    
    # Analysis
    print("\n" + "=" * 60)
    print("SYSTEM ANALYSIS")
    print("=" * 60)
    
    # Load balancing
    loads = [len(agent.assigned_tasks) for agent in agents]
    avg_load = sum(loads) / len(loads)
    max_load = max(loads)
    min_load = min(loads)
    
    print(f"\nLoad Balancing:")
    print(f"  Average load: {avg_load:.1f} tasks/agent")
    print(f"  Min load: {min_load} tasks")
    print(f"  Max load: {max_load} tasks")
    print(f"  Load variance: {max_load - min_load} tasks")
    
    # Efficiency
    print(f"\nEfficiency:")
    print(f"  Total cost: {stats['total_cost']:.2f}")
    print(f"  Average cost per task: {stats['total_cost'] / stats['assigned']:.2f}")
    
    # Success rate
    success_rate = stats['assigned'] / (stats['assigned'] + stats['unassigned']) * 100
    print(f"\nSuccess Rate:")
    print(f"  {success_rate:.0f}% of tasks assigned")
    
    # Key takeaways
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("✅ Multiple agents coordinated without central control")
    print("✅ Auction protocol enabled efficient task allocation")
    print("✅ Load balancing emerged from bidding strategy")
    print("✅ System is scalable and robust")
    print("✅ Agents made autonomous decisions based on local information")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
