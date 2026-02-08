# Learning Agent: Q-Learning in GridWorld

## Overview

This example demonstrates a **learning agent** that improves its performance through experience using **Q-learning**, a fundamental reinforcement learning algorithm.

## What is a Learning Agent?

A learning agent:
- **Starts with no knowledge** of the environment
- **Learns through trial and error** (exploration)
- **Improves over time** based on rewards and punishments
- **Discovers optimal behavior** without being explicitly programmed
- **Adapts to changing environments**

### Structure

```
Environment
     ↓ State, Reward
Learning Agent
     ↓ Action
Environment
     ↓
Update Q-Values (Learning)
     ↓
Improved Policy
```

## Q-Learning Algorithm

Q-learning learns a **Q-function** Q(s, a) that estimates the expected cumulative reward of taking action `a` in state `s`.

### Key Equation

```
Q(s, a) ← Q(s, a) + α[r + γ max_a' Q(s', a') - Q(s, a)]
```

Where:
- **α (alpha)**: Learning rate (0 to 1) - how much to update
- **γ (gamma)**: Discount factor (0 to 1) - how much to value future rewards
- **r**: Immediate reward
- **s'**: Next state after taking action a
- **max_a' Q(s', a')**: Best possible future value

### Components

1. **States (S)**: All possible situations (grid positions)
2. **Actions (A)**: What agent can do (up, down, left, right)
3. **Rewards (R)**: Immediate feedback (+10 for goal, -1 per step, -10 for pits)
4. **Policy (π)**: Strategy for choosing actions
5. **Q-Table**: Stores Q(s, a) values for all state-action pairs

## The GridWorld Example

The agent navigates a grid to reach a goal while avoiding pits:

- **Start**: Random or fixed position
- **Goal**: +10 reward, episode ends
- **Pits**: -10 reward, episode ends
- **Empty cells**: -1 reward (encourages efficiency)
- **Actions**: Move up, down, left, right

### Learning Process

1. **Episode 1**: Agent stumbles randomly, learns nothing useful
2. **Episode 10**: Agent starts avoiding obvious pits
3. **Episode 100**: Agent finds goal occasionally
4. **Episode 1000**: Agent takes near-optimal path consistently

## Real-World Applications

Q-learning and RL are used in:
- **Game AI**: AlphaGo, DQN for Atari
- **Robotics**: Robot manipulation, locomotion
- **Trading**: Algorithmic trading strategies
- **Recommendation systems**: Netflix, YouTube
- **Resource management**: Data center cooling, traffic lights
- **Autonomous vehicles**: Decision-making in complex scenarios

## Running the Example

```bash
cd examples/03-learning-agent
python learning_agent.py
```

The simulation will:
1. Train the agent over many episodes
2. Show learning progress (rewards over time)
3. Display the learned Q-values
4. Demonstrate the learned optimal policy
5. Visualize the agent following the learned path

## Key Concepts Demonstrated

### 1. Exploration vs. Exploitation

**ε-greedy policy:**
- With probability ε: explore (random action)
- With probability 1-ε: exploit (best known action)

Early training: High ε (explore to learn)  
Late training: Low ε (exploit learned knowledge)

### 2. Temporal Difference Learning

Learn from difference between prediction and reality:
```
TD Error = r + γ max_a' Q(s', a') - Q(s, a)
```

### 3. Off-Policy Learning

Q-learning learns optimal policy while following exploratory policy.

### 4. Value Function Convergence

Q-values converge to true values with sufficient exploration.

### 5. Credit Assignment

Learning which actions led to rewards, even delayed ones.

## Comparison with Previous Examples

| Aspect | Reactive | Deliberative | Learning (Q-Learning) |
|--------|----------|--------------|----------------------|
| **Knowledge** | Rules (pre-programmed) | Map (given) | None → Learned |
| **Adaptation** | None | Re-plan | Improves with experience |
| **Optimality** | Not guaranteed | Optimal (with A*) | Converges to optimal |
| **Initial performance** | Good | Good | Poor (random) |
| **Final performance** | Same | Same | Optimal |
| **Training needed** | No | No | Yes |
| **Unknown environments** | Fails | Needs map | Learns through exploration |

## Hyperparameters Explained

### Learning Rate (α)

Controls how much new information overrides old:
- **α = 0**: Never learn anything new
- **α = 1**: Completely forget old estimates
- **Typical**: 0.1 - 0.3
- **Effect**: Higher α = faster learning but more unstable

### Discount Factor (γ)

How much to value future rewards:
- **γ = 0**: Only care about immediate reward (myopic)
- **γ = 1**: All future rewards valued equally
- **Typical**: 0.9 - 0.99
- **Effect**: Higher γ = longer-term planning

### Exploration Rate (ε)

Probability of taking random action:
- **ε = 0**: Always exploit (greedy)
- **ε = 1**: Always explore (random)
- **Typical**: Start high (0.1-1.0), decay to low (0.01-0.1)
- **Effect**: Balances exploration of new strategies vs. using known good ones

## Training Curve Analysis

A typical learning curve shows:

```
Reward
  ↑
  |     ┌────────────── Convergence (optimal)
  |    ╱
  |   ╱
  |  ╱
  | ╱  
  |╱________________
  └──────────────────→ Episodes
  Random   Learning    Optimal
```

**Phases:**
1. **Random (episodes 1-100)**: Exploring randomly, low average reward
2. **Learning (episodes 100-500)**: Finding patterns, reward increasing
3. **Convergence (episodes 500+)**: Near-optimal behavior, stable reward

## Limitations of Q-Learning

1. **Discrete states/actions**: Doesn't scale to continuous spaces
2. **Table storage**: Large state spaces require huge Q-tables
3. **Sample inefficiency**: Needs many episodes to learn
4. **No generalization**: Learns each state independently

**Solutions:**
- **Deep Q-Networks (DQN)**: Neural network approximates Q-function
- **Function approximation**: Linear models, tile coding
- **Policy gradient methods**: Directly learn policy
- **Model-based RL**: Learn environment model

## Exercises

Try modifying the code to:

1. **Larger grid**: See how performance scales with state space

2. **Different reward structures**:
   - Sparse rewards (only at goal)
   - Shaped rewards (distance-based)
   - Penalty for collisions

3. **Multi-goal**: Multiple goals with different rewards

4. **Moving obstacles**: Dynamic environment requiring adaptation

5. **Stochastic actions**: Actions succeed only 80% of the time (wind effect)

6. **Compare algorithms**:
   - SARSA (on-policy alternative to Q-learning)
   - Monte Carlo methods

## Visualizing Learning

The example includes visualizations:

1. **Q-table heatmap**: Shows learned values for each state-action
2. **Policy arrows**: Shows preferred action in each state
3. **Episode rewards**: Learning curve over training
4. **Success rate**: Percentage of successful episodes

## From Q-Learning to Deep RL

Q-learning is the foundation for:

1. **DQN** (Deep Q-Network): CNN + Q-learning for Atari games
2. **Double DQN**: Reduces overestimation bias
3. **Dueling DQN**: Separate value and advantage streams
4. **Rainbow**: Combines multiple DQN improvements
5. **DQN variants**: Used in AlphaGo, AlphaZero (with tree search)

## Further Reading

### Books
- Sutton & Barto, "Reinforcement Learning: An Introduction" - Chapters 6-7
- Russell & Norvig, "AI: A Modern Approach" - Chapter 22

### Papers
- Watkins, "Learning from Delayed Rewards" (1989) - Original Q-learning thesis
- Mnih et al., "Playing Atari with Deep Reinforcement Learning" (2013) - DQN breakthrough

### Courses
- David Silver's RL Course (DeepMind)
- Berkeley CS285 (Deep RL)

---

**Next:** Continue to [Example 04: Multi-Agent System](../04-multi-agent-system/) to see how multiple agents can interact, cooperate, and compete.
