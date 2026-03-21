import pygame
# C

C_TITLE_GOLDEN = (240, 200, 120)
C_SHADOW_GOLDEN = (80, 60, 30)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)# sombra
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

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
    'Level2Bg0': 1,
    'Level2Bg1': 2,
    'Level2Bg2': 2.5,
    'Level2Bg3': 3,
    'Level2Bg4': 3.5,


    'Enemy': 3,
    'Player1': 5,
    'Player2': 5,
    'DarkFire': 10,
    'FireFox': 10,


}

PLAYER_CONTROLS = {
    "Player1": {
        "left": pygame.K_a,
        "right": pygame.K_d,
        "jump": pygame.K_SPACE,
        "attack1": pygame.K_j,
        "attack2": pygame.K_k,
         "shoot": pygame.K_f,
    },

    "Player2": {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "jump": pygame.K_UP,
        "attack1": pygame.K_KP1,
        "attack2": pygame.K_KP2,
        "shoot": pygame.K_KP3,
    }

}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,

    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy': 10,
    'DarkFire': 1,
    'FireFox': 1,
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
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,

    'Player1': 50,
    'Player2': 50,
    'Enemy': 5,
    'DarkFire': 1,
    'FireFox': 1,

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,

    'Player1': 0,
    'Player2': 0,
    'Projectile': 0,
    'FireFox': 0,
    'DarkFire': 0,
    'Enemy': 100,
}

#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 10000

# W
WIN_WIDTH = 768
WIN_HEIGHT = 432