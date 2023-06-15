from collections import deque



################################################################# BFS ###############################################

def missionaries_and_cannibals_bfs():
    def bfs_search(start_state, goal):
        """
        Conducts a BFS search from the initial state to the goal state and returns the path
        """
        # Initialize the frontier and explored set
        frontier = [(start_state, [])]
        explored = set()

        # Continue until the frontier is empty or the goal state is found
        while frontier:
            state, path = frontier.pop(0)

            # Check if the current state is the goal state
            if state == goal:
                return path + [state]

            # Add the current state to the explored set
            explored.add(state)

            # Generate successor states and add them to the frontier
            for successor, action in successors(state):
                if successor not in explored:
                    frontier.append((successor, path + [state, action]))

        # If the goal state is not found, return None
        return None

    # Define the initial and goal states
    start_state = (3, 3, 1, 0, 0, 0)
    goal_state = (0, 0, 0, 3, 3, 1)

    # Find the solution path using BFS
    path = bfs_search(start_state, goal_state)

    # Print the solution path
    if path:
        print("From BFS Solution path:", path)
    else:
        print("No solution found")
################################################################# IDDFS ###############################################

def missionaries_and_cannibals_iddfs():

    def iddfs(start_state, goal_state, max_depth):
        for depth in range(max_depth):
            visited = set()
            path = []
            if dfs(start_state, goal_state, depth, visited, path):
                return path
        return None  # If goal state not found, return None

    def dfs(state, goal_state, depth, visited, path):
        visited.add(state)
        if state == goal_state:
            path.append((goal_state))
            return True
        if depth == 0:
            return False
        for next_state, action in successors(state):
            if next_state not in visited:
                path.append(state)
                path.append(action)
                if dfs(next_state, goal_state, depth - 1, visited, path):
                    return True
                path.pop()
                path.pop()
        return False

    start_state = (3, 3, 1, 0, 0, 0)
    goal_state = (0, 0, 0, 3, 3, 1)
    max_depth = 100  # Maximum depth to search for

    path = iddfs(start_state, goal_state, max_depth)
    if path:
        print("From IDDFS Solution path:", path)
    else:
        print("No path found within max depth.")

################################################################# GBFS ###############################################

def missionaries_and_cannibals_gbfs():

    def gbfs(start_state, goal_state):
        queue = [(heuristic(start_state), start_state,
                  [])]  # Initialize queue with start state and empty path, and heuristic score
        visited = set()  # Initialize visited set to keep track of visited states
        
        while queue:
            queue.sort()  # Sort queue by heuristic score
            score, state, path = queue.pop(0)  # Get state and path with lowest heuristic score

            if state == goal_state:  # If current state is the goal state, return path
                return path +[goal_state]

            visited.add(state)  # Add current state to visited set

            for next_state, action in successors(state):
                if next_state not in visited:  # If next state not visited, add to queue with updated path and heuristic score
                    queue.append((heuristic(next_state), next_state, path + [state, action]))

        return None  # If goal state not found, return None

        #heuristic(state)

    start_state = (
        3, 3, 1, 0, 0, 0)  # Start state with 3 missionaries and 3 cannibals on the left side, and boat on the left side
    goal_state = (
        0, 0, 0, 3, 3,
        1)  # Goal state with 3 missionaries and 3 cannibals on the right side, and boat on the right side

    path = gbfs(start_state, goal_state)

    if path :
        print("From GBFS Solution path:", path)
    else:
        print("No solution found")

################################################################# A STAR ###############################################

def missionaries_and_cannibals_astar():

    def astar(start_state, goal_state):
        queue = [(heuristic(start_state), start_state, [])] # Initialize queue with start state and empty path, and heuristic score
        visited = set() # Initialize visited set to keep track of visited states

        while queue:
            queue.sort() # Sort queue by heuristic score
            score, state, path = queue.pop(0) # Get state and path with lowest heuristic score

            visited.add(state) # Add current state to visited set

            if state == goal_state: # If current state is the goal state, return path
                return path + [goal_state]
            
            for next_state, action in successors(state):
                if next_state not in visited: # If next state not visited, add to queue with updated path and heuristic score
                    g_score = len(path) + 1 # Increment g_score by 1
                    h_score = heuristic(next_state) # Calculate h_score
                    f_score = g_score + h_score # Calculate f_score
                    queue.append((f_score, next_state, path + [state, action]))

        return None # If goal state not found, return None

        #heuristic(state)


    start_state = (3, 3, 1, 0, 0, 0) # Start state with 3 missionaries and 3 cannibals on the left side, and boat on the left side
    goal_state = (0, 0, 0, 3, 3, 1) # Goal state with 3 missionaries and 3 cannibals on the right side, and boat on the right side

    path = astar(start_state, goal_state)
    if path:
        print("From A* Solution path :", path)
    else:
        print("No solution found")

################################################################# HELP CALL FONCTION ###############################################

def successors(state):
    """
    Generates all possible successor states and corresponding actions for a given state
    """
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state

    if boat_left:  # Boat is on the left side
        for i in range(3):
            for j in range(3):
                if i + j == 1 or i + j == 2:  # One or two people in the boat
                    if i <= missionaries_left and j <= cannibals_left:  # Boat has enough people
                        new_state = (
                            missionaries_left - i, cannibals_left - j, 0, missionaries_right + i, cannibals_right + j,
                            1)
                        if is_valid_state(new_state):
                            action = (i, j, "right")
                            yield (new_state, action)
    else:  # Boat is on the right side
        for i in range(3):
            for j in range(3):
                if i + j == 1 or i + j == 2:  # One or two people in the boat
                    if i <= missionaries_right and j <= cannibals_right:  # Boat has enough people
                        new_state = (
                            missionaries_left + i, cannibals_left + j, 1, missionaries_right - i, cannibals_right - j,
                            0)
                        if is_valid_state(new_state):
                            action = (i, j, "left")
                            yield (new_state, action)

def is_valid_state(state):
    """
    Returns True if a given state is valid, i.e., no cannibal can outnumber missionaries on either side
    """
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state

    if missionaries_left != 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right != 0 and missionaries_right < cannibals_right:
        return False

    return True


################################################################# HURISTIC ###############################################

def heuristic(state):
    """
    Heuristic function that estimates the cost to reach the goal state.
    Admissible and consistent.
    """
    missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right, boat_right = state

    # Calculate number of missionaries and cannibals still on the left side
    missionaries_remaining = missionaries_left - boat_left
    cannibals_remaining = cannibals_left - boat_left

    # Calculate number of trips required to move all missionaries and cannibals to the right side
    trips = (missionaries_remaining + cannibals_remaining + 1) / 2

    # Calculate minimum number of steps required to move all missionaries and cannibals across the river
    min_steps = int(trips) * 2 - 1 if (missionaries_remaining + cannibals_remaining) % 2 == 1 else int(trips) * 2

    # Calculate estimated cost to reach goal state
    return min_steps


if __name__ == '__main__':
    missionaries_and_cannibals_bfs()
    missionaries_and_cannibals_iddfs()
    missionaries_and_cannibals_gbfs()
    missionaries_and_cannibals_astar()
