import numpy as np
import yfinance as yf

# ===============================
# Parameters
# ===============================

TICKER = "BTC-USD"
START = "2025-01-01"
END = "2026-12-31"

LOOKBACK = 20
BRANCH = 3
DEPTH = 3

# ===============================
# Load data
# ===============================

df = yf.download(TICKER, start=START, end=END)
prices = df["Close"].values


# ===============================
# RSN Node
# ===============================

class RSNNode:

    def __init__(self, price, depth=0):
        self.price = price
        self.depth = depth
        self.children = []
        self.value = 0

    def expand(self):

        if self.depth >= DEPTH:
            return

        for _ in range(BRANCH):

            future_price = self.price * (1 + np.random.normal(0, 0.01))

            child = RSNNode(future_price, self.depth + 1)

            self.children.append(child)

            child.expand()


# ===============================
# Evaluate tree
# ===============================

def evaluate(node):

    if not node.children:
        return node.price

    values = [evaluate(child) for child in node.children]

    node.value = max(values)

    return node.value


# ===============================
# Run example
# ===============================

current_price = prices[-1]

root = RSNNode(current_price)

root.expand()

prediction = evaluate(root)

print("Current price:", current_price)
print("Predicted future price:", prediction)