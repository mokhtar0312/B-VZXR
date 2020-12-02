import os

import pandas as pd


class GetFinalPosition:
    def __init__(self):
        self.universe_file = 'universe.txt'
        self.instructions_file = 'instrucion_list.txt'

    def run(self):
        universe = self.load_universe()
        instructions = self.load_instructions()

    def load_universe(self) -> pd.DataFrame:
        """
        Loading the universe file in a panda dataframe
        :return: dataframe containing universe data
        """
        universe = pd.read_csv(os.path.join(os.getcwd(), 'resources', self.universe_file), sep=': ', header=None,
                               names=['side', 'size'])
        return universe

    def load_instructions(self) -> pd.DataFrame:
        """
        Loading the instructions file in a panda dataframe
        :return: dataframe containing instructions data
        """
        instructions = pd.read_csv(os.path.join(os.getcwd(), 'resources', self.instructions_file), sep=', ',
                                   header=None, names=['direction', 'steps'])
        return instructions


if __name__ == '__main__':
    GetFinalPosition = GetFinalPosition()
    GetFinalPosition.run()
