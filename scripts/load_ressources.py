import os

import pandas as pd


def load_ressources(universe_file: str, instructions_file: str):
    """
    This function is responsible of loading different files needed for the project
    :param universe_file: universe file name
    :param instructions_file: instructions file name
    :return:
    """
    universe = load_universe(universe_file)
    instructions = load_instructions(instructions_file)
    return universe, instructions


def load_universe(universe_file: str) -> pd.DataFrame:
    """
    Loading the universe file in a panda dataframe
    :param universe_file: universe file name
    :return: dataframe containing universe data
    """
    universe = pd.read_csv(
        os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), r'scripts\resources', universe_file),
        sep=': ', header=None,
        names=['side', 'size'])
    return universe


def load_instructions(instructions_file: str) -> pd.DataFrame:
    """
    Loading the instructions file in a panda dataframe
    :param instructions_file: instructions file name
    :return: dataframe containing instructions data
    """
    instructions = pd.read_csv(
        os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), r'scripts\resources', instructions_file),
        sep=', ',
        header=None, names=['direction', 'steps'])
    return instructions
