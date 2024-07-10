import unittest
from SpaceShip import SpaceShip
from Game import Game
from Alien import Alien

class TestAliens(unittest.TestCase):
    def test_cantidad_Aliens(self):
        self.game = Game(400,500)
        self.nave = SpaceShip(400,500)
        x = 100
        y = 50
        self.Aliens = []
        for i in range(7):
            self.Aliens.append(Alien(x,y))
            x = x + 100
        self.assertEqual(len(self.Aliens), 7)


if __name__ == "__main__":
    unittest.main()
