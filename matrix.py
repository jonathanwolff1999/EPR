"""
    matrix.py calculates the cheapest way trough a matrix
    of numbers
"""

import random

__author__ = "8070193"


def error_func(input_value):
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


def create_matrix(size):
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
def find_way(matrix):
    pass


# TODO: output the best way trough the matrix
def output_func(output):
    pass


matrix = create_matrix(3)
