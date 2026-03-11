import pygame
# C

COLOR_TITLE_GOLDEN = (240, 200, 120)
COLOR_SHADOW_GOLDEN = (80, 60, 30)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 0)# sombra

#O
OUTLINE_COLOR = (80, 40, 0)

#M
MENU_OPTION = ('New Game 1P',
               'New Game 2P - Cooperative',
               'New Game 2P - Competitive',
               'Score',
               'Exit')

#E
ENTITY_SPEED = {
    'Level1Bg0': 0.1,
    'Level1Bg1': 0.2,
    'Level1Bg2': 0.5,
    'Level1Bg3': 1,
    'Level1Bg4': 1.5,
    'Level1Bg5': 2,
    'Level1Bg6': 2.5,
    'Level1Bg7': 2.5,
    'Player1': 2,
    'Player2': 2,
    'Enemy': 1,
}

PLAYER_CONTROLS = {
    "Player1": {
        "left": pygame.K_a,
        "right": pygame.K_d,
        "jump": pygame.K_SPACE,
        "attack1": pygame.K_j,
        "attack2": pygame.K_k
    },

    "Player2": {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "jump": pygame.K_UP,
        "attack1": pygame.K_KP1,
        "attack2": pygame.K_KP2
    }
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy': 50,
}



# W
WIN_WIDTH = 768
WIN_HEIGHT = 432