#!/usr/bin/python3

from typing import List, Union

def matrix_divided(matrix: List[List[Union[int, float]]], div: Union[int, float]) -> List[List[Union[int, float]]]:
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (List[List[Union[int, float]]]): The matrix to be divided.
        div (Union[int, float]): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to zero.

    Returns:
        List[List[Union[int, float]]]: The new matrix with all elements divided by div.
    """
    # Validate the matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate the divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

