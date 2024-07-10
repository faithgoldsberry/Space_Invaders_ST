from MiniGameEngine import GameObject


class Alien(GameObject):
    # inicializamos el Alien
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Alien.png", "Alien")
        self.nivel = 1 # Inicializamos el nivel del juego

    # manejamos las colisiones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet":
            self.destroy()
            print("Alien:me dieron")

# actualizamos el estado del Alíen en cada frame
    def onUpdate(self, dt):
        # Obtener el ancho y alto del mundo
        ww = self.getWorldWidth()
        hh = self.getWorldHeight()
        # Obtener la posición actual del Alien
        x = self.getX()
        y = self.getY()
        # Velocidades de movimiento horizontal y vertical
        velocidad_horizontal = 2 + self.nivel # Aumentar la velocidad con el nivel
        velocidad_vertical = 2 + self.nivel
        # Movimiento horizontal
        while velocidad_horizontal > 0:
            x += 1
            if x >= ww:
                x = 0
            velocidad_horizontal -= 1

        # Movimiento vertical
        for i in range(velocidad_vertical):
            y += 1
            if y >= hh:
                y = 0
        # Actualizar la posición del Alien
        self.setPosition(x, y)

    def aumentarNivel(self):
        self.nivel += 1 # Incrementar el nivel del juego