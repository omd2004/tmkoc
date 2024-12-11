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
