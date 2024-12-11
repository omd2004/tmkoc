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
