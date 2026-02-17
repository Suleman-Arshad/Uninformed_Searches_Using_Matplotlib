import matplotlib.pyplot as plt
import heapq
from matplotlib.colors import ListedColormap

rows, cols = 8, 8

# Grid Setup: 0: Empty, -1: Wall, 1: Start, 2: Target
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Wall Restriction
for k in range(1, 7): 
    grid[k][5] = -1

start_node = (2, 4)
target_node = (4, 2)
grid[start_node[0]][start_node[1]] = 1 
grid[target_node[0]][target_node[1]] = 2 

# Colors: -1:Red, 0:Grey, 1:Green, 2:Blue, 3:Yellow, 4:Cyan
my_colors = ListedColormap(['red', 'lightgrey', 'green', 'blue', 'yellow', 'cyan'])

def redraw(costs_map):
    ax.clear()
    ax.set_title("Uniform Cost Search Animation", fontsize=10, fontweight='bold')
    ax.imshow(grid, cmap=my_colors, vmin=-1, vmax=4)
    
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            label = ""
            if val == 1: label = "S"
            elif val == 2: label = "T"
            elif (r, c) in costs_map and val != -1:
                label = f"{costs_map[(r, c)]:.1f}"
            
            ax.text(c, r, label, ha='center', va='center', fontsize=8, 
                    color='black', fontweight='bold' if label in "ST" else 'normal')
    plt.pause(0.05)

fig, ax = plt.subplots(figsize=(7, 7))
plt.ion()

# --- UCS Logic ---
priority_queue = [(0, start_node)]
visited = {start_node: None}
costs = {start_node: 0}
found = False

while priority_queue:
    current_cost, curr = heapq.heappop(priority_queue)
    
    if curr == target_node:
        found = True
        break
    
    r, c = curr

    # --- STRICT MOVEMENT ORDER ---
    # 1. Up, 2. Right, 3. Bottom, 4. Bottom-Right (D), 5. Left, 6. Top-Left (D)
    directions = [
        (-1,  0, 1.0), # 1. Up
        ( 0,  1, 1.0), # 2. Right
        ( 1,  0, 1.0), # 3. Bottom
        ( 1,  1, 1.4), # 4. Bottom-Right (Main Diagonal)
        ( 0, -1, 1.0), # 5. Left
        (-1, -1, 1.4)  # 6. Top-Left (Main Diagonal)
    ]
    
    for dr, dc, weight in directions:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
            new_total_cost = current_cost + weight
            
            # UCS logic: check if this is the cheapest path found so far
            if (nr, nc) not in costs or new_total_cost < costs[(nr, nc)]:
                costs[(nr, nc)] = round(new_total_cost, 2)
                visited[(nr, nc)] = curr
                heapq.heappush(priority_queue, (new_total_cost, (nr, nc)))
                
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 3
                    redraw(costs)

# --- Path Animation ---
if found:
    path_node = visited.get(target_node)
    while path_node and path_node != start_node:
        grid[path_node[0]][path_node[1]] = 4
        path_node = visited[path_node]
        redraw(costs)

plt.ioff()
plt.show()
