import unittest
from test1 import mission

class testformission(unittest.TestCase):
    # Existing test

    def test_move_forward(self):
        ch = mission()
        ch.sat_move('f','N')
        self.assertEqual(ch.getPos(), [0, 1, 0])

    def test_move_backward(self):
        ch = mission()
        ch.sat_move('b','N')
        self.assertEqual(ch.getPos(), [0, -1, 0])

    def test_turn_left(self):
        ch = mission()
        ch.sat_turning('l','N')
        self.assertEqual(ch.getDirection(), 'W')

    def test_turn_right(self):
        ch = mission()
        ch.sat_turning('r','E')
        self.assertEqual(ch.getDirection(), 'S')

    def test_tilt_up(self):
        ch = mission()
        ch.sat_tilted('u','N')
        self.assertEqual(ch.getDirection(), 'U')

    def test_tilt_down(self):
        ch = mission()
        ch.sat_tilted('d','S')
        self.assertEqual(ch.getDirection(), 'D')

    def test_sequence_of_commands(self):
        ch = mission()
        commands = ['u','b','l']
        ch.execution(commands)
        self.assertEqual(ch.getPos(), [0, 0,-1])
        self.assertEqual(ch.getDirection(), 'W')

        cmd=['b','r','f','l','b','u','f','d']
        ch.execution(cmd)
        self.assertEqual(ch.getPos(), [2,1,0])
        self.assertEqual(ch.getDirection(), 'D')

        cmd2=['u','f','u','l','l','b','b']
        ch.execution(cmd2)
        self.assertEqual(ch.getPos(), [0,1,1])
        self.assertEqual(ch.getDirection(), 'E')