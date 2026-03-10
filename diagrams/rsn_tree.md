# RSN Recursive Prediction Tree

This diagram illustrates how RSN expands possible future states recursively.

```mermaid
graph TD

A[node(t)]

A --> B[node(t+1,1)]
A --> C[node(t+1,2)]
A --> D[node(t+1,3)]

B --> E[node(t+2,1)]
B --> F[node(t+2,2)]

C --> G[node(t+2,3)]
C --> H[node(t+2,4)]

D --> I[node(t+2,5)]
D --> J[node(t+2,6)]
