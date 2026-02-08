# Week 4 Exercise: Multi-Agent Marketplace

## Learning Objectives

- ✅ Design multi-agent systems
- ✅ Implement agent communication protocols
- ✅ Handle cooperative and competitive interactions
- ✅ Analyze emergent system behavior
- ✅ Optimize collective outcomes

## Background

Review [Example 04: Multi-Agent System](../../examples/04-multi-agent-system/) and multi-agent coordination.

## Problem Statement

Create a **multi-agent marketplace** where:
- **Buyer agents** want to purchase items at lowest price
- **Seller agents** want to sell items at highest price
- **Auctioneer** facilitates transactions
- System should reach efficient market equilibrium

### Requirements

**Part 1: Agent Implementation (40 points)**

Implement:
1. **BuyerAgent**:
   - Has maximum willingness to pay for each item
   - Submits bids in auctions
   - Strategy: Don't bid above max price

2. **SellerAgent**:
   - Has minimum acceptable price for each item
   - Responds to bids
   - Strategy: Accept if bid ≥ minimum price

3. **AuctioneerAgent**:
   - Manages multiple simultaneous auctions
   - Matches buyers and sellers
   - Records transaction prices

**Part 2: Auction Mechanisms (30 points)**

Implement two auction types:
1. **English Auction**: Ascending price, highest bidder wins
2. **Double Auction**: Buyers and sellers submit orders, auctioneer matches

Compare:
- Transaction success rate
- Price efficiency (vs. theoretical optimal)
- Computational cost

**Part 3: Emergent Behavior Analysis (30 points)**

Analyze:
- Market price convergence
- Effect of number of agents on efficiency
- Effect of information asymmetry
- Strategic bidding vs. truthful bidding

## Starter Code

```python
class BuyerAgent:
    def __init__(self, agent_id, max_price):
        self.id = agent_id
        self.max_price = max_price
    
    def calculate_bid(self, current_price, item):
        # Bidding strategy
        pass

class SellerAgent:
    def __init__(self, agent_id, min_price):
        self.id = agent_id
        self.min_price = min_price
    
    def accept_bid(self, bid_price, item):
        # Acceptance strategy
        pass

class AuctioneerAgent:
    def run_auction(self, item, buyers, sellers):
        # Auction protocol
        pass
```

## Test Scenarios

1. **5 buyers, 5 sellers, 5 items**
   - Balanced market
   - Should reach equilibrium price

2. **10 buyers, 3 sellers, 5 items**
   - Seller's market
   - Prices should be higher

3. **3 buyers, 10 sellers, 5 items**
   - Buyer's market
   - Prices should be lower

## Evaluation Criteria

- Correctness: Agents follow protocols
- Efficiency: Market clears (all possible trades happen)
- Code quality: Clean, well-documented
- Analysis: Insightful discussion of results

## Bonus Challenges

1. **Learning agents**: Buyers/sellers learn optimal strategies
2. **Reputation system**: Track agent reliability
3. **Coalition formation**: Buyers form groups to negotiate
4. **Dynamic inventory**: Items arrive/leave over time

## Expected Insights

- Market efficiency emerges from individual rationality
- Information affects price discovery
- Auction design impacts outcomes
- Scalability challenges in large systems

**Solution:** See [solution4.py](solution4.py)

---

**Congratulations!** Completing this exercise completes the 4-week curriculum. You now have foundation in:
- ✅ Reactive agents
- ✅ Deliberative agents  
- ✅ Learning agents
- ✅ Multi-agent systems

**Next Steps:** Build your own projects, explore advanced topics, contribute to open source!
