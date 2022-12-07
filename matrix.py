"""
    matrix.py calculates the cheapest way trough a matrix
    of numbers
"""

import random
import math
__author__ = "8070193"


def error_func(input_value: any):
    """
    prints out an error if the user_input is invalid

    Args:
        input_value (any): any userinput which doesnt match expected
        value
    """

    print(f"{input_value} ist kein valider Input!")
    print("")


def input_func():
    """
    accepts an integer input and blocks all other inputtypes

    Returns:
        integer: user_input to be used in other functions
    """
    while True:
        user_input = input("Bitte Matrix Dimension angeben: ")
        try:
            int(user_input)
            return user_input

        except ValueError:
            error_func(user_input)
            continue


def create_matrix(size: int):
    """
    creates a nested list of the given size

    Args:
        size (integer): size for the matrix to be created

    Returns:
        nested list: matrix of numbers
    """
    matrix_dim = list(range(1, 10))
    matrix_data = []

    for i in range(size):  # noqa: W0612
        matrix_data.append([random.choice(matrix_dim) for x in range(size)])

    return matrix_data


# TODO: find the cheapest way trough the matrix
#       for each field find adjacent fields and
#       find out which one is cheaper
#       replace used fields with inf
def find_way(matrix: list):
    """
    finds the cheapest way trough a matrix

    Args:
        matrix (list): list of lists to display our matrix
    """
    start_pos = matrix[0][0]
    end_pos = matrix[-1][-1]
    





def output_func(output: str, field: list):
    """
    prints out the perfect way trough the matrix

    Args:
        output (string): string of all used fields in perfect path
        field (list): list of lists used to display the matrix
    """


    for element in field:
        print(element)

    print("")
    print(f"Der Kürzeste Weg lautet wie folgt: {output}")



grid = create_matrix(3)
find_way(grid)
