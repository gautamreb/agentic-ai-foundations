# Multi-Agent System: Collaborative Task Allocation

## Overview

This example demonstrates a **multi-agent system** where multiple autonomous agents coordinate to efficiently complete tasks through a simple auction mechanism.

## What is a Multi-Agent System?

A multi-agent system (MAS) consists of multiple autonomous agents that:
- **Interact** with each other and the environment
- **Coordinate** to achieve individual or collective goals
- **Communicate** to share information
- **Exhibit emergent behavior** from local interactions
- **Adapt** to other agents' behaviors

### Key Characteristics

1. **Autonomy**: Each agent makes its own decisions
2. **Local views**: Agents have partial information
3. **Decentralization**: No single point of control
4. **Asynchrony**: Agents act independently

## Types of Multi-Agent Interactions

### 1. Cooperative (This Example)
Agents work together toward shared goals:
- Task allocation
- Collaborative problem-solving
- Team coordination

### 2. Competitive
Agents have conflicting goals:
- Games (Chess, Go)
- Markets, auctions
- Resource competition

### 3. Coopetition (Mixed)
Both cooperation and competition:
- Supply chains
- Negotiations
- Coalition formation

## The Task Allocation Example

This example simulates a warehouse or delivery scenario:

**Agents (Workers):**
- Multiple worker agents at different locations
- Each has a capacity (max tasks they can handle)
- Each has different costs based on distance to tasks

**Tasks:**
- Need to be completed
- Located at various positions
- Can be assigned to any agent

**Goal:**
- Minimize total cost (distance traveled)
- Distribute tasks fairly
- Complete all tasks

### The Auction Protocol

Agents use a **Contract Net Protocol** variant:

1. **Task Announcement**: New task is broadcast
2. **Bidding**: Each agent calculates and submits a bid
3. **Winner Selection**: Task awarded to lowest bidder
4. **Commitment**: Winner commits to completing the task

## Real-World Applications

Multi-agent systems are used in:

**Robotics:**
- Warehouse automation (Amazon, Ocado)
- Swarm robotics (drone coordination)
- Multi-robot exploration

**Transportation:**
- Traffic signal coordination
- Ride-sharing (Uber, Lyft dispatch)
- Autonomous vehicle platoons

**Markets:**
- Algorithmic trading
- Supply chain management
- Energy grid balancing

**Games:**
- Team-based AI (StarCraft, Dota)
- NPC coordination
- Procedural content generation

**Distributed Systems:**
- Peer-to-peer networks
- Cloud resource allocation
- Blockchain consensus

## Running the Example

```bash
cd examples/04-multi-agent-system
python multi_agent.py
```

The simulation will:
1. Create multiple worker agents
2. Generate random tasks
3. Show the auction process for each task
4. Display final task allocation
5. Visualize the system state

## Key Concepts Demonstrated

### 1. Communication
Agents exchange messages:
- Task announcements
- Bids
- Confirmations

### 2. Coordination
Agents work together without central control:
- Distributed decision-making
- No single coordinator
- Emergent efficient allocation

### 3. Utility Functions
Each agent evaluates tasks differently:
- Based on distance (cost)
- Based on current load
- Based on capabilities

### 4. Bidding Strategy
Agents compete for tasks:
- Calculate travel cost
- Consider current commitments
- Submit competitive bids

### 5. Emergent Behavior
System-level outcomes from agent interactions:
- Load balancing emerges naturally
- Efficiency without central planning
- Robust to agent failures

## Comparison with Previous Examples

| Aspect | Single Agent | Multi-Agent System |
|--------|--------------|-------------------|
| **Decision-making** | Individual | Distributed |
| **Knowledge** | Complete (for that agent) | Partial, local |
| **Coordination** | Not needed | Essential |
| **Communication** | Environment only | Agent-to-agent |
| **Scalability** | Limited by single agent | Scales with agents |
| **Robustness** | Single point of failure | Redundant, fault-tolerant |
| **Complexity** | Agent complexity | Interaction complexity |

## Communication Protocols

### Speech Acts (FIPA-ACL)
Standard messages types:
- **INFORM**: Share information
- **REQUEST**: Ask for action
- **PROPOSE**: Suggest a plan
- **ACCEPT/REJECT**: Respond to proposal
- **QUERY**: Ask for information

### Contract Net Protocol
1. **Task announcement** (INFORM)
2. **Call for proposals** (REQUEST)
3. **Proposals submitted** (PROPOSE)
4. **Award contract** (ACCEPT)
5. **Rejection** (REJECT)

## Auction Mechanisms

### First-Price Sealed-Bid (This Example)
- All bids submitted simultaneously
- Lowest bidder wins
- Winner pays their bid

### English Auction
- Open, ascending price
- Highest bidder wins
- Good for selling items

### Dutch Auction
- Descending price
- First to accept wins
- Fast resolution

### Vickrey Auction (Second-Price)
- Sealed bids
- Highest bidder wins
- Pays second-highest bid
- Incentive-compatible (truth-telling)

## Game Theory in MAS

### Nash Equilibrium
No agent can improve by changing strategy alone.

### Pareto Efficiency
No agent can improve without hurting another.

### Social Welfare
Maximizing sum of all agents' utilities.

**This example aims for:** Minimize total cost (social welfare optimization)

## Advanced Multi-Agent Concepts

### 1. Coalition Formation
Agents form groups for tasks requiring multiple workers.

### 2. Negotiation
Agents discuss and agree on terms (price, deadlines, etc.).

### 3. Trust and Reputation
Agents track others' reliability and prefer trustworthy partners.

### 4. Learning in MAS
Agents learn to predict others' behavior and adapt strategies.

### 5. Mechanism Design
Design rules (auctions, protocols) for desired outcomes.

## Challenges in Multi-Agent Systems

1. **Communication overhead**: Too many messages slow system
2. **Coordination complexity**: Hard to ensure efficient cooperation
3. **Conflicts**: Agents may have opposing goals
4. **Scalability**: Performance with many agents
5. **Partial observability**: Agents don't see everything
6. **Dynamic environments**: Agents/tasks come and go

## Extensions and Exercises

Try modifying the code to:

1. **Dynamic tasks**: Tasks arrive over time, not all at once

2. **Agent capabilities**: Some agents can do some tasks, not others

3. **Coalitions**: Some tasks require multiple agents working together

4. **Learning**: Agents learn better bidding strategies

5. **Communication costs**: Sending messages costs energy/time

6. **Failures**: Agents can fail; system must recover

7. **Negotiation**: After winning, agents can negotiate terms

8. **Reputation**: Track agent performance, prefer reliable agents

## From Cooperative to Competitive

**Cooperative** (minimizing total cost):
```python
my_bid = my_cost_for_task  # Truthful bidding
```

**Competitive** (maximizing profit):
```python
my_bid = my_cost + markup  # Add profit margin
```

**Strategic** (learning from others):
```python
my_bid = predict_winning_bid() - small_amount  # Just beat competition
```

## Visualization

The example shows:
- Agent positions (workers)
- Task positions
- Assignments (which agent gets which task)
- Costs and distances
- Auction process

## Further Reading

### Books
- Shoham & Leyton-Brown, "Multiagent Systems" (free online)
- Wooldridge, "An Introduction to MultiAgent Systems"
- Weiss, "Multiagent Systems" (comprehensive handbook)

### Papers
- Smith, "The Contract Net Protocol" (1980) - Classic coordination protocol
- Vickrey, "Counterspeculation, Auctions, and Competitive Sealed Tenders" (1961)
- Stone & Veloso, "Multiagent Systems: A Survey from a Machine Learning Perspective" (2000)

### Conferences
- AAMAS (Autonomous Agents and Multi-Agent Systems)
- AAAI Multi-Agent Systems track

### Tools and Frameworks
- **SPADE**: Multi-agent platform in Python
- **MASON**: Multi-agent simulation library
- **NetLogo**: Agent-based modeling environment
- **Mesa**: Python framework for agent-based models

---

## Summary

Multi-agent systems represent the cutting edge of AI:
- Real-world problems often involve multiple entities
- Coordination is key to efficiency
- Emergent behaviors from simple rules
- Scales better than monolithic systems
- More robust and adaptive

**Key Insight:** Complex, intelligent behavior can emerge from simple agents following local rules and interacting with each other!

---

**Congratulations!** You've completed all four core examples:
1. ✅ Reactive Agent (Thermostat)
2. ✅ Deliberative Agent (A* Pathfinding)
3. ✅ Learning Agent (Q-Learning)
4. ✅ Multi-Agent System (Task Allocation)

**Next Steps:** Move on to the [Weekly Exercises](../../exercises/) to apply what you've learned!
