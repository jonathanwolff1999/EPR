"""
    matrix.py calculates the cheapest way trough a matrix
    of numbers
"""

import random
import math

__author__ = "8070193, Wolff"


def create_matrix(size: int):
    """
    creates a quadratic, nested list of the given size

    Args:
        size (integer): size for the matrix to be created

    Returns:
        nested list: matrix of numbers
    """

    # defines my values for the matrix generation
    matrix_dim = list(range(0, 9))
    matrix_data = []

    # create a nested list of random values inside the definitionrange
    for _ in range(size):
        matrix_data.append([random.choice(matrix_dim) for _ in range(size)])

    return matrix_data


def calc_cost(matrix, coord_x=0, coord_y=0, cost=0, iteration=0, indices=None):
    """
    recursive function to go trough a two dimensional matrix and finds cost
    of adjacent fields and takes the cheapest way trough it

    Parameters:
        matrix (list): matrix to be calculated
        coord_x (int): x coordinate of the current position
        coord_y (int): y coordinate of the current position
        cost (int): current cost
        iteration (int): current iteration
    """
    size = len(matrix)

    # breakpoints for recursion
    if coord_x == coord_y and coord_x == size - 1:
        indices.append((size - 1, size - 1))
        print(f"Iterationen: {iteration}")
        print(f"Pfad: {indices}")
        return cost

    if iteration >= size**2:
        raise Exception("Idk bruh, wyd?")
    # set initial cost to cost of node [0][0]
    if iteration == 0:
        cost = matrix[0][0]

    if indices is None:
        indices = []

    # calculate cost to move right and down
    cost_to_move_right = (
        matrix[coord_x][coord_y + 1] if coord_y < size - 1 else math.inf
    )
    cost_to_move_down = (
        matrix[coord_x + 1][coord_y] if coord_x < size - 1 else math.inf
    )
    # compare costs and move to the cheapest way
    if cost_to_move_down < cost_to_move_right:
        return calc_cost(
            matrix,
            coord_x + 1,
            coord_y,
            cost + cost_to_move_down,
            iteration + 1,
            indices + [(coord_x, coord_y)],
        )
    else:
        return calc_cost(
            matrix,
            coord_x,
            coord_y + 1,
            cost + cost_to_move_right,
            iteration + 1,
            indices + [(coord_x, coord_y)],
        )

def main():
    """
    main function to run the program
    """

    # creates a matrix of the given size
    field = create_matrix(int(input("Bitte Dimension angeben: ")))

    # prints the matrix
    for ele in field:
        print("(", end=" ")
        for pos in ele:
            print(pos, end=" ")

        print(")")

    # calculates the cheapest way trough the matrix
    costs = calc_cost(field)
    print(f"Kosten: {costs}")


# testcases for each function
if __name__ == "__main__":
    # testcases for create_matrix()

    # testcases for calc_cost()
    main()
