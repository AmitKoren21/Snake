import pygame, sys

import instructions

import button
import loading_bar
import main


def draw_message1(self, message, font_size, color, location):
    font = pygame.font.SysFont(consts.TITLE1_FONT, font_size)
    text_ing = font.render(message, True, color)
    screen.blit(text_ing, location)


def draw_message2(self, message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_ing = font.render(message, True, color)
    screen.blit(text_ing, location)


def draw_title1(self):
    draw_message1(self, consts.TITLE1, consts.TITLE1_SIZE, consts.TITLE_COLOR, consts.TITLE_LOCATION1)


def draw_title2(self):
    draw_message2(self, consts.TITLE2, consts.TITLE2_SIZE, consts.TITLE_COLOR, consts.TITLE_LOCATION2)


def draw_image1():
    dest = (180, 195)
    screen.blit(consts.npc10, dest)
    lego = pygame.transform.scale(consts.npc10, (100, 100))
    screen.blit(consts.npc10, dest)
    pygame.display.update()


def draw_image2():
    dest = (275, 277)
    screen.blit(consts.npc8, dest)
    lego = pygame.transform.scale(consts.npc8, (100, 100))
    screen.blit(consts.npc8, dest)
    pygame.display.update()


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'
        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw1(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def draw2(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation + 70
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def draw3(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation + 140
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    print('click')
                    if button1.pressed == True:
                        # loading_bar.loading_bar()
                        main.main()
                    elif button2.pressed == True:
                        instructions.draw_title1()
                    elif button3.pressed == True:
                        # loading_bar.loading_bar()
                        pygame.quit()
                        sys.exit()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None, 30)

button1 = Button('START', 200, 40, (150, 250), 5)
button2 = Button('HOW TO PLAY?', 200, 40, (150, 250), 5)
button3 = Button('QUIT', 200, 40, (150, 250), 5)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((121, 205, 205))
    button1.draw1()
    button2.draw2()
    button3.draw3()
    draw_title1(consts.TITLE1)
    draw_title2(consts.TITLE2)
    draw_image1()

    pygame.display.update()
    clock.tick(60)



mainue()
