import time
from MiniGameEngine import GameObject
from Bullet import Bullet


class SpaceShip(GameObject):
    # inicializamos la Nave Espacial
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/SpaceShip.png", "SpaceShip")
        self.lastBullet = time.time()
        self.vida = 4 # asignamos cantidad de vida a la nave

    # actualizamos el estado de la Nave Espacial en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # movimiento lateral
        if self.isPressed("Left"):
            x = x - 4
            if x - w / 2 < 0:
                x = w / 2
        elif self.isPressed("Right"):
            x = x + 4
            if x > ww - w / 2:
                x = ww - w / 2
        self.setPosition(x, y)

        # disparamos una bala
        if self.isPressed("space"):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x, y - 30)
                self.lastBullet = time.time()
    
    def restarVida(self):
        self.vida -= 1 # con cada colisión con un alíen, restamos una vida a la nave

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Alien":
            self.restarVida()

    # metodo que retorna el valor de la vida
    def getVida(self):
        return self.vida
