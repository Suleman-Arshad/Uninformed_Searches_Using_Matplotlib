Uninformed Search Algorithms Visualizer

This repository contains a collection of Python scripts that visualize six fundamental **Uninformed Search** algorithms. Using an 8x8 grid, these scripts demonstrate how different search strategies navigate from a start node to a target node while navigating obstacles and following strict movement constraints.

🛠️ Installation & Dependencies

To run these visualizations, you must have Python installed on your system. The project uses the `matplotlib` library for the graphical interface and real-time animations.

Step 1: Install Matplotlib
Open your terminal or command prompt and run:
pip install matplotlib
When selecting a search strategy for navigating a grid, several uninformed search algorithms offer distinct advantages depending on the goal. Breadth-First Search (BFS) is the standard for unweighted grids because it explores level by level, guaranteed to find the shortest path. In contrast, Depth-First Search (DFS) dives as deep as possible into a single branch before backtracking, which can be faster in a best-case scenario but is not guaranteed to be optimal. To handle weighted paths, such as accounting for the $1.41$ cost of a diagonal move versus the $1.0$ cost of a straight move, Uniform Cost Search (UCS) is used to find the mathematically cheapest path.Variations of these depth-based searches include Depth-Limited Search (DLS), which adds a fixed boundary to DFS to prevent it from wandering into infinite loops, and Iterative Deepening DFS (IDDFS), which repeatedly runs DLS with increasing limits to combine the memory efficiency of DFS with the optimality of BFS. Finally, Bidirectional Search optimizes the process by initiating two simultaneous searches—one from the start and one from the target—to meet in the middle, significantly reducing the number of nodes explored compared to a traditional one-way search.

⚙️ Movement Constraints & Logic
All algorithms strictly follow a Clockwise Priority for expanding neighbors. Only the Main Diagonal (Top-Left to Bottom-Right) is permitted.
1. Strict Expansion Order:
Up (-1, 0)
Right (0, 1)
Bottom (1, 0)
Bottom-Right (1, 1) (Main Diagonal)
Left (0, -1)
Top-Left (-1, -1) (Main Diagonal)
Note: Top-Right and Bottom-Left movements are excluded.
2. Visualization Legend:
🟩 Green (S): Start Node
🟦 Blue (T): Target Node
🟥 Red: Walls / Obstacles (Value: -1)
🟨 Yellow: Explored Cells (Frontier)
🟦 Cyan: Final Calculated Path

💻 How to Run
Ensure all your .py files are in the same directory.
Run your desired algorithm from the terminal:
python ucs_pathfinding.py
An interactive window will appear, showing the step-by-step search process.

💡 Search Insights
DFS Best Case: Given the "Up" priority, the best case for DFS is when the target is directly above the start node.
UCS Optimality: In the UCS implementation, straight moves cost 1.0 and diagonal moves cost 1.41, ensuring the path found is the shortest physical distance.
IDDFS Utility: IDDFS is particularly useful for finding the shortest path when memory is limited, as it mimics BFS behavior using only DFS-level memory.
