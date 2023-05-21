import pygame as pg

up = "up"
down = "down"

class Rocket:

    rocket_width = 20
    rocket_height = 70
    step = 6
    left = "левая"
    right = "правая"


    def __init__(self, surf, color, type):
        self.height = Rocket.rocket_height
        self.surf = surf
        self.color = color
        self.type = type
        if self.type == Rocket.left:
            self.x = surf.get_width() - Rocket.rocket_width
        elif self.type == Rocket.right:
            self.x = 0
        self.y_start = surf.get_height() // 2 - Rocket.rocket_height // 2
        self.y = self.y_start
        self.step = Rocket.step / ((1200//4)**2 + (650)**2)**(1/2) * (surf.get_width()**2 + surf.get_height()**2)**(1/2)
        pg.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.rocket_width, Rocket.rocket_height))



    def fly(self, direction=""):
        pg.draw.rect(self.surf, self.color, (self.x, self.y, Rocket.rocket_width, Rocket.rocket_height))
        if direction == up:
            self.y -= self.step
            if self.y + Rocket.rocket_height < 0:
                self.y = self.surf.get_height()
        elif direction == down:
            self.y += self.step
            if self.y > self.surf.get_height():
                self.y = 0 - Rocket.rocket_height