from unittest import TestCase

import pandas as pd

from scripts.robot_actions import get_new_orientation, get_final_position, get_new_position


class TestRobotActions(TestCase):

    def test_get_final_position(self):
        position = (0, 0)
        orientation = 'up'
        d = {'side': ['width', 'height'], 'size': [5, 5]}
        universe = pd.DataFrame(data=d)
        c = {'direction': ['right', 'right'], 'steps': [10, 10]}
        instructions = pd.DataFrame(data=c)
        assert get_final_position(position, orientation, universe, instructions) == (4, 0)

    def test_get_final_position_type(self):
        position = (0, 0)
        orientation = 'up'
        d = {'side': ['width', 'height'], 'size': [5, 5]}
        universe = pd.DataFrame(data=d)
        c = {'direction': ['right', 'right'], 'steps': [10, 10]}
        instructions = pd.DataFrame(data=c)
        assert isinstance(get_final_position(position, orientation, universe, instructions), tuple)

    def test_get_new_orientation(self):
        old_orientation_cases = ['up', 'right', 'down', 'left']
        instructions_cases = ['right', 'left']
        results = ['right', 'left', 'down', 'up', 'left', 'right', 'up', 'down']
        i = 0
        for orient in old_orientation_cases:
            for instruction in instructions_cases:
                assert get_new_orientation(orient, instruction) == results[i]
                i += 1

    def test_get_new_orientation_type(self):
        assert isinstance(get_new_orientation('up', 'right'), str)

    def test_get_new_position_result(self):
        actual_position = (1, 5)
        orientation = 'up'
        step = 2
        d = {'side': ['width', 'height'], 'size': [10, 10]}
        universe = pd.DataFrame(data=d)
        assert get_new_position(actual_position, orientation, step, universe) == (1, 7)

    def test_get_new_position_type(self):
        actual_position = (1, 5)
        orientation = 'up'
        step = 2
        d = {'side': ['width', 'height'], 'size': [10, 10]}
        universe = pd.DataFrame(data=d)
        assert isinstance(get_new_position(actual_position, orientation, step, universe), tuple)
