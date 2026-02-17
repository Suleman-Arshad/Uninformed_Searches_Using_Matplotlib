import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

rows, cols = 8, 8

# Grid Setup
grid = [[0 for _ in range(cols)] for _ in range(rows)]
for k in range(1, 7): grid[k][5] = -1

start_node = (2, 7)
target_node = (4, 2)
grid[start_node[0]][start_node[1]] = 1 
grid[target_node[0]][target_node[1]] = 2 

# Colors: -1:Red, 0:Grey, 1:Green, 2:Blue, 3:Yellow (Explored), 4:Cyan (Path)
my_colors = ListedColormap(['red', 'lightgrey', 'green', 'blue', 'yellow', 'cyan'])

def redraw():
    ax.clear()
    ax.set_title("Bidirectional Search", fontsize=14, fontweight='bold')
    ax.imshow(grid, cmap=my_colors, vmin=-1, vmax=4)
    
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            label = "S" if val == 1 else "T" if val == 2 else ""
            ax.text(c, r, label, ha='center', va='center', fontsize=10, color='black', fontweight='bold')
    plt.pause(0.1)

fig, ax = plt.subplots(figsize=(7, 7))
plt.ion()

# --- Bidirectional Logic ---
q_start = [start_node]
q_target = [target_node]

# Visited maps store the parent node to reconstruct the path later
vis_start = {start_node: None}
vis_target = {target_node: None}

meeting_node = None

# Clockwise Order: Up, Right, Bottom, Bottom-Right, Left, Top-Left
directions = [(-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)]



while q_start and q_target:
    # 1. Expand Forward Search
    curr_s = q_start.pop(0)
    for dr, dc in directions:
        nr, nc = curr_s[0] + dr, curr_s[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
            if (nr, nc) not in vis_start:
                vis_start[(nr, nc)] = curr_s
                if (nr, nc) in vis_target: # Intersection found!
                    meeting_node = (nr, nc)
                    break
                if grid[nr][nc] == 0: grid[nr][nc] = 3
                q_start.append((nr, nc))
                redraw()
    if meeting_node: break

    # 2. Expand Backward Search
    curr_t = q_target.pop(0)
    for dr, dc in directions:
        nr, nc = curr_t[0] + dr, curr_t[1] + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
            if (nr, nc) not in vis_target:
                vis_target[(nr, nc)] = curr_t
                if (nr, nc) in vis_start: # Intersection found!
                    meeting_node = (nr, nc)
                    break
                if grid[nr][nc] == 0: grid[nr][nc] = 3
                q_target.append((nr, nc))
                redraw()
    if meeting_node: break

# --- Path Reconstruction ---
if meeting_node:
    # Trace back from meeting point to Start
    curr = meeting_node
    while curr:
        if grid[curr[0]][curr[1]] not in [1, 2]: grid[curr[0]][curr[1]] = 4
        curr = vis_start[curr]
        redraw()
    
    # Trace back from meeting point to Target
    curr = vis_target[meeting_node]
    while curr:
        if grid[curr[0]][curr[1]] not in [1, 2]: grid[curr[0]][curr[1]] = 4
        curr = vis_target[curr]
        redraw()

plt.ioff()
plt.show()
