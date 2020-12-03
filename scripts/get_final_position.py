import warnings

from load_ressources import load_ressources
from robot_actions import get_final_position

warnings.filterwarnings("ignore")


class GetFinalPosition:
    def __init__(self):
        self.universe_file = 'universe.txt'
        self.instructions_file = 'instrucion_list.txt'
        self.initial_position = (0, 0)
        self.initial_orientation = 'up'

    def run(self):
        universe, instructions = load_ressources(self.universe_file, self.instructions_file)
        final_position = get_final_position(self.initial_position, self.initial_orientation, universe,
                                            instructions)
        self.display_final_result(final_position)

    def display_final_result(self, final_position: tuple) -> None:
        """
        Displaying the final positiong of the robot
        :param final_position: The robot position
        :return:
        """
        print(f' The B-VZXR Robot will be in ( {final_position[0]} , {final_position[1]} ) !!!')


if __name__ == '__main__':
    GetFinalPosition = GetFinalPosition()
    GetFinalPosition.run()
