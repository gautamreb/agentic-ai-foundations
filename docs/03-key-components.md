# Key Components of Intelligent Agents

## Overview

Regardless of their type, all intelligent agents share core components that enable them to function effectively. This guide explores the six fundamental building blocks: **Perception**, **Reasoning**, **Planning**, **Action**, **Learning**, and **Memory**.

```
┌──────────────────────────────────────────────────┐
│                 Intelligent Agent                │
│                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │Perception│ ──►│ Reasoning│ ──►│ Planning │  │
│  └──────────┘    └──────────┘    └──────────┘  │
│                         │                        │
│  ┌──────────┐    ┌──────▼───┐    ┌──────────┐  │
│  │  Memory  │◄───┤ Learning │◄───┤  Action  │  │
│  └──────────┘    └──────────┘    └──────────┘  │
│                                                  │
└──────────────────────────────────────────────────┘
           ▲                          │
           │        Environment       │
           └──────────────────────────┘
```

---

## 1. Perception

### What is Perception?

**Perception** is the process by which an agent senses its environment and converts raw sensory data into meaningful internal representations.

### Key Aspects

#### Sensors
Different agents use different sensors:
- **Physical robots:** Cameras, LiDAR, ultrasonic, touch, microphones
- **Software agents:** API responses, database queries, log files
- **Game agents:** Game state, score, positions
- **LLM agents:** Text input, web search results, tool outputs

#### Preprocessing
Raw sensor data often needs processing:
- **Filtering:** Remove noise
- **Normalization:** Scale values to standard ranges
- **Feature extraction:** Identify relevant patterns
- **Sensor fusion:** Combine multiple sensor types

#### State Representation
How the agent internally represents what it perceives:
- **Discrete states:** Finite set of possibilities (e.g., chess positions)
- **Continuous states:** Real-valued vectors (e.g., robot position [x, y, θ])
- **Symbolic:** Logic-based representations (e.g., "Block A is on Block B")
- **Neural:** Embedding vectors (e.g., image features from CNN)

### Examples

#### Self-Driving Car
```python
# Perception pipeline
raw_camera_image → Object Detection → [car, pedestrian, traffic_light]
raw_lidar_points → Point Cloud Processing → [obstacle_map, drivable_area]
raw_gps_signal → Localization → [latitude, longitude, heading]
                                  ↓
                          Combined World Model
```

#### Chess AI
```python
# Board state perception
board_position = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    # ... rest of board
]
features = extract_features(board_position)
# → piece positions, control, king safety, material balance
```

#### Chatbot
```python
# Natural language perception
user_input = "What's the weather like today?"
                ↓
    Natural Language Understanding
                ↓
intent = "weather_query"
entities = {"time": "today", "location": "implicit"}
```

### Challenges

- **Partial Observability:** Can't see everything (fog of war in games)
- **Noisy Sensors:** Measurements contain errors
- **Uncertainty:** Ambiguous or conflicting information
- **High Dimensionality:** Too much data (e.g., high-resolution images)
- **Real-time Constraints:** Must process quickly

### Best Practices

1. **Use appropriate sensors** for your environment
2. **Filter noise** before processing
3. **Extract relevant features** instead of using raw data
4. **Handle missing data** gracefully
5. **Calibrate sensors** regularly

---

## 2. Reasoning

### What is Reasoning?

**Reasoning** is the process of drawing inferences from perceived information to understand the current situation and predict outcomes.

### Types of Reasoning

#### 1. Deductive Reasoning
Drawing specific conclusions from general rules:
```
Rule: "If it's raining, then the ground is wet"
Observation: "It is raining"
Conclusion: "The ground is wet"
```

**Applications:**
- Expert systems
- Theorem proving
- Game rule enforcement

#### 2. Inductive Reasoning
Generalizing from specific observations:
```
Observation: "Swan 1 is white"
Observation: "Swan 2 is white"  
Observation: "Swan 3 is white"
Generalization: "All swans are white" (though this can be wrong!)
```

**Applications:**
- Machine learning
- Pattern recognition
- Hypothesis formation

#### 3. Abductive Reasoning
Finding the best explanation for observations:
```
Observation: "The ground is wet"
Possible explanations: "It rained" OR "Sprinkler was on"
Best explanation: "It rained" (if sky is cloudy)
```

**Applications:**
- Diagnosis
- Root cause analysis
- Interpretability

#### 4. Probabilistic Reasoning
Reasoning under uncertainty:
```
P(Disease | Symptoms) = P(Symptoms | Disease) × P(Disease) / P(Symptoms)
```

**Applications:**
- Bayesian inference
- Risk assessment
- Decision making under uncertainty

### Reasoning Techniques

#### Logic-Based
- **Propositional logic:** Boolean combinations
- **First-order logic:** Quantifiers and predicates
- **Description logic:** Ontologies and knowledge graphs

#### Probabilistic
- **Bayesian networks:** Graphical models of dependencies
- **Markov models:** State transition probabilities
- **Monte Carlo methods:** Sampling-based inference

#### Neural
- **Deep learning:** Pattern recognition in high-dimensional data
- **Attention mechanisms:** Focus on relevant information
- **Transformers:** Context-aware reasoning (LLMs)

### Examples

#### Medical Diagnosis Agent
```python
# Bayesian reasoning
symptoms = ["fever", "cough", "fatigue"]
prior_probabilities = {
    "flu": 0.05,
    "covid": 0.02,
    "cold": 0.15
}

# Compute posterior probabilities given symptoms
posterior = bayesian_update(symptoms, prior_probabilities)
# → {"covid": 0.65, "flu": 0.25, "cold": 0.10}

diagnosis = max(posterior, key=posterior.get)  # → "covid"
```

#### Game AI
```python
# Minimax reasoning for chess
def evaluate_position(board):
    if is_checkmate(board):
        return INFINITY if our_turn() else -INFINITY
    
    score = 0
    score += material_balance(board)
    score += positional_advantage(board)
    score += king_safety(board)
    
    return score
```

#### Autonomous Vehicle
```python
# Probabilistic reasoning about pedestrian intent
def predict_pedestrian_action(pedestrian_state):
    # State: position, velocity, gaze direction
    
    if pedestrian_looking_at_road and near_crosswalk:
        p_cross = 0.8
    elif pedestrian_walking_parallel:
        p_cross = 0.1
    else:
        p_cross = 0.3
    
    return {"cross": p_cross, "not_cross": 1 - p_cross}
```

### Challenges

- **Computational complexity:** Some reasoning is NP-hard
- **Incomplete information:** Missing facts
- **Inconsistent information:** Contradictory data
- **Real-time constraints:** Must reason quickly
- **Common sense:** Hard to encode obvious knowledge

---

## 3. Planning

### What is Planning?

**Planning** is the process of determining a sequence of actions to achieve a goal, considering constraints and optimizing for objectives.

### Planning Paradigms

#### 1. Classical Planning
Assumes:
- Deterministic environment
- Full observability
- Known action effects

**Representation:**
- **States:** Complete world descriptions
- **Actions:** Preconditions and effects
- **Goal:** Desired state properties

**Example (STRIPS notation):**
```
Action: PickUp(block)
  Preconditions: On(block, table), HandEmpty
  Effects: Holding(block), ¬On(block, table), ¬HandEmpty
```

#### 2. Probabilistic Planning
Handles uncertainty in action outcomes:
- **MDPs (Markov Decision Processes):** Stochastic transitions
- **POMDPs:** Partial observability + stochasticity
- **Output:** Policy (state → action mapping)

#### 3. Hierarchical Planning
Breaks complex tasks into subtasks:
- **HTN (Hierarchical Task Network):** Decompose high-level tasks
- **Abstraction:** Plan at multiple levels of detail
- **Efficiency:** Reduces search space

#### 4. Temporal Planning
Considers time and concurrent actions:
- **Scheduling:** Allocate resources over time
- **Deadlines:** Time-bounded objectives
- **Durative actions:** Actions with duration

### Planning Algorithms

#### Search-Based

**Uninformed Search:**
- **Breadth-First Search (BFS):** Complete, optimal for uniform cost
- **Depth-First Search (DFS):** Memory efficient, not optimal
- **Uniform-Cost Search:** Optimal for varying action costs

**Informed Search (Heuristic):**
- **A\*:** Optimal with admissible heuristic
- **Greedy Best-First:** Fast but not optimal
- **IDA\*:** Memory-efficient A*

**Example A\* for pathfinding:**
```python
def a_star(start, goal, grid):
    # f(n) = g(n) + h(n)
    # g(n): cost from start to n
    # h(n): heuristic (estimated cost from n to goal)
    
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    
    while not open_set.empty():
        current = open_set.get()[1]
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + distance(current, neighbor)
            
            if tentative_g < g_score.get(neighbor, INFINITY):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                open_set.put((f_score, neighbor))
    
    return None  # No path found
```

#### Optimization-Based
- **Linear Programming:** Continuous action spaces
- **Integer Programming:** Discrete decisions
- **Constraint Satisfaction:** Satisfy all constraints

#### Sampling-Based
- **RRT (Rapidly-exploring Random Tree):** Robot motion planning
- **PRM (Probabilistic Roadmap):** Multi-query planning

### Examples

#### Robot Navigation
```python
# Task: Move from A to B avoiding obstacles
plan = a_star(
    start=current_position,
    goal=target_position,
    grid=occupancy_map,
    heuristic=euclidean_distance
)
# → [move_north, move_north, move_east, move_east, ...]
```

#### Task Scheduling
```python
# Task: Schedule meetings for multiple people
problem = SchedulingProblem(
    tasks=[meeting1, meeting2, meeting3],
    resources=[person_a, person_b, room_1],
    constraints=[no_conflicts, within_business_hours]
)
schedule = solve_csp(problem)
# → {meeting1: (Monday, 9am, room_1), ...}
```

#### Meal Planning
```python
# Task: Plan weekly meals optimizing nutrition and cost
planner = MealPlanner(
    days=7,
    constraints=[
        calorie_target(2000),
        protein_minimum(150),
        budget_maximum(50)
    ]
)
meal_plan = planner.optimize()
# → {Monday: [breakfast, lunch, dinner], ...}
```

### Challenges

- **Combinatorial explosion:** Too many possible plans
- **Uncertainty:** Actions may fail
- **Dynamic environments:** World changes during planning
- **Resource constraints:** Limited time, energy, budget
- **Multi-objective:** Conflicting goals

### Planning Best Practices

1. **Use domain knowledge** to guide search
2. **Plan at appropriate granularity** (not too detailed)
3. **Re-plan when needed** (don't stick to obsolete plans)
4. **Hierarchical decomposition** for complex tasks
5. **Consider uncertainty** in critical applications

---

## 4. Action

### What is Action?

**Action** is the means by which an agent affects its environment through actuators, executing plans and responding to percepts.

### Types of Actions

#### 1. Physical Actions
Manipulating the physical world:
- **Movement:** Walking, driving, flying
- **Manipulation:** Grasping, assembling, operating tools
- **Communication:** Speaking, displaying

#### 2. Digital Actions
Interacting with software systems:
- **API calls:** Sending requests, querying databases
- **File operations:** Reading, writing, modifying
- **UI interactions:** Clicking, typing, scrolling

#### 3. Communication Actions
Interacting with other agents or humans:
- **Inform:** Sharing information
- **Request:** Asking for actions
- **Negotiate:** Proposing deals
- **Coordinate:** Synchronizing activities

### Action Selection

How does an agent choose what to do?

#### 1. Rule-Based
```python
if battery_low:
    action = go_to_charging_station()
elif task_assigned:
    action = execute_task()
else:
    action = explore()
```

#### 2. Policy-Based (RL)
```python
# Learned policy π(s) → a
state = perceive_environment()
action = policy(state)
```

#### 3. Planning-Based
```python
# Execute next step of plan
if plan is None or plan_failed:
    plan = create_plan(current_state, goal)

action = plan.next_step()
```

#### 4. Utility Maximization
```python
# Choose action with highest expected utility
actions = get_possible_actions(state)
action = max(actions, key=lambda a: expected_utility(a, state))
```

### Action Execution

#### Challenges

1. **Execution Failures**
   - Hardware malfunction
   - Unexpected obstacles
   - Resource depletion

2. **Partial Execution**
   - Action interrupted
   - Incomplete effects

3. **Timing**
   - Actions may take time
   - Concurrent actions
   - Synchronization

#### Strategies

**Robust Execution:**
```python
def execute_with_retry(action, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            result = action.execute()
            if verify_success(result):
                return result
        except ActionFailure as e:
            log_error(e)
            if attempt < max_attempts - 1:
                recover_from_failure()
    
    return None  # Action failed
```

**Monitoring:**
```python
def execute_with_monitoring(action, expected_effects):
    action.execute()
    
    actual_effects = observe_environment()
    
    if actual_effects != expected_effects:
        # Re-plan or take corrective action
        handle_unexpected_outcome(actual_effects)
```

### Examples

#### Robotic Arm
```python
# Low-level motor control
def move_to_position(target_x, target_y, target_z):
    while not at_target():
        current_pos = get_current_position()
        error = target_pos - current_pos
        
        # PID controller
        velocity = kp * error + ki * integral(error) + kd * derivative(error)
        
        set_motor_velocities(velocity)
        sleep(dt)
```

#### Chatbot
```python
# Generate and send response
def respond_to_user(user_message):
    intent = classify_intent(user_message)
    
    if intent == "weather":
        weather_data = call_weather_api(extract_location(user_message))
        response = format_weather_response(weather_data)
    elif intent == "greeting":
        response = generate_greeting()
    
    send_message(response)
```

#### Trading Agent
```python
# Execute trade
def execute_trade(order):
    # Check pre-conditions
    if not validate_order(order):
        return False
    
    # Place order
    order_id = trading_api.place_order(
        symbol=order.symbol,
        quantity=order.quantity,
        price=order.price,
        order_type=order.type
    )
    
    # Monitor execution
    status = wait_for_fill(order_id, timeout=60)
    
    return status == "filled"
```

---

## 5. Learning

### What is Learning?

**Learning** is the process by which an agent improves its performance on future tasks based on experience.

### Why Learning Matters

- **Adaptation:** Handle new situations not anticipated by designers
- **Efficiency:** Discover better strategies over time
- **Scalability:** Reduce need for manual programming
- **Generalization:** Apply knowledge to new domains

### Learning Paradigms

#### 1. Supervised Learning
Learn from labeled examples:

**Input:** (x, y) pairs where y is the correct label  
**Goal:** Learn function f(x) ≈ y  
**Applications:** Classification, regression

**Example:**
```python
# Learn to classify emails as spam/not spam
training_data = [
    ("Buy now!", "spam"),
    ("Meeting at 3pm", "not_spam"),
    ("You won $1000", "spam"),
    # ... thousands more examples
]

model = train_classifier(training_data)
prediction = model.predict("Cheap viagra!")  # → "spam"
```

#### 2. Unsupervised Learning
Discover patterns without labels:

**Input:** Unlabeled data  
**Goal:** Find structure or patterns  
**Applications:** Clustering, dimensionality reduction, anomaly detection

**Example:**
```python
# Discover customer segments
customer_data = [[age, income, purchase_frequency], ...]
clusters = k_means(customer_data, k=3)
# → Group 1: Young, low income, frequent buyers
# → Group 2: Middle-aged, high income, occasional buyers
# → Group 3: Retired, medium income, rare buyers
```

#### 3. Reinforcement Learning (RL)
Learn from rewards and punishments:

**Input:** State-action-reward sequences  
**Goal:** Learn policy that maximizes cumulative reward  
**Applications:** Game playing, robotics, resource allocation

**Key Concepts:**
- **State (s):** Current situation
- **Action (a):** What agent does
- **Reward (r):** Immediate feedback
- **Policy (π):** Strategy (s → a)
- **Value (V):** Expected cumulative reward

**Example - Q-Learning:**
```python
# Learn to play a game
Q = {}  # Q-table: Q(state, action) → expected reward

for episode in range(num_episodes):
    state = env.reset()
    
    while not done:
        # Choose action (ε-greedy)
        if random() < epsilon:
            action = random_action()
        else:
            action = argmax_a(Q[state, a])
        
        # Take action, observe result
        next_state, reward, done = env.step(action)
        
        # Update Q-value
        Q[state, action] += alpha * (
            reward + gamma * max_a(Q[next_state, a]) - Q[state, action]
        )
        
        state = next_state
```

#### 4. Transfer Learning
Apply knowledge from one task to another:

**Example:**
```python
# Use pre-trained image model for medical diagnosis
base_model = load_pretrained("ImageNet_ResNet50")
# Fine-tune on medical images
medical_model = fine_tune(base_model, medical_images)
```

### Learning Techniques for Agents

#### Online Learning
Learn while operating:
- Update model with each new experience
- Adapt to changing environment
- Example: Recommendation systems

#### Offline Learning
Learn from collected dataset before deployment:
- Train on historical data
- More stable and predictable
- Example: Autonomous driving in simulation

#### Active Learning
Agent chooses what to learn from:
- Query for labels on uncertain examples
- Efficient use of human feedback
- Example: Labeling rare events

#### Meta-Learning
Learn how to learn:
- Adapt quickly to new tasks
- Few-shot learning
- Example: Adapting to new users

### Examples

#### Self-Driving Car
```python
# Learn from millions of miles of driving data
# Supervised: Object detection from labeled images
# RL: Optimize comfort and efficiency
# Imitation: Learn from human drivers

model = train_driving_policy(
    sensor_data=camera_images,
    actions=human_driver_actions,
    rewards=safety_scores
)
```

#### Game AI
```python
# Learn to play StarCraft
agent = RL_Agent()

for game in range(1_000_000):
    state = game.start()
    
    while not game.over():
        action = agent.select_action(state)
        next_state, reward = game.step(action)
        
        agent.learn(state, action, reward, next_state)
        state = next_state

# After training, agent reaches professional human level
```

### Challenges

- **Sample efficiency:** Needs lots of data
- **Exploration vs. exploitation:** Balance trying new things vs. using known good strategies
- **Credit assignment:** Which action caused the reward?
- **Stability:** Learning can be unstable
- **Generalization:** Overfitting to training data

---

## 6. Memory

### What is Memory?

**Memory** allows an agent to store and recall information over time, enabling learning, planning, and handling partial observability.

### Types of Memory

#### 1. Short-Term Memory (Working Memory)
Temporary storage of recent information:
- **Capacity:** Limited (7 ± 2 items in humans)
- **Duration:** Seconds to minutes
- **Purpose:** Maintain context for current task

**Example:**
```python
class Agent:
    def __init__(self):
        self.short_term_memory = deque(maxlen=10)
    
    def process_percept(self, percept):
        self.short_term_memory.append(percept)
        # Use recent history for decision making
        context = list(self.short_term_memory)
        action = self.decide(context)
        return action
```

#### 2. Long-Term Memory
Persistent storage of knowledge:
- **Capacity:** Essentially unlimited
- **Duration:** Indefinite
- **Purpose:** Store learned knowledge, experiences, rules

**Types:**
- **Episodic:** Specific experiences ("I saw a red car at 3pm")
- **Semantic:** General knowledge ("Cars have wheels")
- **Procedural:** How to do things ("How to tie shoelaces")

**Example:**
```python
class Agent:
    def __init__(self):
        self.long_term_memory = {
            "rules": [],  # Learned rules
            "experiences": [],  # Past episodes
            "knowledge_base": {}  # Facts and relationships
        }
    
    def store_experience(self, state, action, result):
        self.long_term_memory["experiences"].append({
            "state": state,
            "action": action,
            "result": result,
            "timestamp": now()
        })
    
    def recall_similar_experience(self, current_state):
        similar = find_most_similar(
            current_state,
            self.long_term_memory["experiences"]
        )
        return similar
```

#### 3. External Memory
Storage outside the agent:
- **Databases:** Persistent structured data
- **Files:** Documents, logs
- **Knowledge graphs:** Relationships between entities
- **Vector stores:** Embeddings for semantic search

**Example:**
```python
# LLM agent with external memory
class LLMAgent:
    def __init__(self):
        self.vector_db = VectorDatabase()
    
    def answer_question(self, question):
        # Retrieve relevant context from memory
        relevant_docs = self.vector_db.search(question, top_k=5)
        
        # Use retrieved context in prompt
        prompt = f"""
        Context: {relevant_docs}
        Question: {question}
        Answer:
        """
        
        return llm.generate(prompt)
```

### Memory Mechanisms

#### 1. Attention
Focus on relevant information:
```python
# Transformer attention mechanism
def attention(query, keys, values):
    scores = query @ keys.T / sqrt(d_k)
    weights = softmax(scores)
    output = weights @ values
    return output
```

#### 2. Forgetting
Remove outdated or irrelevant information:
- **Time-based:** Decay old memories
- **Importance-based:** Keep important, forget trivial
- **Capacity-based:** Remove when memory is full

```python
def forget_old_memories(memories, max_age=30_days):
    current_time = now()
    return [m for m in memories if current_time - m.timestamp < max_age]
```

#### 3. Consolidation
Transfer from short-term to long-term:
```python
def consolidate_memory(short_term, long_term):
    # Identify important patterns
    patterns = extract_patterns(short_term)
    
    # Store in long-term memory
    for pattern in patterns:
        if is_novel(pattern, long_term) and is_important(pattern):
            long_term.add(pattern)
```

### Examples

#### Chatbot with Conversation History
```python
class ConversationalAgent:
    def __init__(self):
        self.conversation_history = []
    
    def respond(self, user_message):
        # Add to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Generate response using history for context
        response = llm.generate(
            messages=self.conversation_history,
            max_context=4096
        )
        
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        return response
```

#### Navigation Agent with Map Memory
```python
class NavigationAgent:
    def __init__(self):
        self.map = OccupancyGrid()
        self.visited = set()
    
    def explore(self):
        current_pos = self.get_position()
        
        # Update map with sensor readings
        obstacles = self.scan_environment()
        self.map.update(current_pos, obstacles)
        
        # Mark as visited
        self.visited.add(current_pos)
        
        # Choose unexplored direction
        next_pos = self.choose_unexplored(self.map, self.visited)
        self.move_to(next_pos)
```

### Challenges

- **Memory capacity:** Limited storage
- **Retrieval speed:** Fast access needed
- **Relevance:** Recalling pertinent information
- **Privacy:** Sensitive information
- **Forgetting:** What to keep vs. discard

---

## Integration: How Components Work Together

### Example: Autonomous Delivery Robot

```python
class DeliveryRobot:
    def __init__(self):
        # Memory
        self.map = SpatialMemory()
        self.delivery_history = []
        
        # Learning
        self.path_planner = LearnedPlanner()
    
    def run(self):
        while True:
            # 1. PERCEPTION
            sensors = self.read_sensors()
            obstacles = self.detect_obstacles(sensors.lidar)
            location = self.localize(sensors.gps, sensors.imu)
            
            # 2. REASONING
            if self.battery_low():
                goal = self.charging_station
            elif self.has_package():
                goal = self.package_destination
            else:
                goal = self.depot
            
            # 3. PLANNING
            if self.plan is None or self.environment_changed():
                self.plan = self.path_planner.plan(
                    start=location,
                    goal=goal,
                    obstacles=obstacles
                )
            
            # 4. ACTION
            next_action = self.plan.next_step()
            self.execute_action(next_action)
            
            # 5. LEARNING
            if self.delivery_completed():
                reward = self.calculate_reward()  # Speed, safety, efficiency
                self.path_planner.update(reward)
            
            # 6. MEMORY
            self.map.update(location, obstacles)
            self.delivery_history.append({
                "time": now(),
                "location": location,
                "action": next_action
            })
```

---

## What's Next?

Now that you understand the core components of intelligent agents, continue to [Prerequisites](04-prerequisites.md) to learn about the skills and resources you need to start building your own agents.

---

**Key Takeaways:**
- ✅ **Perception** converts sensor data into internal representations
- ✅ **Reasoning** draws inferences from information (deductive, inductive, probabilistic)
- ✅ **Planning** determines action sequences to achieve goals
- ✅ **Action** executes plans and affects the environment
- ✅ **Learning** improves performance through experience (supervised, RL, etc.)
- ✅ **Memory** stores information for context and learning
- ✅ All components work together in the perception-reasoning-planning-action-learning cycle
