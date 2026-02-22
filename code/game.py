#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Hokai Fantasy")
        self.clock = pygame.time.Clock()
        self.running = True

        self.menu = Menu(self.window)

    def run(self):

        while self.running:
            self.handle_events()
            self.window.fill((0, 0, 0))  # limpa a tela
            self.menu.run()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False






        # Check for all events
        # for event in pygame.event.get():
        #       if event.type == pygame.QUIT:
        #       pygame.quit()  # Close Window
        #        quit()  # end pygame

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

