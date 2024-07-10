# VSCODE
# File -> Preferences -> Settings: Buscar y Marcar "Python: Execute In File Dir"

from MiniGameEngine import GameWorld
from SpaceShip import SpaceShip
from Alien import Alien


class Game(GameWorld):
    def __init__(self, posicionX, posicionY):
        # Inicializamos el mundo del juego
        super().__init__(800, 600, title="Actividad 01", bgpic="Recursos/Fondo.png")

        # agregamos a los actores
        self.objetoNave = SpaceShip(posicionX, posicionY) #creamos un objeto de la clase nave
        self.Aliens = {}
        keys = range(7)
        values = [Alien(100,50), Alien(200,50), Alien(300,50), Alien(400,50), Alien(500,50), Alien(600,50), Alien(700,50)]
        for i in keys:
            self.Aliens[i] = values[i]
        """
        x = 100
        y = 50
        self.Aliens = []
        for i in range(7):
            #self.Aliens.append(Alien(x,y))
            self.Aliens["Alien_created"] = Alien(x,y)
            x = x + 100
        print(self.Aliens)


        Coordinadas originales
        Alien(100, 50)
        Alien(200, 50)
        Alien(300, 50)
        Alien(400, 50)
        Alien(500, 50)
        Alien(600, 50)
        Alien(700, 50)
        """

    def onUpdate(self, dt):
        fps = round(1 / dt, 1)
        # print(fps)
        vidaNave = self.objetoNave.getVida()
        # si la vida de la nave es menor o igual a 0, se cierra el juego
        if vidaNave <= 0:
            for i in range(7):
                self.Aliens.popitem()
                print(self.Aliens)
            input("Game Over, presiona Enter para cerrar el juego...")
            self.exitGame()

if __name__ == "__main__":
    print("Bienvenidos al juego Space Invaders")
    x = int(input("Ingresa la posición X para la nave: "))
    y = int(input("Ingresa la posición Y para la nave: "))

    game = Game(x,y)
    game.gameLoop(60)
