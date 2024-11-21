import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import time

# Maze creation
def create_maze(): 
    maze = np.array([
        [0, 1, 0, 0, 0, 1, 0], 
        [0, 1, 0, 1, 0, 1, 0], 
        [0, 0, 0, 1, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 1, 0] 
    ]) 
    start = (0, 0)   # Top-left corner 
    goal = (4, 6)    # Bottom-right corner 
    return maze, start, goal

# Display the maze and path
def display_maze(maze, path=[]): 
    for position in path:
        maze[position] = 2  # Mark path with '2'

    plt.imshow(maze, cmap="coolwarm")
    plt.show()

# BFS
def bfs(maze, start, goal): 
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        (node, path) = queue.popleft()
        
        if node == goal:
            return path
        
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
            neighbor = (node[0] + d[0], node[1] + d[1])
            if (0 <= neighbor[0] < maze.shape[0] and 0 <= neighbor[1] < maze.shape[1] and 
                neighbor not in visited and maze[neighbor] == 0):
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # Return an empty path if no path is found


# Performance Analysis
def analyze_performance(algorithm, maze, start, goal): 
    start_time = time.time()
    path = algorithm(maze, start, goal)
    execution_time = time.time() - start_time
    space_complexity = len(path)
    return path, execution_time, space_complexity

# Main Execution
maze, start, goal = create_maze()

# BFS Results
bfs_path, bfs_time, bfs_space = analyze_performance(bfs, maze, start, goal)
print("BFS Path:", bfs_path)
print("BFS Time:", bfs_time)
print("BFS Space Complexity:", bfs_space)

display_maze(maze, bfs_path)