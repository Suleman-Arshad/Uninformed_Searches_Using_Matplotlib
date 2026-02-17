import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

rows, cols = 8, 8
LIMIT = 10  # Max depth the search can go

# Grid Setup
grid = [[0 for _ in range(cols)] for _ in range(rows)]
for k in range(1, 7): grid[k][5] = -1

start_node = (2, 4)
target_node = (4, 2)
grid[start_node[0]][start_node[1]] = 1 
grid[target_node[0]][target_node[1]] = 2 

my_colors = ListedColormap(['red', 'lightgrey', 'green', 'blue', 'yellow', 'cyan'])

def redraw():
    ax.clear()
    ax.set_title(f"Depth-Limited Search (Limit: {LIMIT})", fontsize=12, fontweight='bold')
    ax.imshow(grid, cmap=my_colors, vmin=-1, vmax=4)
    
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            label = "S" if val == 1 else "T" if val == 2 else ""
            ax.text(c, r, label, ha='center', va='center', fontsize=10, color='black', fontweight='bold')
    plt.pause(0.1)

fig, ax = plt.subplots(figsize=(7, 7))
plt.ion()

# --- DLS Logic ---
# Stack stores: (current_node, current_depth)
stack = [(start_node, 0)]
visited = {start_node: (None, 0)} # Stores (Parent, Depth)
found = False



while stack:
    curr, depth = stack.pop() # LIFO behavior
    
    if curr == target_node:
        found = True
        break
    
    # If we haven't reached the limit, expand neighbors
    if depth < LIMIT:
        r, c = curr
        # To maintain the 1->6 order with a Stack (LIFO), 
        # we reverse the list so the first priority is popped last.
        directions = [
            (-1,  0), # 1. Up
            ( 0,  1), # 2. Right
            ( 1,  0), # 3. Bottom
            ( 1,  1), # 4. Bottom-Right (Diagonal)
            ( 0, -1), # 5. Left
            (-1, -1)  # 6. Top-Left (Diagonal)
        ]
        
        # Reverse directions for stack priority
        for dr, dc in reversed(directions):
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                # In DLS, we can revisit a node if we find it at a shallower depth
                if (nr, nc) not in visited or depth + 1 < visited[(nr, nc)][1]:
                    visited[(nr, nc)] = (curr, depth + 1)
                    stack.append(((nr, nc), depth + 1))
                    
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 3
                        redraw()

# --- Path Animation ---
if found:
    path_node = visited.get(target_node)[0]
    while path_node and path_node != start_node:
        grid[path_node[0]][path_node[1]] = 4
        path_node = visited[path_node][0]
        redraw()
else:
    print("Target not found within depth limit.")

plt.ioff()
plt.show()
