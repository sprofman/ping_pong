import pygame as pg
from colors import *
from rokcet import *
from ball import *
from functions import *

pg.init()

display_width = 1200
display_height = 650

up = "up"
down = "down"

fps = 60

display = pg.display.set_mode((display_width, display_height))

display.fill(WHITE)

x_surf_left = 0
y_surf_left = 0
width_surf_left = display_width // 4
height_surf_left = display_height
surf_left = pg.Surface((width_surf_left, height_surf_left))
surf_left.fill(BLACK)


x_surf_right = display_width // 4 * 3
y_surf_right = 0
width_surf_right = display_width // 4
height_surf_right = display_height
surf_right = pg.Surface((width_surf_right, height_surf_right))
surf_right.fill(BLACK)


x_surf_middle = display_width // 4
y_surf_middle = 0
width_surf_middle = display_width // 2
height_surf_middle = display_height
surf_middle = pg.Surface((width_surf_middle, height_surf_middle))
surf_middle.fill(WHITE)

ball = Ball(surf_middle, color=GREEN)

left = "левая"
right = "правая"
color_rocket_left = WHITE
color_rocket_right = WHITE
rocket_left = Rocket(surf_left, color_rocket_left, left)
rocket_right = Rocket(surf_right, color_rocket_right, right)

size_font = 60
color_font = LIGHT_BLUE
text_score_1, text_score_2 = create_font(size_font, color_font)

display.blit(surf_middle, (x_surf_middle, y_surf_middle))
display.blit(surf_left, (x_surf_left, y_surf_left))
display.blit(surf_right, (x_surf_right, y_surf_right))
display.blit(text_score_1, (display_width // 8, display_height // 2))
display.blit(text_score_2, (display_width // 8 * 7, display_height // 2))

pg.display.update()

rele_pause = False
rele = True
while rele:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            rele = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                rele_pause = not rele_pause
            elif event.key == pg.K_ESCAPE:
                write_score(0, 0)

    if rele_pause == False:
        surf_right.fill(BLACK)
        rocket_right.fly()
        display.blit(surf_right, (x_surf_right, y_surf_right))

        surf_left.fill(BLACK)
        rocket_left.fly()
        display.blit(surf_left, (x_surf_left, y_surf_left))

        text_score_1, text_score_2 = create_font(size_font, color_font)
        display.blit(text_score_1, (display_width // 8, display_height // 2))
        display.blit(text_score_2, (display_width // 8 * 7, display_height // 2))
        pg.display.update()

        continue


    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        surf_left.fill(BLACK)
        rocket_left.fly(up)
        display.blit(surf_left, (x_surf_left, y_surf_left))
    if keys[pg.K_s]:
        surf_left.fill(BLACK)
        rocket_left.fly(down)
        display.blit(surf_left, (x_surf_left, y_surf_left))
    if keys[pg.K_o]:
        surf_right.fill(BLACK)
        rocket_right.fly(up)
        display.blit(surf_right, (x_surf_right, y_surf_right))
    if keys[pg.K_l]:
        surf_right.fill(BLACK)
        rocket_right.fly(down)
        display.blit(surf_right, (x_surf_right, y_surf_right))

    surf_middle.fill(WHITE)
    rele_pause = ball.move(rocket_left, rocket_right)
    display.blit(surf_middle, (x_surf_middle, y_surf_middle))

    surf_right.fill(BLACK)
    rocket_right.fly()
    display.blit(surf_right, (x_surf_right, y_surf_right))

    surf_left.fill(BLACK)
    rocket_left.fly()
    display.blit(surf_left, (x_surf_left, y_surf_left))

    text_score_1, text_score_2 = create_font(size_font, color_font)
    display.blit(text_score_1, (display_width // 8, display_height // 2))
    display.blit(text_score_2, (display_width // 8 * 7, display_height // 2))

    pg.display.update()

    pg.time.delay(1000 // fps)