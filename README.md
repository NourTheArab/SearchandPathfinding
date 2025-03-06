# **Search and Pathfinding - Lab A**

## **Overview**
This project implements and compares four search algorithms to solve a **maze navigation problem**, where an agent (mouse) must collect all rewards while finding the optimal path.

## **Maze Representation**
- **P** → Agent's starting position.
- **.** → Rewards (prizes to collect).
- **%** → Walls (impassable obstacles).
- **Spaces (` `)** → Open paths the agent can traverse.

## **Implemented Search Algorithms**

### Depth-First Search (DFS)
- Uses a **stack (LIFO)** to explore deep paths first.
- Does **not guarantee** the shortest path.
- Can get stuck exploring deep branches.

### Breadth-First Search (BFS)
- Uses a **queue (FIFO)** to explore paths layer by layer.
- **Guarantees** the shortest path.
- Expands **many nodes**, leading to high memory usage.

### Greedy Best-First Search (GBFS)
- Uses a **priority queue** based on a heuristic.
- **Heuristic:** Manhattan distance to the closest reward.
- **Fast**, but may not find the best path.

### A* Search (A**)
- Uses **both path cost (`g`) and heuristic (`h`)**.
- **Formula:** `f(n) = g(n) + h(n)`.
- **Most efficient algorithm**, balancing speed and optimality.

### Output
Once you run python State.py, it will prompt you to enter a maze file name. I have done this so that I don't use hard-coded mazes, and open it for further uses. 
Once you write the full file name, the script will run and show you step-by-step what's happening. 

#### You can also type q to quit.










