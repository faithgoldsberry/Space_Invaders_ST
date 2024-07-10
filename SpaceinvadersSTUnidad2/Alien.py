from MiniGameEngine import GameObject
from globals import global_score


class Alien(GameObject):
    paso_lateral = 100
    paso_vertical = 25

    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Alien.png", "Alien")
        self.desplazamiento = 0
        self.direccion = "derecha"
        self.orientacion = "adelante"
        self.contador = 0
        self.nivel = 0
        self.y_original = y

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        global global_score  # Use the global score variable
        if gobj.getTipo() == "Bullet":
            self.destroy()
            global_score += 1  # Increment the global score
            print("score:", global_score)
        elif gobj.getTipo() == "SpaceShip":
            self._gw.exitGame()
            print("Cuidado con la Nave Espacial")

    # actualizamos el estado del Alien en cada frame
    def onUpdate(self, dt):
        ww = self.getWorldWidth()
        w = self.getWidth()
        hh = self.getWorldHeight()
        h = self.getHeight()
        x = self.getX()
        y = self.getY()

        match self.direccion:
            case "derecha":
                x += 2
                self.desplazamiento += 2
                if self.desplazamiento >= self.paso_lateral:
                    self.direccion = "abajo"
                    self.desplazamiento = 0
            case "abajo":
                y += 4
                self.desplazamiento += 4
                if self.desplazamiento >= self.paso_vertical:
                    if self.orientacion == "adelante":
                        self.orientacion = "detras"
                        self.direccion = "izquierda"
                    else:
                        self.orientacion = "adelante"
                        self.direccion = "derecha"
                    self.desplazamiento = 0
            case "izquierda":
                x -= 2
                self.desplazamiento += 2
                if self.desplazamiento >= self.paso_lateral:
                    self.direccion = "abajo"
                    self.desplazamiento = 0

        if self.contador == 700:
            y= self.y_original
            self.contador = 0
            self.nivel += 1
        else:
            self.contador +=1
        self.setPosition(x, y)
        for i in range(self.nivel):
            self.desplazamiento +=1
