"""
Week 4 Exercise Solution: Multi-Agent Marketplace

Implements buyer/seller agents with auction mechanisms.

Author: Agentic AI Foundations
"""

import random
from typing import List, Tuple


class Item:
    """Represents an item to be bought/sold."""
    def __init__(self, item_id: int, name: str):
        self.id = item_id
        self.name = name
        self.sold_price = None
        self.buyer = None
        self.seller = None


class BuyerAgent:
    """Agent that wants to buy items."""
    
    def __init__(self, agent_id: int, max_prices: dict):
        self.id = agent_id
        self.max_prices = max_prices  # {item_id: max_price}
        self.purchases = []
    
    def calculate_bid(self, item: Item, current_price: float = 0) -> float:
        """Calculate bid for an item."""
        if item.id not in self.max_prices:
            return 0
        
        max_price = self.max_prices[item.id]
        
        # Bid slightly below max (leave room for profit)
        bid = max_price * 0.95
        
        # In English auction, bid increment above current price
        if current_price > 0:
            bid = max(bid, current_price + 1)
        
        return min(bid, max_price)
    
    def accept_price(self, item: Item, price: float) -> bool:
        """Decide whether to accept a price."""
        if item.id not in self.max_prices:
            return False
        return price <= self.max_prices[item.id]


class SellerAgent:
    """Agent that wants to sell items."""
    
    def __init__(self, agent_id: int, min_prices: dict):
        self.id = agent_id
        self.min_prices = min_prices  # {item_id: min_price}
        self.sales = []
    
    def accept_bid(self, item: Item, bid: float) -> bool:
        """Decide whether to accept a bid."""
        if item.id not in self.min_prices:
            return False
        return bid >= self.min_prices[item.id]
    
    def ask_price(self, item: Item) -> float:
        """Set asking price for an item."""
        if item.id not in self.min_prices:
            return float('inf')
        
        # Ask slightly above minimum
        return self.min_prices[item.id] * 1.05


class AuctioneerAgent:
    """Facilitates auctions between buyers and sellers."""
    
    def __init__(self):
        self.transactions = []
    
    def run_english_auction(self, item: Item, buyers: List[BuyerAgent], 
                           seller: SellerAgent) -> Tuple[float, BuyerAgent]:
        """
        English auction: ascending price, highest bidder wins.
        
        Returns:
            (final_price, winning_buyer) or (0, None)
        """
        current_price = seller.ask_price(item)
        active_buyers = buyers.copy()
        
        print(f"\n  Starting English auction for {item.name}")
        print(f"  Starting price: ${current_price:.2f}")
        
        while len(active_buyers) > 1:
            # Get bids from active buyers
            bids = []
            for buyer in active_buyers:
                bid = buyer.calculate_bid(item, current_price)
                if buyer.accept_price(item, bid):
                    bids.append((bid, buyer))
            
            if not bids:
                break
            
            # Highest bid becomes new price
            highest_bid, highest_bidder = max(bids, key=lambda x: x[0])
            current_price = highest_bid
            
            # Remove low bidders
            active_buyers = [b for _, b in bids if b.accept_price(item, current_price + 1)]
        
        # Check if seller accepts final price
        if active_buyers and seller.accept_bid(item, current_price):
            winner = active_buyers[0]
            print(f"  SOLD to Buyer {winner.id} for ${current_price:.2f}")
            return current_price, winner
        else:
            print(f"  NOT SOLD (no acceptable bids)")
            return 0, None
    
    def run_sealed_bid_auction(self, item: Item, buyers: List[BuyerAgent],
                               seller: SellerAgent) -> Tuple[float, BuyerAgent]:
        """
        Sealed-bid auction: all bids submitted, highest wins.
        
        Returns:
            (final_price, winning_buyer) or (0, None)
        """
        print(f"\n  Starting sealed-bid auction for {item.name}")
        
        # Collect all bids
        bids = []
        for buyer in buyers:
            bid = buyer.calculate_bid(item)
            if buyer.accept_price(item, bid):
                bids.append((bid, buyer))
                print(f"    Buyer {buyer.id} bids ${bid:.2f}")
        
        if not bids:
            print(f"  NOT SOLD (no bids)")
            return 0, None
        
        # Highest bid wins
        winning_bid, winner = max(bids, key=lambda x: x[0])
        
        # Check if seller accepts
        if seller.accept_bid(item, winning_bid):
            print(f"  SOLD to Buyer {winner.id} for ${winning_bid:.2f}")
            return winning_bid, winner
        else:
            print(f"  NOT SOLD (seller rejected ${winning_bid:.2f})")
            return 0, None
    
    def run_marketplace(self, items: List[Item], buyers: List[BuyerAgent],
                       sellers: List[SellerAgent], auction_type='sealed'):
        """Run marketplace for all items."""
        print("\n" + "=" * 60)
        print(f"MARKETPLACE: {auction_type.upper()} AUCTIONS")
        print("=" * 60)
        
        for i, item in enumerate(items):
            seller = sellers[i % len(sellers)]  # Assign seller
            
            if auction_type == 'english':
                price, buyer = self.run_english_auction(item, buyers, seller)
            else:
                price, buyer = self.run_sealed_bid_auction(item, buyers, seller)
            
            if buyer:
                item.sold_price = price
                item.buyer = buyer
                item.seller = seller
                buyer.purchases.append(item)
                seller.sales.append(item)
                self.transactions.append((item, price, buyer, seller))
        
        self.print_summary()
    
    def print_summary(self):
        """Print transaction summary."""
        print("\n" + "=" * 60)
        print("MARKETPLACE SUMMARY")
        print("=" * 60)
        
        if self.transactions:
            total_volume = sum(price for _, price, _, _ in self.transactions)
            avg_price = total_volume / len(self.transactions)
            
            print(f"Transactions: {len(self.transactions)}")
            print(f"Total volume: ${total_volume:.2f}")
            print(f"Average price: ${avg_price:.2f}")
        else:
            print("No transactions completed")


def demonstrate():
    """Demonstrate multi-agent marketplace."""
    print("=" * 60)
    print("WEEK 4 SOLUTION: MULTI-AGENT MARKETPLACE")
    print("=" * 60)
    
    # Create items
    items = [Item(i, f"Item-{i}") for i in range(5)]
    
    # Create buyer agents (willing to pay)
    buyers = [
        BuyerAgent(0, {0: 50, 1: 60, 2: 70}),
        BuyerAgent(1, {0: 55, 1: 65, 2: 75, 3: 80}),
        BuyerAgent(2, {2: 65, 3: 85, 4: 90}),
    ]
    
    # Create seller agents (minimum acceptable)
    sellers = [
        SellerAgent(0, {0: 40, 1: 50}),
        SellerAgent(1, {2: 60, 3: 70, 4: 75}),
    ]
    
    # Run marketplace
    auctioneer = AuctioneerAgent()
    auctioneer.run_marketplace(items, buyers, sellers, auction_type='sealed')
    
    print("\n" + "=" * 60)
    print("KEY INSIGHTS")
    print("=" * 60)
    print("✅ Market mechanisms coordinate self-interested agents")
    print("✅ Prices emerge from supply and demand")
    print("✅ Auction design affects outcomes")
    print("✅ Multi-agent systems enable complex interactions")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate()
