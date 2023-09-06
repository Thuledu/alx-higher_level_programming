#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists: The new matrix with elements divided by div.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

