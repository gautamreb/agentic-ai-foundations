# Week 3 Exercise: Training a Navigation Agent

## Learning Objectives

- ✅ Implement Q-learning from scratch
- ✅ Design reward functions
- ✅ Tune hyperparameters (α, γ, ε)
- ✅ Analyze learning curves
- ✅ Compare with deliberative planning

## Background

Review [Example 03: Learning Agent](../../examples/03-learning-agent/) and reinforcement learning basics.

## Problem Statement

Train a **navigation agent** to find treasures while avoiding traps in a custom GridWorld.

### Environment

- 8x8 grid
- Start position: (0, 0)
- Treasures: +100 reward at 3 locations
- Traps: -50 reward at 5 locations
- Empty cells: -1 reward (encourages efficiency)
- Episode ends when treasure found or max steps reached

### Requirements

**Part 1: Q-Learning Implementation (40 points)**
- Implement Q-learning update rule
- ε-greedy exploration strategy
- Train for 1000 episodes

**Part 2: Hyperparameter Tuning (30 points)**
- Test different learning rates (α): 0.01, 0.1, 0.5
- Test different discount factors (γ): 0.8, 0.9, 0.99
- Plot learning curves for each
- Identify best combination

**Part 3: Analysis (30 points)**
- Compare final performance with random agent
- Compare with A* pathfinding agent
- Discuss when RL is better than planning

## Starter Code

```python
class QLearningNavigator:
    def __init__(self, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = defaultdict(float)
        # ... 
    
    def learn(self, state, action, reward, next_state, done):
        # Q-learning update
        pass
    
    def train(self, env, episodes=1000):
        # Training loop
        pass
```

## Expected Results

- Initial: Random performance (~-500 avg reward)
- After 100 episodes: Finding treasures occasionally (~0 avg reward)
- After 500 episodes: Consistent good paths (~+80 avg reward)
- After 1000 episodes: Near-optimal (~+95 avg reward)

**Solution:** See [solution3.py](solution3.py)
