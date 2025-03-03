from collections import deque
import heapq

class State:
    def __init__(self, position, remaining_rewards):
        self.position = position  # (x, y)
        self.remaining_rewards = frozenset(remaining_rewards)  # {(x1, y1), (x2, y2), ...}
        
    def __lt__(self, other):
        return self.position < other.position

def get_neighbors(state, maze):
    x, y = state.position
    possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    valid_moves = [pos for pos in possible_moves if maze[pos[0]][pos[1]] != '%']
    return valid_moves

def is_goal(state):
    return len(state.remaining_rewards) == 0

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

def single_dfs(file_path):
    maze, initial_state = read_maze(file_path)
    stack = [(initial_state, [])]  # (current state, path taken)
    visited = set()

    while stack:
        state, path = stack.pop()
        
        if state.position in visited:
            continue
        visited.add(state.position)

        if is_goal(state):
            print_maze_solution(maze, path)
            print(f"Path cost: {len(path)}")
            print(f"Nodes expanded: {len(visited)}")
            return path
        
        for move in get_neighbors(state, maze):
            new_rewards = state.remaining_rewards - {move} if move in state.remaining_rewards else state.remaining_rewards
            new_state = State(move, new_rewards)
            stack.append((new_state, path + [move]))

    print("No solution found.")
    return None

def print_maze_solution(maze, path):
    maze_copy = [row[:] for row in maze]  # Make a copy of the maze
    for x, y in path:
        if maze_copy[x][y] != '.':  # Keep rewards visible
            maze_copy[x][y] = '#'
    
    print("\nSolution:")
    for row in maze_copy:
        print("".join(row))
single_dfs('test_maze.txt')

def single_bfs(file_path):
    maze, initial_state = read_maze(file_path)
    queue = deque([(initial_state, [])])  # (current state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state.position in visited:
            continue
        visited.add(state.position)

        if is_goal(state):
            print_maze_solution(maze, path)
            print(f"Path cost: {len(path)}")
            print(f"Nodes passed: {len(visited)}")
            return path

        for move in get_neighbors(state, maze):
            new_rewards = state.remaining_rewards - {move} if move in state.remaining_rewards else state.remaining_rewards
            new_state = State(move, new_rewards)
            queue.append((new_state, path + [move]))

    print("Sadly, the mouse is dead :(")
    return None

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def single_gbfs(file_path):
    maze, initial_state = read_maze(file_path)
    goal = next(iter(initial_state.remaining_rewards))  # 1prize,1goal
    
    priority_queue = [(manhattan_distance(initial_state.position, goal), initial_state, [])]
    visited = set()

    while priority_queue:
        _, state, path = heapq.heappop(priority_queue)


        if state.position in visited:
            continue
        visited.add(state.position)

        if is_goal(state):
            print_maze_solution(maze, path)
            print(f"Path cost: {len(path)}")
            print(f"Nodes passed: {len(visited)}")
            return path

        for move in get_neighbors(state, maze):
            new_rewards = state.remaining_rewards - {move} if move in state.remaining_rewards else state.remaining_rewards
            new_state = State(move, new_rewards)
            heapq.heappush(priority_queue, (manhattan_distance(move, goal), new_state, path + [move]))



    print("Sadly, the mouse is dead :(")
    return None

single_gbfs('test_maze.txt')
