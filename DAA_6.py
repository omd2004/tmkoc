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
