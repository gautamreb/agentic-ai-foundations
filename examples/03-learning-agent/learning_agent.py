"""
Learning Agent: Q-Learning in GridWorld

This example demonstrates a reinforcement learning agent that learns to navigate
a grid world through trial and error using the Q-learning algorithm.

Key Concepts:
- Reinforcement learning (learning from rewards)
- Q-learning algorithm
- Exploration vs. exploitation (ε-greedy)
- Temporal difference learning
- Value function convergence

Author: Agentic AI Foundations
License: MIT
"""

import random
import numpy as np
from collections import defaultdict
from typing import Tuple, List, Dict
import time


class GridWorldEnv:
    """
    GridWorld environment for reinforcement learning.
    
    The agent starts at a position and must reach the goal while avoiding pits.
    - Goal: +10 reward, episode ends
    - Pits: -10 reward, episode ends
    - Each step: -1 reward (encourages efficiency)
    """
    
    def __init__(self, width: int = 5, height: int = 5):
        """
        Initialize GridWorld environment.
        
        Args:
            width: Grid width
            height: Grid height
        """
        self.width = width
        self.height = height
        
        # Define special cells
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
        
        # Pits (obstacles that end episode with negative reward)
        self.pits = {(1, 1), (2, 2), (3, 1)}
        
        # Current agent position
        self.agent_pos = self.start
        
        # Action space: up, down, left, right
        self.actions = ['up', 'down', 'left', 'right']
        
    def reset(self) -> Tuple[int, int]:
        """
        Reset environment to start state.
        
        Returns:
            Initial state (position)
        """
        self.agent_pos = self.start
        return self.agent_pos
    
    def step(self, action: str) -> Tuple[Tuple[int, int], float, bool]:
        """
        Execute action and return result.
        
        Args:
            action: Action to take ('up', 'down', 'left', 'right')
            
        Returns:
            Tuple of (next_state, reward, done)
        """
        x, y = self.agent_pos
        
        # Calculate next position based on action
        if action == 'up':
            y = min(y + 1, self.height - 1)
        elif action == 'down':
            y = max(y - 1, 0)
        elif action == 'left':
            x = max(x - 1, 0)
        elif action == 'right':
            x = min(x + 1, self.width - 1)
        
        next_pos = (x, y)
        self.agent_pos = next_pos
        
        # Determine reward and whether episode is done
        if next_pos == self.goal:
            reward = 10.0
            done = True
        elif next_pos in self.pits:
            reward = -10.0
            done = True
        else:
            reward = -1.0  # Small penalty for each step (encourages efficiency)
            done = False
        
        return next_pos, reward, done
    
    def display(self, q_agent=None):
        """
        Display the grid world.
        
        Args:
            q_agent: Optional QLearningAgent to show policy arrows
        """
        print("\nGrid World:")
        print("  " + "".join([str(i) for i in range(self.width)]))
        
        for y in range(self.height - 1, -1, -1):
            row = f"{y} "
            for x in range(self.width):
                pos = (x, y)
                if pos == self.agent_pos:
                    row += "A"  # Agent
                elif pos == self.goal:
                    row += "G"  # Goal
                elif pos in self.pits:
                    row += "X"  # Pit
                elif q_agent:
                    # Show best action as arrow
                    best_action = q_agent.get_best_action(pos)
                    arrow_map = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
                    row += arrow_map.get(best_action, "·")
                else:
                    row += "·"  # Empty
            print(row)
        print()


class QLearningAgent:
    """
    Q-Learning agent that learns optimal policy through experience.
    
    Q-learning is a model-free, off-policy RL algorithm that learns
    a Q-function: Q(state, action) → expected cumulative reward
    
    Update rule:
        Q(s, a) ← Q(s, a) + α[r + γ max_a' Q(s', a') - Q(s, a)]
    """
    
    def __init__(self, 
                 actions: List[str],
                 learning_rate: float = 0.1,
                 discount_factor: float = 0.9,
                 epsilon: float = 0.1):
        """
        Initialize Q-Learning agent.
        
        Args:
            actions: List of possible actions
            learning_rate (α): How much to update Q-values (0-1)
            discount_factor (γ): How much to value future rewards (0-1)
            epsilon (ε): Exploration probability (0-1)
        """
        self.actions = actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        
        # Q-table: Q(state, action) → expected reward
        # Using defaultdict for automatic initialization to 0
        self.q_table: Dict[Tuple[Tuple[int, int], str], float] = defaultdict(float)
        
        # Statistics
        self.episode_rewards = []
        
        print(f"Q-Learning Agent initialized:")
        print(f"  Learning rate (α): {self.lr}")
        print(f"  Discount factor (γ): {self.gamma}")
        print(f"  Exploration rate (ε): {self.epsilon}")
        print()
    
    def get_q_value(self, state: Tuple[int, int], action: str) -> float:
        """
        Get Q-value for state-action pair.
        
        Args:
            state: Current state
            action: Action to evaluate
            
        Returns:
            Q-value (estimated future reward)
        """
        return self.q_table[(state, action)]
    
    def get_best_action(self, state: Tuple[int, int]) -> str:
        """
        Get action with highest Q-value for given state (greedy policy).
        
        This is the EXPLOITATION step - using learned knowledge.
        
        Args:
            state: Current state
            
        Returns:
            Best action according to Q-values
        """
        q_values = [self.get_q_value(state, action) for action in self.actions]
        max_q = max(q_values)
        
        # If multiple actions have same max Q, choose randomly among them
        best_actions = [action for action, q in zip(self.actions, q_values) 
                       if q == max_q]
        
        return random.choice(best_actions)
    
    def choose_action(self, state: Tuple[int, int]) -> str:
        """
        Choose action using ε-greedy policy.
        
        ε-greedy balances exploration and exploitation:
        - With probability ε: explore (random action)
        - With probability 1-ε: exploit (best action)
        
        Args:
            state: Current state
            
        Returns:
            Chosen action
        """
        if random.random() < self.epsilon:
            # EXPLORE: Random action
            return random.choice(self.actions)
        else:
            # EXPLOIT: Best known action
            return self.get_best_action(state)
    
    def learn(self, 
              state: Tuple[int, int], 
              action: str, 
              reward: float, 
              next_state: Tuple[int, int], 
              done: bool):
        """
        Update Q-value using Q-learning update rule.
        
        Q-learning update (Temporal Difference learning):
            Q(s, a) ← Q(s, a) + α[r + γ max_a' Q(s', a') - Q(s, a)]
        
        Where:
            - α (learning_rate): How much to update
            - r (reward): Immediate reward
            - γ (discount_factor): Future reward importance
            - max_a' Q(s', a'): Best possible future value
            - Q(s, a): Current estimate
        
        Args:
            state: Current state
            action: Action taken
            reward: Reward received
            next_state: Resulting state
            done: Whether episode ended
        """
        # Current Q-value estimate
        current_q = self.get_q_value(state, action)
        
        if done:
            # If episode ended, there's no future reward
            target_q = reward
        else:
            # Otherwise, estimate future rewards
            # max_a' Q(next_state, a') = best possible future value
            next_max_q = max([self.get_q_value(next_state, a) for a in self.actions])
            target_q = reward + self.gamma * next_max_q
        
        # Temporal Difference (TD) error
        td_error = target_q - current_q
        
        # Update Q-value
        new_q = current_q + self.lr * td_error
        self.q_table[(state, action)] = new_q
    
    def train(self, env: GridWorldEnv, num_episodes: int = 1000, verbose: bool = True):
        """
        Train the agent through multiple episodes.
        
        Each episode:
        1. Reset environment
        2. Until done:
           a. Choose action (ε-greedy)
           b. Take action, observe result
           c. Learn from experience (update Q-values)
        
        Args:
            env: GridWorld environment
            num_episodes: Number of training episodes
            verbose: Whether to print progress
        """
        print(f"Training for {num_episodes} episodes...")
        print("-" * 60)
        
        for episode in range(num_episodes):
            # Reset environment
            state = env.reset()
            total_reward = 0
            steps = 0
            done = False
            
            # Run episode
            while not done:
                # Choose action using ε-greedy policy
                action = self.choose_action(state)
                
                # Take action, observe result
                next_state, reward, done = env.step(action)
                total_reward += reward
                steps += 1
                
                # Learn from this experience (Q-value update)
                self.learn(state, action, reward, next_state, done)
                
                state = next_state
                
                # Prevent infinite loops
                if steps > 100:
                    break
            
            # Record episode statistics
            self.episode_rewards.append(total_reward)
            
            # Print progress
            if verbose and (episode + 1) % 100 == 0:
                avg_reward = np.mean(self.episode_rewards[-100:])
                print(f"Episode {episode + 1:4d} | "
                      f"Avg Reward (last 100): {avg_reward:6.2f} | "
                      f"Steps: {steps:3d}")
        
        print("-" * 60)
        print("Training complete!")
        print()
    
    def display_q_table(self, env: GridWorldEnv):
        """
        Display learned Q-values for each state.
        
        Args:
            env: GridWorld environment
        """
        print("Learned Q-Values:")
        print("=" * 60)
        
        for y in range(env.height - 1, -1, -1):
            for x in range(env.width):
                state = (x, y)
                
                # Skip special states
                if state == env.goal:
                    print(f"  GOAL ({x},{y})", end="")
                    continue
                elif state in env.pits:
                    print(f"   PIT ({x},{y})", end="")
                    continue
                
                # Find best action and its Q-value
                best_action = self.get_best_action(state)
                best_q = self.get_q_value(state, best_action)
                
                print(f" ({x},{y}):{best_action[0].upper()} {best_q:5.1f}", end="")
            print()
        print("=" * 60)
        print()


def plot_training_curve(rewards: List[float], window: int = 100):
    """
    Display a simple ASCII plot of training progress.
    
    Args:
        rewards: List of episode rewards
        window: Moving average window size
    """
    print("\nTraining Progress (Moving Average):")
    print("-" * 60)
    
    # Calculate moving average
    if len(rewards) < window:
        return
    
    moving_avg = []
    for i in range(window, len(rewards) + 1, window):
        avg = np.mean(rewards[i-window:i])
        moving_avg.append(avg)
    
    # Simple ASCII plot
    min_val = min(moving_avg)
    max_val = max(moving_avg)
    range_val = max_val - min_val if max_val != min_val else 1
    
    height = 10
    for i in range(height):
        threshold = max_val - (i * range_val / height)
        line = ""
        for avg in moving_avg:
            line += "█" if avg >= threshold else " "
        print(f"{threshold:6.1f} |{line}|")
    
    print(f"{'':6s} |{'_' * len(moving_avg)}|")
    print(f"{'':7s} 0{' ' * (len(moving_avg) - 4)}{len(rewards)}")
    print(f"{'':7s} Episodes")
    print()


def demonstrate_learned_policy(agent: QLearningAgent, env: GridWorldEnv):
    """
    Demonstrate the learned policy by running one episode.
    
    Args:
        agent: Trained Q-learning agent
        env: GridWorld environment
    """
    print("=" * 60)
    print("DEMONSTRATING LEARNED POLICY")
    print("=" * 60)
    
    # Temporarily set epsilon to 0 (no exploration, pure exploitation)
    old_epsilon = agent.epsilon
    agent.epsilon = 0.0
    
    state = env.reset()
    done = False
    steps = 0
    total_reward = 0
    
    print("\nAgent following learned policy:")
    env.display(q_agent=agent)
    
    while not done and steps < 50:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        total_reward += reward
        steps += 1
        
        print(f"Step {steps}: {state} --{action}--> {next_state} | Reward: {reward:+.0f}")
        env.display(q_agent=agent)
        
        state = next_state
        time.sleep(0.5)
    
    # Restore epsilon
    agent.epsilon = old_epsilon
    
    print("-" * 60)
    if state == env.goal:
        print(f"✅ SUCCESS! Reached goal in {steps} steps")
        print(f"   Total reward: {total_reward:.1f}")
    else:
        print(f"❌ Did not reach goal within {steps} steps")
    print("=" * 60)
    print()


def main():
    """
    Main demonstration of Q-learning agent.
    """
    print("=" * 60)
    print("LEARNING AGENT: Q-LEARNING IN GRIDWORLD")
    print("=" * 60)
    print()
    
    # Create environment
    env = GridWorldEnv(width=5, height=5)
    
    print("Environment created:")
    print(f"  Size: {env.width}x{env.height}")
    print(f"  Start: {env.start}")
    print(f"  Goal: {env.goal}")
    print(f"  Pits: {env.pits}")
    print()
    
    # Show initial grid
    env.display()
    
    # Create and train agent
    agent = QLearningAgent(
        actions=env.actions,
        learning_rate=0.1,
        discount_factor=0.9,
        epsilon=0.1
    )
    
    # Train the agent
    agent.train(env, num_episodes=1000, verbose=True)
    
    # Display results
    agent.display_q_table(env)
    plot_training_curve(agent.episode_rewards)
    
    # Demonstrate learned policy
    demonstrate_learned_policy(agent, env)
    
    # Key takeaways
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("✅ Agent learned optimal policy through trial and error")
    print("✅ Q-learning converges to optimal Q-values")
    print("✅ ε-greedy balances exploration and exploitation")
    print("✅ Temporal Difference learning enables online learning")
    print("✅ No prior knowledge needed - agent discovers strategy")
    print("=" * 60)


if __name__ == "__main__":
    main()
