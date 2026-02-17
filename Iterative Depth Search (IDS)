import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

rows, cols = 8, 8

# Grid Setup
grid = [[0 for _ in range(cols)] for _ in range(rows)]
for k in range(1, 7): grid[k][5] = -1

start_node = (4, 7)
target_node = (4, 2)
grid[start_node[0]][start_node[1]] = 1 
grid[target_node[0]][target_node[1]] = 2 

my_colors = ListedColormap(['red', 'lightgrey', 'green', 'blue', 'yellow', 'cyan'])

def redraw(current_limit):
    ax.clear()
    ax.set_title(f"IDDFS - Current Depth Limit: {current_limit}", fontsize=12, fontweight='bold')
    ax.imshow(grid, cmap=my_colors, vmin=-1, vmax=4)
    
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            label = "S" if val == 1 else "T" if val == 2 else ""
            ax.text(c, r, label, ha='center', va='center', fontsize=10, color='black', fontweight='bold')
    plt.pause(0.01) # Faster pause since it repeats often

fig, ax = plt.subplots(figsize=(7, 7))
plt.ion()

def depth_limited_search(start, target, limit):
    """A standard DLS that returns (found_bool, parent_map)"""
    stack = [(start, 0)]
    visited = {start: (None, 0)}
    
    # Directions in strict priority: Up, Right, Bottom, Bottom-Right, Left, Top-Left
    directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]
    
    while stack:
        curr, depth = stack.pop()
        
        if curr == target:
            return True, visited
        
        if depth < limit:
            r, c = curr
            # Reverse directions to maintain stack priority (Up is popped first)
            for dr, dc in reversed(directions):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    # Only visit if not seen in THIS iteration OR seen at a deeper level
                    if (nr, nc) not in visited or depth + 1 < visited[(nr, nc)][1]:
                        visited[(nr, nc)] = (curr, depth + 1)
                        stack.append(((nr, nc), depth + 1))
                        
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 3
                            redraw(limit)
    return False, visited

# --- IDDFS Logic ---
found = False
final_visited = {}



for current_limit in range(rows * cols):
    # Reset grid for visual clarity of each iteration
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 3: grid[r][c] = 0
            
    found, final_visited = depth_limited_search(start_node, target_node, current_limit)
    
    if found:
        break

# --- Path Animation ---
if found:
    path_node = final_visited.get(target_node)[0]
    while path_node and path_node != start_node:
        grid[path_node[0]][path_node[1]] = 4
        path_node = final_visited[path_node][0]
        redraw(current_limit)

plt.ioff()
plt.show()
