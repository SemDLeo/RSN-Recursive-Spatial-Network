# RSN — Recursive Spatial Network

**Recursive Spatial Network (RSN)** is a prediction framework designed to explore future state trajectories through recursive expansion in a **6-dimensional hypercube state space**.

Unlike traditional predictive models that estimate a single future outcome, RSN generates a **recursive tree of possible future states**, allowing the system to evaluate multiple potential trajectories simultaneously.

The model integrates:

* **High-dimensional state representation**
* **Recursive future expansion**
* **Hash-based spatial node mapping**
* **Distributed storage architecture**

RSN aims to provide a **general framework for prediction and simulation in complex dynamic systems**, including but not limited to:

* financial markets
* physical simulations
* weather systems
* social dynamics
* autonomous planning systems

---

# Core Concept

RSN models future evolution as a **recursive state expansion process** in a structured state space.

At each step, a node representing the current system state generates multiple possible future states.

These nodes form a **recursive prediction tree** embedded in a **6-dimensional state space**.

Key components:

```
State Encoding → Recursive Expansion → Spatial Mapping → Value Evaluation
```

---

# 1. State Representation

Each node in RSN represents a system state encoded as a **6-dimensional feature vector**:

$$
f_i \in \mathbb{R}^6
$$

A general representation:

$$
f_i = (s_i, h_i, i_{1,i}, i_{2,i}, i_{3,i}, r_i)
$$

Where:

* $s_i$ : system state encoding
* $h_i$ : historical summary
* $i_{1,i}, i_{2,i}, i_{3,i}$ : indicators
* $r_i$ : resource/value variable


These features are **domain-independent** and can represent different systems.

Example applications:

Financial systems

```
RSI
MACD
Volume
```

Environmental systems

```
temperature
humidity
pressure
```

Social systems

```
population
mobility
economic index
```

---

# 2. 6D Hypercube State Space

The state vector lies within a **6-dimensional hypercube**:

$$
\mathcal{H}_6 = [0,1]^6
$$

The hypercube structure provides:

* balanced dimensional complexity
* high representational capacity
* symmetric neighborhood topology

A discrete 6-dimensional hypercube contains:

```
2^6 = 64 vertices
192 edges
```

This structure enables efficient traversal and exploration of nearby states.

---

# 3. Recursive State Expansion

Future states are generated recursively.

For a node (n_t):

$$
n_{t+1,j} = G(n_t, \epsilon_j)
$$

Where:

$G$ is the state generator
$\epsilon_j$ is a stochastic perturbation.

State update:

$$
f_{t+1} = \Phi(f_t, \epsilon)
$$

The recursive expansion forms a prediction tree.

If each node generates $C$ branches and the depth is $D$:

$$
N = \sum_{k=0}^{D} C^k
$$

This tree represents a **set of possible future trajectories**.

---

# 4. Spatial Node Mapping

To enable scalable computation and visualization, each node is assigned a spatial coordinate.

A node ID is generated using hashing:

```
node_id = hash(depth, index, state)
```

The hash is mapped to a spatial grid:

```
x = hash(id) mod Nx
y = hash(id>>8) mod Ny
z = hash(id>>16) mod Nz
```

This mapping ensures:

* deterministic node placement
* unique spatial coordinates
* efficient indexing

---

# 5. Distributed Storage

The hashed node ID also enables **distributed storage and sharding**.

Nodes are assigned to storage shards:

```
shard = node_id mod M
```

Where **M** is the number of storage nodes.

Advantages:

* O(1) lookup
* load-balanced distribution
* scalable node expansion
* distributed recursive computation

---

# 6. Value Propagation

Each node may carry a value or reward signal.

Value update:

$$
v_{t+1} = v_t + R(n_t, n_{t+1})
$$

Where $R$ is a reward or value function.

Examples:

Financial systems

```
profit
```

AI planning

```
reward
```

Physical systems

```
energy change
```

---

# 7. Optimal Trajectory Search

RSN searches for trajectories maximizing cumulative value:

$$
P^* = \arg\max_P \sum_{n_i \in P} v_i
$$

This resembles **Monte Carlo trajectory search**, but operates within a structured **high-dimensional state space**.

---

# 8. Mathematical Advantages

The combination of **6-dimensional state space and recursive expansion** offers several advantages.

### Balanced complexity

State space size:

$$
|\mathcal{S}| = n^6
$$

This provides high expressiveness while remaining computationally manageable.

---

### Multi-path prediction stability

Traditional predictors produce a single trajectory.

RSN generates multiple future paths:

$$
\big\{ f_{t+1}^{(1)}, \dots, f_{t+1}^{(C)} \big\}
$$


This reduces long-term prediction sensitivity to noise.

---

### State space coverage

With sufficient branching:

$$
C \rightarrow \infty
$$

RSN approximates the full reachable state space.

---

# 9. Potential Applications

RSN is a **general prediction framework** applicable to many domains.

Possible applications include:

* financial market simulation
* weather forecasting
* energy grid prediction
* autonomous planning systems
* complex system simulation

---

# 10. Future Work

Planned developments include:

* reference implementation
* distributed RSN engine
* visualization tools
* reinforcement learning integration

A reference implementation will be released in:

```
RSN-engine (coming soon)
```

---

# Citation

If you reference this project:

```
@article{sem.d.leo2026rsn,
  title={Recursive Spatial Network: Prediction over a 6D Hypercube State Space},
  author={Leo},
  year={2026}
}
```

---

# License

MIT License

---

# Author

Sem.D.Leo
2026
