import pygame
pygame.init()

TRAIN_SIZE = 80

NPC_SIZE = 50

# screen
WIDTH = 480
HEIGHT = 480

BLUE = (152,245,255)
BLUE2 = (121,205,205)
CORAL = (240,128,128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

GRID_SIZE = 20
GRID_WIDTH = WIDTH / GRID_SIZE
GRID_HEIGHT = HEIGHT / GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
font = pygame.font.Font('freesansbold.ttf', 30)

# NPC generate
npc1 = pygame.image.load("photos/LEGO_1.png")
npc1 = pygame.transform.scale(npc1, (NPC_SIZE, NPC_SIZE))

npc2 = pygame.image.load("photos/LEGO_2.png")
npc2 = pygame.transform.scale(npc2, (NPC_SIZE, NPC_SIZE))

npc3 = pygame.image.load("photos/LEGO_3.png")
npc3 = pygame.transform.scale(npc3, (NPC_SIZE, NPC_SIZE))

npc4 = pygame.image.load("photos/LEGO_4.png")
npc4 = pygame.transform.scale(npc4, (NPC_SIZE, NPC_SIZE))

npc5 = pygame.image.load("photos/LEGO_5.png")
npc5 = pygame.transform.scale(npc5, (NPC_SIZE, NPC_SIZE))

npc6 = pygame.image.load("photos/LEGO_6.png")
npc6 = pygame.transform.scale(npc6, (NPC_SIZE, NPC_SIZE))

npc7 = pygame.image.load("photos/LEGO_7.png")
npc7 = pygame.transform.scale(npc7, (NPC_SIZE, NPC_SIZE))

npc8 = pygame.image.load("photos/LEGO_8.png")
npc8 = pygame.transform.scale(npc8, (NPC_SIZE, NPC_SIZE))

npc9 = pygame.image.load("photos/LEGO_9.png")
npc9 = pygame.transform.scale(npc9, (NPC_SIZE, NPC_SIZE))

npc10 = pygame.image.load("photos/LEGO_10.png")
npc10 = pygame.transform.scale(npc10, (NPC_SIZE, NPC_SIZE))

npc11 = pygame.image.load("photos/LEGO_11.png")
npc11 = pygame.transform.scale(npc11, (NPC_SIZE, NPC_SIZE))

npc12 = pygame.image.load("photos/LEGO_12.png")
npc12 = pygame.transform.scale(npc12, (NPC_SIZE, NPC_SIZE))

npc13 = pygame.image.load("photos/LEGO_13.png")
npc13 = pygame.transform.scale(npc13, (NPC_SIZE, NPC_SIZE))

npc14 = pygame.image.load("photos/LEGO_14.png")
npc14 = pygame.transform.scale(npc14, (NPC_SIZE, NPC_SIZE))

npc_list = [npc1, npc2, npc3, npc4, npc5, npc6, npc7, npc8, npc9, npc10, npc11, npc12, npc13, npc14]

# train
TRAIN_UP = pygame.image.load("photos/train_up.png")
TRAIN_UP = pygame.transform.scale(TRAIN_UP, (TRAIN_SIZE, TRAIN_SIZE))
TRAIN_DOWN = pygame.image.load("photos/train_down.png")
TRAIN_DOWN = pygame.transform.scale(TRAIN_DOWN, (TRAIN_SIZE, TRAIN_SIZE))
TRAIN_LEFT = pygame.image.load("photos/train_left.png")
TRAIN_LEFT = pygame.transform.scale(TRAIN_LEFT, (TRAIN_SIZE, TRAIN_SIZE))
TRAIN_RIGHT = pygame.image.load("photos/train_right.png")
TRAIN_RIGHT = pygame.transform.scale(TRAIN_RIGHT, (TRAIN_SIZE, TRAIN_SIZE))

CART_UP = pygame.image.load("photos/cart_up.png")
CART_UP = pygame.transform.scale(CART_UP, (TRAIN_SIZE, TRAIN_SIZE))
CART_DOWN = pygame.image.load("photos/cart_down.png")
CART_DOWN = pygame.transform.scale(CART_DOWN, (TRAIN_SIZE, TRAIN_SIZE))
CART_LEFT = pygame.image.load("photos/cart_left.png")
CART_LEFT = pygame.transform.scale(CART_LEFT, (TRAIN_SIZE, TRAIN_SIZE))
CART_RIGHT = pygame.image.load("photos/cart_right.png")
CART_RIGHT = pygame.transform.scale(CART_RIGHT, (TRAIN_SIZE, TRAIN_SIZE))

TITLE1 = "WELCOME!"
TITLE2 =  "to the snake train game :)"
TITLE1_SIZE = int(0.15 * WIDTH)
TITLE_COLOR =(0,0,0)
TITLE_LOCATION1 = \
    (0.1 * WIDTH, HEIGHT / 6 - (TITLE1_SIZE / 6))
FONT_NAME = "Calibri"
TITLE1_FONT = 'georgia'

TITLE2_SIZE = int(0.07 * WIDTH)
TITLE_LOCATION2 = \
    (0.15 * WIDTH, HEIGHT / 3  - (TITLE2_SIZE / 6))

INSTRUCTIONS = ["Welcome to our game! the game purpose is",
                " to invite any of the game's characters" ,
                "into our special train!.",
                "how can we do that?",
                "when the train picks them up,",
                "you get 1 point to your score!",
                "and why is that good?",
                "your score is exchanged into money",
                "you can spend on the train services!",
                "in other words, this game allows you to get",
                "'free' rides "
                "based on your playing skills",
                " and consistency! :)",
                "so... Good Luck!! "]
INSTRUCTIONS_SIZE = int(0.05* WIDTH)
INSTRUCTIONS_COLOR = (0,0,0)
INSTRUCTIONS_LOCATION1x = 0.03 * WIDTH
INSTRUCTIONS_LOCATION1y = HEIGHT / 11 - (TITLE1_SIZE / 6)
FONT_INSTRUCTIONS = "arial"
