import matplotlib.pyplot as plt # Provides tools for creating visualizations and plots
from matplotlib.colors import ListedColormap # Allows creating a custom list of colors for the grid

rows=8
cols=8
# Grid Making
grid=[]
for i in range(rows):
    new_row=[]
    for j in range(cols):
        new_row.append(0)
    grid.append(new_row)
# Put -1 to built the restriction
for k in range (1,7):
    grid[k][5]=-1

start_node = (2, 7)
target_node = (4, 2)
grid[start_node[0]][start_node[1]] = 1 # Give number to access the Starting block of grid for text
grid[target_node[0]][target_node[1]] = 2 # Give number to access the Target block of grid for text

# Colors: -1:red, 0:lightgrey, 1:green, 2:blue, 3:yellow (Explored), 4:cyan (Path)
my_colors = ListedColormap(['red', 'lightgrey', 'green', 'blue', 'yellow', 'cyan'])

def redraw():
    ax.clear() # Removes all previous drawings from the current axes to start fresh
    # vmin and vmax ensure the colors map correctly to our numbers (-1 to 4)
    ax.set_title("DFS Pathfinding Animation", fontsize=14, fontweight='bold') # Sets the text label at the top of the plot
    ax.imshow(grid, cmap=my_colors, vmin=-1, vmax=4) # Renders the 2D list as a colored image on the screen
    
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            # Add text in the grid box with the numbers assigned to the grid block
            if val == 1:
                label = "S"
            elif val == 2:
                label = "T"
            else:
                label = ""
            
            ax.text(c, r, label, ha='center', va='center', color='black', fontweight='bold') # Places a text string at a specific (x, y) coordinate
    
    plt.pause(0.05) # Pauses execution briefly to allow the GUI to update and show the animation

fig, ax = plt.subplots() # Creates a new figure window and a set of axes for drawing
plt.ion() # Turns on interactive mode so the plot updates immediately without blocking the code

# --- DFS Logic ---
stack = [start_node]
visited = {start_node: None}
found = False

while stack and not found:
    curr = stack.pop() # Remove From last to explore it
    
    if curr == target_node:
        found = True
        break
    
    r, c = curr
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1,-1), (1,1)]:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] != -1 and (nr, nc) not in visited:
                visited[(nr, nc)] = curr
                stack.append((nr, nc)) # Adds a new neighbor to the end of the to-do list
                
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 3 
                    redraw()

# --- Path Animation ---
path_node = visited.get(target_node) # Retrieves the value associated with the key from the dictionary
while path_node and path_node != start_node:
    grid[path_node[0]][path_node[1]] = 4
    path_node = visited[path_node]
    redraw()

plt.ioff() # Disables interactive mode so the final window stays open normally
plt.show() # Displays the final figure and waits for the user to close it
