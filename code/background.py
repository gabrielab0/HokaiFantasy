#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


import pygame

from const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Background(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

        self.scroll = 0

        # escala correta do fundo
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        self.scroll -= ENTITY_SPEED[self.name]

        if self.scroll <= -self.rect.width:
            self.scroll += self.rect.width

    def draw(self, window):
        for i in range(3):
            window.blit(self.surf, (self.scroll + i * self.rect.width, 0))