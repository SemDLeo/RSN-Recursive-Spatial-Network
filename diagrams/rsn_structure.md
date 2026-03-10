# RSN System Architecture

This diagram illustrates the core architecture of the Recursive Spatial Network (RSN).

```mermaid
flowchart TD

A[Input State Vector f ∈ R6]

A --> B[State Representation Layer]

B --> C[Recursive Expansion Layer]

C --> D1[Future State 1]
C --> D2[Future State 2]
C --> D3[Future State 3]

D1 --> E[Value Evaluation]
D2 --> E
D3 --> E

E --> F[Optimal Path Selection]

F --> G[Prediction Output]
