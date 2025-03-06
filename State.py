#Nour A. - Lab A
from collections import deque
import heapq

class State:
    def __init__(self, position, remaining_rewards):
        self.position = position  # (x, y)
        self.remaining_rewards = frozenset(remaining_rewards)

    def __lt__(self, other):
        return self.position < other.position  #comparisons needed

def get_neighbors(state, maze):
    x, y = state.position
    rows, cols = len(maze), len(maze[0])
    possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_moves = [
        (nx, ny) for nx, ny in possible_moves
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '%'
    ]
    return valid_moves

def is_goal(state):
    if len(state.remaining_rewards) == 0:
        print("Goal reached: The mouse is happy.")
        return True
    return False

def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    
    start = None
    rewards = set()

    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'P':
                start = (i, j)
            elif cell == '.':
                rewards.add((i, j))
    
    return maze, State(start, rewards)

def print_maze_solution(maze, path):
    maze_copy = [row[:] for row in maze]  # copy maze
    for x, y in path:
        if maze_copy[x][y] != '.':  # Keep rewards visible
            maze_copy[x][y] = '#'
    
    print("\nSolution:")
    for row in maze_copy:
        print("".join(row))

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def multi_astar(file_path):
    maze, initial_state = read_maze(file_path)
    priority_queue = [(0, 0, initial_state, [])]  # (f, g, state, path)
    visited = {}  # keys are (position, remaining_rewards)

    while priority_queue:
        _, g, state, path = heapq.heappop(priority_queue)
        print(f"Expanding: {state.position} | Remaining rewards: {state.remaining_rewards}")
        
        if (state.position, state.remaining_rewards) in visited and visited[(state.position, state.remaining_rewards)] <= g:
            continue
        visited[(state.position, state.remaining_rewards)] = g

        # if the reward gets collected, remove it (so no loop)
        new_rewards = set(state.remaining_rewards)
        if state.position in new_rewards:
            print(f"Collected reward at {state.position}!")
            new_rewards.remove(state.position)
        
        if not new_rewards:  # stop when all rewards are collected
            print("Goal reached! The mouse is happy.")
            print_maze_solution(maze, path)
            print(f"Path cost: {len(path)}")
            print(f"Nodes expanded: {len(visited)}")
            return path

        for move in get_neighbors(state, maze):
            updated_rewards = frozenset(new_rewards)  # Convert back to frozenset
            new_state = State(move, updated_rewards)
            print(f"Moving to {move} | New rewards left: {updated_rewards}")
            heuristic = sum(manhattan_distance(move, reward) for reward in updated_rewards)
            new_g = g + 1
            f = new_g + heuristic
            heapq.heappush(priority_queue, (f, new_g, new_state, path + [move]))

    print("The mouse is dead.")
    return None

if __name__ == "__main__":
    while True:
        file_name = input("Which maze do you want to throw the mouse at? Write the name: ")
        if file_name.lower() == "q":
            print("Quitting. The mouse escapes!")
            break
        try:
            multi_astar(file_name)  #so that I don't have  a hardcoded file.
            break
        except FileNotFoundError:
            print(f"Hmmmm..not sure that '{file_name}' is a correct maze name. Please try again or press 'q' to quit.")
