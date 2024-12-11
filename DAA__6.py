import sys


# A function to reduce the cost matrix (row and column reduction)
def reduce_matrix(matrix, n):
    row_reduction, col_reduction = 0, 0

    # Row reduction
    for i in range(n):
        min_row = min(matrix[i])
        if min_row != sys.maxsize:  # Only subtract if a valid min exists
            row_reduction += min_row
            for j in range(n):
                matrix[i][j] -= min_row

    # Column reduction
    for j in range(n):
        min_col = min(matrix[i][j] for i in range(n))
        if min_col != sys.maxsize:  # Only subtract if a valid min exists
            col_reduction += min_col
            for i in range(n):
                matrix[i][j] -= min_col

    return row_reduction + col_reduction


# Branch and Bound for Assignment Problem
def branch_and_bound(cost_matrix, n):
    # Initialize best cost as maximum possible value
    best_cost = sys.maxsize
    best_assignment = [-1] * n

    # Priority queue with (cost, assignment, reduced cost matrix)
    pq = [(0, [-1] * n, [row[:] for row in cost_matrix])]  # Start with an empty assignment

    while pq:
        cost, assignment, matrix = pq.pop(0)

        # If all students are assigned, check the current cost
        if len(set(assignment)) == n:
            if cost < best_cost:
                best_cost = cost
                best_assignment = assignment[:]
            continue

        # Try assigning the next student to each unassigned club
        for club in range(n):
            if club not in assignment:
                new_assignment = assignment[:]
                new_assignment[len(set(new_assignment))] = club
                new_matrix = [row[:] for row in matrix]  # Copy the matrix

                # Mark the row and column as assigned
                for i in range(n):
                    new_matrix[len(set(new_assignment)) - 1][i] = sys.maxsize  # Mark row as assigned
                for i in range(n):
                    new_matrix[i][club] = sys.maxsize  # Mark column as assigned

                # Reduce the matrix for the new state
                new_cost = cost + reduce_matrix(new_matrix, n)

                # If the new cost is better, add it to the queue
                if new_cost < best_cost:
                    pq.append((new_cost, new_assignment, new_matrix))

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

print(f"Minimum cost: {best_cost}")
print(f"Optimal assignment: {best_assignment}")
