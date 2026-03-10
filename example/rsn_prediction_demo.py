import numpy as np


BRANCH = 3
DEPTH = 4


class RSNNode:

    def __init__(self, state, depth=0):

        self.state = state
        self.depth = depth
        self.children = []
        self.value = 0

    def expand(self):

        if self.depth >= DEPTH:
            return

        for _ in range(BRANCH):

            noise = np.random.normal(0, 0.1, len(self.state))

            new_state = self.state + noise

            child = RSNNode(new_state, self.depth + 1)

            self.children.append(child)

            child.expand()


def evaluate(node):

    if not node.children:

        return np.sum(node.state)

    values = [evaluate(child) for child in node.children]

    node.value = max(values)

    return node.value


# initial state (6D)

initial_state = np.random.rand(6)

root = RSNNode(initial_state)

root.expand()

best_value = evaluate(root)

print("Initial state:", initial_state)
print("Best predicted value:", best_value)