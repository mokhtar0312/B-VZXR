import pandas as pd


def get_final_position(position: tuple, orientation: str, universe: pd.DataFrame, instructions: pd.DataFrame) -> tuple:
    """
    function which will execute all mouvement instruction to find the final postion of the robot
    :param universe: the map dimensions
    :param instructions: the dataframe containing all consecutive instructions
    :return: tuple containing the final coordinate of the robot
    """
    for index, row in instructions.iterrows():
        orientation = get_new_orientation(orientation, row['direction'])
        position = get_new_position(position, orientation, row['steps'], universe)
    return position


def get_new_orientation(old_orientation: str, instruction: str) -> str:
    """
    Get the new orientation to take after reading a new instruction
    :param old_orientation: the old orientation of the robot
    :param instruction: the instruction to turn right or left
    :return: the new orientation of the robot
    """
    if old_orientation == 'up':
        if instruction == 'right':
            return 'right'
        else:
            return 'left'
    elif old_orientation == 'right':
        if instruction == 'right':
            return 'down'
        else:
            return 'up'
    elif old_orientation == 'down':
        if instruction == 'right':
            return 'left'
        else:
            return 'right'
    elif old_orientation == 'left':
        if instruction == 'right':
            return 'up'
        else:
            return 'down'


def get_new_position(actual_position: tuple, orientation: str, step: int, universe: pd.DataFrame) -> tuple:
    """
    Calculate new position after each move
    :param actual_position: the actual position of the robot
    :param orientation: the axe on which the robot will move
    :param step: steps on horizontal or vertical axe
    :param universe: universe file data containing the limits of the plan
    :return: the new coordinate of the robot
    """
    result = (0, 0)
    min_abs, max_abs = 0, int(universe[universe.side == 'width']['size']) - 1
    min_ord, max_ord = 0, int(universe[universe.side == 'height']['size']) - 1
    if orientation == 'up':
        if actual_position[1] + step > max_ord:
            result = (actual_position[0], max_ord)
        else:
            result = (actual_position[0], actual_position[1] + step)

    elif orientation == 'down':
        if actual_position[1] - step < min_ord:
            result = (actual_position[0], min_ord)
        else:
            result = (actual_position[0], actual_position[1] - step)

    elif orientation == 'right':
        if actual_position[0] + step > max_abs:
            result = (max_abs, actual_position[1])
        else:
            result = (actual_position[0] + step, actual_position[1])

    elif orientation == 'left':
        if actual_position[0] - step < min_abs:
            result = (min_abs, actual_position[1])
        else:
            result = (actual_position[0] - step, actual_position[1])
    return result
