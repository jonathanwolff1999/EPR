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

    # ask for a user_input until an integer is entered
    while True:
        user_input = input("Bitte Matrix Dimension angeben: ")
        try:
            user_input = int(user_input)
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

    # defines my values for the matrix generation
    matrix_dim = list(range(1, 10))
    matrix_data = []

    # create a nested list of random values inside the definitionrange
    for i in range(size):  # noqa: W0612
        matrix_data.append([random.choice(matrix_dim) for x in range(size)])

    return matrix_data


def create_dict(matrix: list):
    """
    finds the cheapest way trough a matrix

    Args:
        matrix (list): list of lists to display our matrix
    """
    # create a dict with key value pairs {key = index, value = node_weigth}
    positions = {}
    for element in matrix:
        first_ind = matrix.index(element)

        for coord in element:
            second_ind = element.index(coord)

            index = (first_ind, second_ind)
            positions[f'{index}'] =  (matrix[first_ind][second_ind])
    return positions


def get_pos(matrix: list, positions: dict, current_coords: tuple, size: int):
    """
    gets the current position and all adjacent positions

    Args:
        matrix (list): our matrix to step trough
        positions (dict): dictionary of all fields and their values
        current_coords (tuple): current coordinates
        size (int): size of our matrix

    Returns:
        _type_: _description_
    """
    end = (len(grid)-1, len(grid)- 1)
    path = []
    cost = 0
    adjacent = []
    north_value,west_value,south_value,east_value = 1000, 1000, 1000, 1000

    if current_coords == end:
        return path
    else:

        
        current_value = matrix[current_coords[0]][current_coords[1]]
        current_value = positions[f'{current_coords}']
        path.append(current_coords)



        if current_coords[0] != 0:
            north = ((current_coords[0] - 1), (current_coords[1]))
            north_value = positions[f'{north}']
            print(f"norden = {north}, value = {north_value}")
            adjacent.append(north_value)

        if current_coords[1] != 0:
            west = ((current_coords[0]), (current_coords[1] - 1))
            west_value = positions[f'{west}']
            print(f"westen = {west}, value = {west_value}")
            adjacent.append(west_value)

        if current_coords[0] < 3:
            south = ((current_coords[0] + 1), (current_coords[1]))
            south_value = positions[f'{south}']
            print(f"süden = {south}, value = {south_value}")
            adjacent.append(south_value)

        for idx,elem in enumerate(grid):
            if idx > len(grid):
                east = ((current_coords[0]), (current_coords[1] + 1))
                east_value = positions[f'{east}']
                print(f"osten = {east}, value = {east_value}")
                adjacent.append(east_value)
        print(f"hurensohnliste: {adjacent}")
        cheapest = find_cheapest(adjacent)



        blocker = -1
        int(blocker)


        if cheapest == north_value:
            positions.update({(f"{current_coords}"): blocker})
            cost += current_value
            current_coords = north
            get_pos(grid, positions, current_coords, size)

        if cheapest == west_value:
            positions.update({(f"{current_coords}"): blocker})
            cost += current_value
            current_coords = west
            get_pos(grid, positions, current_coords, size)

        if cheapest == south_value:
            positions.update({(f"{current_coords}"): blocker})
            cost += current_value
            current_coords = south
            get_pos(grid, positions, current_coords, size)

        if cheapest == east_value:
            positions.update({(f"{current_coords}"): blocker})
            cost += current_value
            current_coords = east
            get_pos(grid, positions, current_coords, size)


def find_cheapest(adjacent: list):
    """
    quick function to find the cheapest adjacent field

    Returns:
        integer: value of the cheapest adjacent field
    """
    print(adjacent)
    for elem in adjacent:
        int(elem)
    cheapest = min(adjacent)
    return cheapest




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


dimension = input_func()
grid = create_matrix(dimension)
for j in grid:
    for i in j:
        print(i, end="  ")
    print("")

print("")
print("")

position_list = create_dict(grid)
final_path = get_pos(grid, position_list, (0,0), dimension)
print(final_path)
