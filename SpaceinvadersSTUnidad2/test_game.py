import unittest
from SpaceShip import SpaceShip
from Game import Game

class TestPosition(unittest.TestCase):
    game = Game()

    def __init__(self, test):
        self.ox = 400
        self.oy = 540
        self.ss = SpaceShip(self.ox, self.oy)
        return super().__init__(test)

    def test_getX(self):
        self.assertEqual(self.ss.getX(), self.ox)

    def test_getY(self):
        self.assertEqual(self.ss.getY(), self.oy)

    def test_setPosition(self):
        x = 350
        y = 550
        self.ss.setPosition(x,y)
        self.assertEqual(self.ss.getX(), x)
        self.assertEqual(self.ss.getY(), y)
