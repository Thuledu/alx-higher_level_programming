#!/usr/bin/python3
"""A function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n."""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.

    Args:
    - n: An integer representing the number of rows in Pascal's triangle.

    Returns:
    - A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
