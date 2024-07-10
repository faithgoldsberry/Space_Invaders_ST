# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from SpaceShip import SpaceShip
from Alien import Alien
from globals import global_score


class Game(GameWorld):
    def __init__(self):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Actividad 01", bgpic="Recursos/Fondo.png")

        # agregamos a los actores
        SpaceShip(400, 540)
        x = 100
        y = 50
        for i in range(3):
            for j in range(6):
                Alien(x,y)
                x += 100
            x = 100
            y +=50

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        if self.isPressed("Escape"):
            self.exitGame()


# -- show time
if __name__ == "__main__":
    game = Game()
    game.gameLoop(60)
