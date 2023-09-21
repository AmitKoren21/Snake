import time

import pygame
import button
import main

pygame.init()

scren = pygame.display.set_mode((consts.WIDTH, consts.HEIGHT))


def screen():
    scren.fill(consts.BLUE2)


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_INSTRUCTIONS, consts.INSTRUCTIONS_SIZE)
    text_img = font.render(message, True, color)
    scren.blit(text_img, location)


def draw_title1():
    pygame.init()

    while True:
        screen()
        for i in range(len(consts.INSTRUCTIONS)):
            instruction = consts.INSTRUCTIONS[i]
            draw_message(instruction, consts.INSTRUCTIONS_SIZE, consts.INSTRUCTIONS_COLOR,
                         (consts.INSTRUCTIONS_LOCATION1x, (i+1)*consts.INSTRUCTIONS_LOCATION1y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main.main()



