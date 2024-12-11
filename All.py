
# CODE 1
def large_number_square(num):
    # Base case: if the number is small, directly return the square
    if len(num) == 1:
        return int(num) ** 2

    # Split the number into two halves
    mid = len(num) // 2
    left = num[:mid]  # Left part of the number
    right = num[mid:]  # Right part of the number

    # Convert to integers
    left_int = int(left)
    right_int = int(right)

    # Compute intermediate terms
    left_square = large_number_square(left)  # Square of left part
    right_square = large_number_square(right)  # Square of right part
    cross_term = left_int * right_int  # Product of left and right

    # Combine the results using base shifting
    n = len(right)  # Number of digits in the right part
    result = (10 ** (2 * n)) * left_square + (10 ** n) * 2 * cross_term + right_square

    return result


# Input a 20-digit number as a string
number = input("Enter the Number: ")
result = large_number_square(number)
print(f"The square of {number} is:\n{result}")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#CODE 2
def job_scheduling(jobs):
    # Sort jobs by profit in decreasing order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Find the maximum deadline
    max_deadline = max(job[0] for job in jobs)

    # Initialize the schedule (slots)
    schedule = [-1] * max_deadline  # -1 means slot is empty
    total_profit = 0

    # Assign jobs to slots
    for job in jobs:
        deadline, profit = job
        # Find a slot for this job (latest slot before its deadline)
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = profit  # Assign job's profit to this slot
                total_profit += profit
                break

    return schedule, total_profit


# Example input: List of (deadline, profit) for each job
jobs = [(4, 20), (1, 10), (1, 40), (1, 30)]  # Format: (deadline, profit)

# Get the schedule and total profit
schedule, total_profit = job_scheduling(jobs)

print("Job Schedule (profit in each slot):", schedule)
print("Total Profit:", total_profit)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#CODE 3

def floyd_warshall(graph):
    # Number of vertices
    n = len(graph)

    # Initialize distance matrix with the input graph
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0  # Distance to itself is zero
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]  # Distance is the edge weight

    # Floyd-Warshall algorithm
    for k in range(n):  # Intermediate nodes
        for i in range(n):  # Source node
            for j in range(n):  # Destination node
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example input graph: Adjacency matrix representation
# 0 means no direct connection between the cities
graph = [
    [0, 4, 0, 0, 0, 0],
    [4, 0, 8, 0, 0, 0],
    [0, 8, 0, 7, 0, 4],
    [0, 0, 7, 0, 9, 14],
    [0, 0, 0, 9, 0, 10],
    [0, 0, 4, 14, 10, 0]
]

# Compute shortest paths
shortest_paths = floyd_warshall(graph)

# Display the shortest path matrix
print("Shortest paths between all pairs of cities:")
for row in shortest_paths:
    print(row)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#CODE 4

import heapq


def network_delay_time(n, edges, k):
    # Create a graph as an adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((v, w))

    # Min-heap to keep track of the shortest distance to each node
    heap = [(0, k)]  # (time, node)
    shortest_time = {i: float('inf') for i in range(1, n + 1)}
    shortest_time[k] = 0

    # Perform Dijkstra's algorithm
    while heap:
        current_time, node = heapq.heappop(heap)

        # Skip processing if we've already found a shorter path
        if current_time > shortest_time[node]:
            continue

        # Update neighboring nodes
        for neighbor, time in graph[node]:
            new_time = current_time + time
            if new_time < shortest_time[neighbor]:
                shortest_time[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))

    # Find the maximum time to reach any node
    max_time = max(shortest_time.values())
    return max_time if max_time != float('inf') else -1


# Example usage
n = 4
edges = [
    (2, 1, 1),  # Edge from node 2 to node 1 with weight 1
    (2, 3, 1),  # Edge from node 2 to node 3 with weight 1
    (3, 4, 1)  # Edge from node 3 to node 4 with weight 1
]
k = 2  # Start node

result = network_delay_time(n, edges, k)
print("Time for all the nodes to receive the signal:", result)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#CODE 5

# Define possible moves for a knight
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]


def is_valid_move(x, y, board, n):
    # Check if the move is within bounds and the cell is unvisited
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def knight_tour(board, n, move_count, x, y):
    # If all squares are visited, return True
    if move_count == n * n:
        return True

    # Try all possible knight moves
    for move in knight_moves:
        next_x = x + move[0]
        next_y = y + move[1]

        if is_valid_move(next_x, next_y, board, n):
            # Mark the square with the move count
            board[next_x][next_y] = move_count

            # Recursively try the next move
            if knight_tour(board, n, move_count + 1, next_x, next_y):
                return True

            # Backtrack: Unmark the square
            board[next_x][next_y] = -1

    return False


def solve_knight_tour(n, start_x, start_y):
    # Create an NxN board initialized to -1
    board = [[-1 for _ in range(n)] for _ in range(n)]

    # Place the knight at the starting position
    board[start_x][start_y] = 0  # Start position is move 0

    # Start the backtracking algorithm
    if knight_tour(board, n, 1, start_x, start_y):
        # Print the solution board
        for row in board:
            print(row)
    else:
        print("No solution exists.")


# Example usage
n = 5  # Size of the chessboard
start_x, start_y = 0, 0  # Starting position
solve_knight_tour(n, start_x, start_y)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

#CODE 6

import sys


# A class to represent the node in branch and bound tree
class Node:
    def __init__(self, cost, level, assignment, reduced_cost_matrix):
        self.cost = cost  # The cost of current assignment
        self.level = level  # The current level in the tree (how many assignments made)
        self.assignment = assignment  # List to store current assignment
        self.reduced_cost_matrix = reduced_cost_matrix  # Reduced cost matrix after row and column reduction


def reduce_matrix(matrix, n):
    # Row reduction: subtract the minimum value from each row
    row_reduction = 0
    for i in range(n):
        row_min = min(matrix[i])
        if row_min != sys.maxsize:
            row_reduction += row_min
            for j in range(n):
                matrix[i][j] -= row_min

    # Column reduction: subtract the minimum value from each column
    col_reduction = 0
    for j in range(n):
        col_min = sys.maxsize
        for i in range(n):
            col_min = min(col_min, matrix[i][j])
        if col_min != sys.maxsize:
            col_reduction += col_min
            for i in range(n):
                matrix[i][j] -= col_min

    return row_reduction + col_reduction


def branch_and_bound(cost_matrix, n):
    # Initial matrix copy
    reduced_cost_matrix = [row[:] for row in cost_matrix]
    initial_cost = reduce_matrix(reduced_cost_matrix, n)

    # Initialize the root node
    root = Node(initial_cost, -1, [-1] * n, reduced_cost_matrix)

    # Min-heap to store nodes with the lowest cost
    pq = [root]
    best_cost = sys.maxsize
    best_assignment = [-1] * n

    while pq:
        # Get the node with the least cost
        current_node = pq.pop(0)

        # If this node's cost exceeds the best cost, we prune it
        if current_node.cost >= best_cost:
            continue

        # If we've assigned all students to clubs, check if the cost is the best
        if current_node.level == n - 1:
            if current_node.cost < best_cost:
                best_cost = current_node.cost
                best_assignment = current_node.assignment[:]
            continue

        # Branching: Try assigning the next student to every possible club
        for club in range(n):
            # If the club has already been assigned, skip it
            if club in current_node.assignment:
                continue

            # Create a new assignment by assigning the current student to the club
            new_assignment = current_node.assignment[:]
            new_assignment[current_node.level + 1] = club

            # Create a new cost matrix with the current assignment
            new_cost_matrix = [row[:] for row in current_node.reduced_cost_matrix]
            for i in range(n):
                new_cost_matrix[current_node.level + 1][i] = sys.maxsize  # Mark row as assigned
            for i in range(n):
                new_cost_matrix[i][club] = sys.maxsize  # Mark column as assigned

            # Reduce the matrix for the new assignment
            new_cost = current_node.cost + reduce_matrix(new_cost_matrix, n)

            # If the new cost is less than the best known cost, continue exploring this branch
            if new_cost < best_cost:
                pq.append(Node(new_cost, current_node.level + 1, new_assignment, new_cost_matrix))

    return best_cost, best_assignment


# Example usage
cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

n = len(cost_matrix)
best_cost, best_assignment = branch_and_bound(cost_matrix, n)

print("The minimum cost is:", best_cost)
print("The optimal assignment is:")
for i in range(n):
    print(f"Student {i + 1} assigned to Club {best_assignment[i] + 1}")
