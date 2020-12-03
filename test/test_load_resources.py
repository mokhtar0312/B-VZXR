from unittest import TestCase
from scripts.load_ressources import load_universe, load_instructions


class TestLoadRessources(TestCase):

    def test_load_universe_width(self):
        universe_file = 'universe.txt'
        df = load_universe(universe_file)
        assert int(df[df.side == 'width']['size']) > 0

    def test_load_universe_height(self):
        universe_file = 'universe.txt'
        df = load_universe(universe_file)
        assert int(df[df.side == 'height']['size']) > 0

    def test_load_instructions_direction(self):
        instructions_file = 'instrucion_list.txt'
        df = load_instructions(instructions_file)
        assert str(df.direction[0]) in ['right', 'left']

    def test_load_instructions_step(self):
        instructions_file = 'instrucion_list.txt'
        df = load_instructions(instructions_file)
        assert df.steps[0] >= 0
