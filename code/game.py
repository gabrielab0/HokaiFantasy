#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import window

from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level



class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.last_event = None
        self.menu = Menu(self.window)

    def run(self):
        while self.running:

            menu_return = self.menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0] # [Player1, Player2]

                # LEVEL 1
                level = Level(self.window, 'Level1', menu_return, player_score)
                passou = level.run()

                # LEVEL 2
                if passou:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level.run()


                for bg in level.backgrounds:
                    bg.draw(self.window)

                pygame.display.flip()



            elif menu_return == MENU_OPTION[4]:
                self.running = False
