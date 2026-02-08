# Agent Types and Architectures

## Overview

Different problems require different agent designs. This guide explores the main types of agents, from simple reactive systems to complex multi-agent architectures.

## The Agent Classification Hierarchy

```
Intelligent Agents
│
├── Simple Reflex Agents (Reactive)
├── Model-Based Reflex Agents  
├── Goal-Based Agents (Deliberative)
├── Utility-Based Agents
├── Learning Agents
└── Multi-Agent Systems
```

## 1. Reactive Agents (Simple Reflex Agents)

### Definition
Reactive agents respond directly to current percepts using condition-action rules, without considering history or future consequences.

### Structure
```
Percepts → Condition-Action Rules → Actions
```

### Characteristics
- ✅ **Fast:** Immediate responses with minimal computation
- ✅ **Simple:** Easy to implement and understand
- ❌ **Limited:** Cannot handle partially observable environments
- ❌ **No planning:** Cannot consider future consequences

### How They Work

**Algorithm:**
```python
function SIMPLE_REFLEX_AGENT(percept):
    state = INTERPRET_INPUT(percept)
    rule = RULE_MATCH(state, rules)
    action = rule.ACTION
    return action
```

### Real-World Examples

#### 1. Thermostat
```python
if temperature < 68°F:
    turn_on_heater()
elif temperature > 72°F:
    turn_on_cooling()
else:
    maintain_off()
```

#### 2. Automatic Door
```python
if motion_detected():
    open_door()
    wait(5_seconds)
    close_door()
```

#### 3. Spam Filter (Simple)
```python
if email_contains(spam_keywords):
    mark_as_spam()
else:
    deliver_to_inbox()
```

#### 4. Anti-lock Braking System (ABS)
```python
if wheel_locked():
    release_brake()
else:
    apply_brake()
```

### When to Use
- Environment is fully observable
- Correct action depends only on current percept
- Speed is critical
- Problems are simple and well-defined

### Limitations
- Cannot handle partially observable environments
- No memory of past states
- Cannot plan ahead
- Stuck in infinite loops if rules conflict

---

## 2. Model-Based Reflex Agents

### Definition
These agents maintain an **internal state** (model) of the world that tracks aspects not visible in current percepts.

### Structure
```
Percepts → Update Internal State → Condition-Action Rules → Actions
         ↑                        ↑
         └─── Internal Model ─────┘
```

### Characteristics
- ✅ **Handles partial observability**
- ✅ **Maintains history**
- ✅ **More robust than simple reflex**
- ❌ **Still no long-term planning**

### How They Work

**Algorithm:**
```python
function MODEL_BASED_REFLEX_AGENT(percept):
    state = UPDATE_STATE(state, action, percept, model)
    rule = RULE_MATCH(state, rules)
    action = rule.ACTION
    return action
```

### Real-World Examples

#### 1. Robot Vacuum (Roomba)
- **Internal model:** Map of cleaned vs. uncleaned areas
- **Behavior:** Tracks where it's been to ensure complete coverage
- **Adaptation:** Updates map when encountering obstacles

#### 2. Self-Checkout Scanner
- **Internal model:** List of scanned items
- **Behavior:** Tracks total price, flags suspicious activity
- **Adaptation:** Remembers what's been scanned vs. bagged

#### 3. Email Client with Filters
- **Internal model:** User's reading patterns, folder structure
- **Behavior:** Sorts emails based on learned preferences
- **Adaptation:** Updates model when user moves emails

### When to Use
- Partial observability
- Actions depend on recent history
- Need to track state over time
- Environment changes gradually

---

## 3. Deliberative Agents (Goal-Based Agents)

### Definition
Deliberative agents explicitly represent goals and use **planning** and **search** to find action sequences that achieve those goals.

### Structure
```
Percepts → State → Goals → Planning/Search → Action Sequence
                     ↓
                  World Model
```

### Characteristics
- ✅ **Considers future consequences**
- ✅ **Flexible:** Can handle multiple goals
- ✅ **Optimal solutions** (with good search)
- ❌ **Computationally expensive**
- ❌ **Slower than reactive agents**

### How They Work

**Algorithm:**
```python
function GOAL_BASED_AGENT(percept):
    state = UPDATE_STATE(state, percept)
    if not GOAL_ACHIEVED(state, goals):
        plan = SEARCH(state, goals, world_model)
        action = plan[0]  # Execute first step
    else:
        action = NO_OP
    return action
```

### Key Techniques

#### Search Algorithms
- **Uninformed:** BFS, DFS, Uniform-Cost Search
- **Informed:** A*, Greedy Best-First Search
- **Adversarial:** Minimax, Alpha-Beta Pruning

#### Planning
- **Classical:** STRIPS, PDDL
- **Hierarchical:** HTN planning
- **Probabilistic:** MDPs, POMDPs

### Real-World Examples

#### 1. GPS Navigation (Google Maps)
- **Goal:** Reach destination
- **Planning:** A* or Dijkstra's algorithm to find shortest path
- **Adaptation:** Re-plans when encountering traffic or road closures
- **Reasoning:** Considers distance, time, traffic patterns

#### 2. Chess AI (Stockfish)
- **Goal:** Checkmate opponent's king
- **Planning:** Minimax with alpha-beta pruning
- **Depth:** Looks 20+ moves ahead
- **Evaluation:** Uses heuristics to evaluate positions

#### 3. Automated Meeting Scheduler
- **Goal:** Schedule meeting that works for all attendees
- **Planning:** Constraint satisfaction to find valid time slots
- **Reasoning:** Considers preferences, conflicts, priorities

#### 4. Mission Planning for Mars Rovers
- **Goal:** Complete scientific objectives within power/time budget
- **Planning:** Task scheduling with resource constraints
- **Reasoning:** Long-term planning due to communication delays

### When to Use
- Clear, explicit goals
- Need to plan multi-step sequences
- Can afford computation time for planning
- World can be modeled accurately

### Advantages Over Reactive
- Can achieve complex goals requiring multiple steps
- Finds optimal or near-optimal solutions
- Handles goal changes gracefully

---

## 4. Utility-Based Agents

### Definition
Utility-based agents use a **utility function** to rank different world states and choose actions that maximize expected utility.

### Structure
```
Percepts → State → Utility Function → Expected Utility of Actions → Best Action
                          ↓
                    Preferences/Values
```

### Characteristics
- ✅ **Handles conflicting goals**
- ✅ **Optimal decision-making**
- ✅ **Quantifies trade-offs**
- ❌ **Requires precise utility function**
- ❌ **Computationally intensive**

### How They Work

**Algorithm:**
```python
function UTILITY_BASED_AGENT(percept):
    state = UPDATE_STATE(state, percept)
    actions = GET_POSSIBLE_ACTIONS(state)
    
    best_action = None
    best_utility = -infinity
    
    for action in actions:
        expected_utility = COMPUTE_EXPECTED_UTILITY(action, state)
        if expected_utility > best_utility:
            best_utility = expected_utility
            best_action = action
    
    return best_action
```

### Real-World Examples

#### 1. Stock Trading Algorithms
- **Utility:** Maximize profit while minimizing risk
- **Trade-offs:** Risk vs. reward, short-term vs. long-term gains
- **Decision:** Which stocks to buy/sell and when

#### 2. Medical Diagnosis Systems
- **Utility:** Patient health outcomes, treatment costs, side effects
- **Trade-offs:** Aggressive treatment vs. quality of life
- **Decision:** Optimal treatment plan

#### 3. Recommendation Systems (Netflix, Spotify)
- **Utility:** User satisfaction, engagement, diversity
- **Trade-offs:** Popular vs. niche content, exploitation vs. exploration
- **Decision:** What to recommend next

### When to Use
- Multiple competing objectives
- Need to quantify trade-offs
- Preferences can be encoded numerically
- Optimal decision-making is critical

---

## 5. Learning Agents

### Definition
Learning agents improve their performance over time through experience, adapting to their environment without explicit reprogramming.

### Structure
```
┌────────────────────────────────────────┐
│           Learning Element             │
│  (Updates knowledge from experience)   │
└────────────┬───────────────────────────┘
             ↓
┌────────────────────────────────────────┐
│         Performance Element            │
│    (Selects actions based on           │
│     current knowledge)                 │
└────────────┬───────────────────────────┘
             ↓
        Environment
             ↓
┌────────────────────────────────────────┐
│            Critic                      │
│   (Provides feedback on performance)   │
└────────────────────────────────────────┘
```

### Characteristics
- ✅ **Adapts to new situations**
- ✅ **Improves over time**
- ✅ **Handles unknown environments**
- ❌ **Requires training data/experience**
- ❌ **May learn incorrect behaviors**

### Learning Paradigms

#### 1. Supervised Learning
- Learn from labeled examples
- Example: Spam filter learning from user-labeled emails

#### 2. Unsupervised Learning
- Discover patterns without labels
- Example: Clustering customer segments

#### 3. Reinforcement Learning (RL)
- Learn from rewards and punishments
- Example: Game-playing agents, robotics

### Reinforcement Learning in Detail

**Key Concepts:**
- **State (S):** Current situation
- **Action (A):** What the agent can do
- **Reward (R):** Immediate feedback
- **Policy (π):** Strategy mapping states to actions
- **Value Function (V):** Long-term expected reward

**Common RL Algorithms:**
- Q-Learning
- SARSA  
- Deep Q-Networks (DQN)
- Policy Gradients
- Actor-Critic methods
- Proximal Policy Optimization (PPO)

### Real-World Examples

#### 1. AlphaGo / AlphaZero
- **Learning method:** Self-play reinforcement learning
- **Performance:** Superhuman level in Go, Chess, Shogi
- **Improvement:** Millions of games played against itself

#### 2. Autonomous Drone Racing
- **Learning method:** RL in simulation, transfer to real world
- **Performance:** Learns optimal flight paths
- **Improvement:** Gets faster with more practice

#### 3. Personalized News Feed (Facebook, Twitter)
- **Learning method:** Online learning from user engagement
- **Performance:** Maximizes time spent and engagement
- **Improvement:** Adapts to changing user interests

#### 4. Robotic Grasping
- **Learning method:** Trial and error with reward shaping
- **Performance:** Learns to pick up diverse objects
- **Improvement:** Generalizes to new object shapes

### When to Use
- Environment is initially unknown
- Optimal behavior is hard to specify
- Need adaptation to changing conditions
- Have access to feedback/rewards

---

## 6. Multi-Agent Systems (MAS)

### Definition
Multi-Agent Systems consist of multiple autonomous agents interacting in a shared environment, which can cooperate, compete, or negotiate.

### Types of Interactions

#### 1. Cooperative
Agents work together toward common goals
- Example: Robot teams, distributed problem-solving

#### 2. Competitive  
Agents pursue conflicting goals
- Example: Poker bots, competitive trading

#### 3. Mixed (Coopetition)
Agents both cooperate and compete
- Example: Supply chain networks, auction markets

### Characteristics
- ✅ **Scalable:** Distribute computation
- ✅ **Robust:** Fault tolerance through redundancy
- ✅ **Emergent behavior:** Complex outcomes from simple rules
- ❌ **Coordination challenges**
- ❌ **Communication overhead**

### Key Concepts

#### Communication
- **Speech acts:** Request, inform, propose, agree
- **Protocols:** Contract Net, auctions, voting
- **Languages:** KQML, FIPA-ACL

#### Coordination
- **Centralized:** Leader coordinates all agents
- **Decentralized:** Agents coordinate peer-to-peer
- **Emergent:** Coordination from local interactions

#### Game Theory
- **Nash Equilibrium:** Stable strategy profiles
- **Pareto Optimality:** Efficient allocations
- **Mechanism Design:** Design rules for desired outcomes

### Real-World Examples

#### 1. Traffic Signal Control
- **Agents:** Each intersection has an agent
- **Goal:** Minimize overall traffic congestion
- **Coordination:** Agents share traffic flow information
- **Emergent behavior:** Green waves on arterial roads

#### 2. Ant Colony Optimization
- **Agents:** Virtual ants exploring solution space
- **Goal:** Find shortest path (e.g., traveling salesman)
- **Coordination:** Pheromone trails (stigmergy)
- **Emergent behavior:** Optimal routes discovered

#### 3. Multiplayer Game NPCs
- **Agents:** Different NPC types (soldiers, medics, commanders)
- **Goal:** Defeat player team
- **Coordination:** Squad tactics, flanking maneuvers
- **Emergent behavior:** Realistic team combat

#### 4. Blockchain Consensus (Proof of Stake)
- **Agents:** Validator nodes
- **Goal:** Agree on transaction history
- **Coordination:** Consensus protocols
- **Emergent behavior:** Decentralized trust

#### 5. Smart Grid Energy Management
- **Agents:** Homes, businesses, power plants, storage
- **Goal:** Balance supply and demand efficiently
- **Coordination:** Price signals, negotiations
- **Emergent behavior:** Stable grid with renewables

### When to Use
- Problem naturally decomposes into subproblems
- Need scalability and fault tolerance
- Multiple stakeholders with different goals
- Centralized control is infeasible

---

## Comparison Table

| Type | Complexity | Speed | Optimality | Adaptability | Use Case |
|------|-----------|-------|-----------|--------------|----------|
| **Reactive** | Low | Very Fast | Low | None | Thermostats, simple control |
| **Model-Based** | Medium | Fast | Medium | Low | Robot navigation, tracking |
| **Deliberative** | High | Slow | High | Medium | GPS, chess AI, planning |
| **Utility-Based** | High | Slow | Optimal | Medium | Trading, recommendations |
| **Learning** | Very High | Varies | Improves | Very High | Game AI, robotics, personalization |
| **Multi-Agent** | Very High | Varies | Varies | High | Swarms, markets, distributed systems |

## Choosing the Right Agent Type

### Decision Tree

```
Does the problem require learning/adaptation?
├─ YES → Learning Agent or Multi-Agent with Learning
└─ NO → Continue...
    │
    Are multiple autonomous entities involved?
    ├─ YES → Multi-Agent System
    └─ NO → Continue...
        │
        Are there conflicting goals/trade-offs?
        ├─ YES → Utility-Based Agent
        └─ NO → Continue...
            │
            Does it require planning ahead?
            ├─ YES → Deliberative/Goal-Based Agent
            └─ NO → Continue...
                │
                Is the environment partially observable?
                ├─ YES → Model-Based Reflex Agent
                └─ NO → Simple Reflex Agent
```

## Hybrid Architectures

Real-world systems often combine multiple agent types:

### 1. Subsumption Architecture
- Layer reactive behaviors
- Higher-level behaviors can override lower ones
- Example: Robot control (avoid obstacles → explore → go to goal)

### 2. Three-Layer Architecture
- **Reactive layer:** Fast responses to immediate threats
- **Deliberative layer:** Planning and reasoning
- **Executive layer:** Coordinates between layers

### 3. BDI (Belief-Desire-Intention)
- **Beliefs:** Model of the world
- **Desires:** Goals to achieve
- **Intentions:** Currently pursued plans
- Example: Intelligent personal assistants

## What's Next?

Now that you understand different agent types, continue to [Key Components](03-key-components.md) to learn about the building blocks that make agents work: perception, reasoning, planning, action, learning, and memory.

---

**Key Takeaways:**
- ✅ **Reactive agents** are fast but limited to current percepts
- ✅ **Model-based agents** maintain internal state for partial observability
- ✅ **Deliberative agents** plan ahead to achieve explicit goals
- ✅ **Utility-based agents** optimize trade-offs between competing objectives
- ✅ **Learning agents** improve performance through experience
- ✅ **Multi-agent systems** involve multiple interacting autonomous agents
- ✅ Choose agent type based on problem requirements and constraints
