import time
from MiniGameEngine import GameObject
from Bullet import Bullet
from globals import global_score


class SpaceShip(GameObject):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/SpaceShip.png", "SpaceShip")
        self.lastBullet = time.time()

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        hh = self.getWorldHeight()
        h = self.getHeight()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("a"):
            x = x - 4
            if x - w / 2 < 0:
                x = w / 2
        elif self.isPressed("d"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
        elif self.isPressed("w"):
            y = y - 4
            if y - h / 2 < 0:
                y = h / 2
        elif self.isPressed("s"):
            y = y + 4
            if y > hh - h / 2:
                y = hh - h / 2
        self.setPosition(x, y)

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x, y - 30)
                self.lastBullet = time.time()
